#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Let's try Face Detection API of Face++

Usage: 
    python3 face_detection.py [IMAGE_FILE] [SAVE_FILE]

[IMAGE_FILE]: original image file
[SAVE_FILE] : save file name

Output:
 After executing this script 3 files are ganerated.
 - SAVE_FILE.json ... Response data from Face Detection API
 - SAVE_FILE_attributes.png ... New image which some detected results are added on the original image
 - SAVE_FILE_landmarks.png ... New image which landmarks are added on the original image
"""
import requests
from PIL import Image, ImageDraw
import base64
import json
import os, sys
import math

def get_apikey():
    """
    To get 'API Key' and 'API secret' from external file
    for access to Face Detection Web API.
    The external files are named '.apikey' in this script but you can
    modifiy anything if you want.
    
    'API Key' and 'API Secret' are written with json form as below:
        {
        'api_key': '*****************',
        'api_secret':'******************'
        }    
     And this file is stored in the same directory as this script.   
     I recommend to grant proper permisson to this file due to security reason.     
    """
    #load API Keys
    with open('.apikey', 'r') as f:
        apikey = json.loads(f.read())
    
    return apikey['api_key'], apikey['api_secret']

def get_face_pos(p, r):
    """
    To get rectangle positoin with rotation angle 'r' degree
    Input: 
      p: face positon [width, top, left, height] from 'face_rectangle' attribute
         Note that this is list type. 
      r: head rotation angle from 'headpose_roll' attribute
    Output:
      4 corner positions(x, y) of rotated rectangle
    """
    # Change unit of angle from degree to radian
    theta = math.radians(r)
    
    # Calculate 4 corner positions from input 'p' 
    w, t, l, h = p[0], p[1], p[2], p[3]
    pos = [(l, t), (l+w, t), (l+w, t+h), (l, t+h)]
 
    # Calculate the center of rectangle
    center = (l+w/2, t+h/2)

    # Rotate rectangle and get new 4 positions
    rotated_pos = []
    for point in pos:
        x = center[0] + (point[0]-center[0])*math.cos(theta) - (point[1]-center[1])*math.sin(theta) 
        y = center[1] + (point[0]-center[0])*math.sin(theta) + (point[1]-center[1])*math.cos(theta) 
        
        rotated_pos.append((x, y))

    return rotated_pos
    
def face_detection(imgfile, savefile):
    """
    """
    ###########################################
    # Get response data from Face Detection API
    ###########################################

    #Get API key
    API_KEY, API_SECRET = get_apikey() 
    
    #Set image file and save file
    file_path = imgfile
    savefile = savefile
    
    #Open imagefile with binary (base64)
    with open(file_path, 'rb') as f:
        img_in = f.read()
    
    img_file = base64.encodebytes(img_in)
        
    #URL for Web API    
    url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
    
    #Set configuration
    config = {'api_key':API_KEY,
              'api_secret':API_SECRET,
              'image_base64':img_file,
              'return_landmark':1,
              'return_attributes':'gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus'}
    
    # POST to Web API
    res = requests.post(url, data=config)
    
    # Load json data
    data = json.loads(res.text)
    
    # Save json data to 'savefile'
    with open(savefile+'.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    # Display the response data on the screen
    data_json = json.dumps(data, indent=4)
    print(data_json)
    
    #########################################################
    # Dipict information from attribute on the original image
    #########################################################

    #Open original image file and create Image object
    img = Image.open(file_path)
    
    #Create ImageDraw Object
    img_draw = ImageDraw.Draw(img)
    
    for face in data['faces']:
        # Get attributes from API
        if 'attributes' in face:
            emotion = max(face['attributes']['emotion'].items(), key=lambda x:x[1])[0]
            gender = face['attributes']['gender']['value']
            age = face['attributes']['age']['value']
            mouthstatus = max(face['attributes']['mouthstatus'].items(), key=lambda x:x[1])[0]
            glass = face['attributes']['glass']['value']
            skinstatus = max(face['attributes']['skinstatus'].items(), key=lambda x:x[1])[0]
            ethnicity = face['attributes']['ethnicity']['value']
            headpose_roll = face['attributes']['headpose']['roll_angle'] 

            right_eye_gaze = face['attributes']['eyegaze']['right_eye_gaze']
            left_eye_gaze = face['attributes']['eyegaze']['left_eye_gaze']
            
            # Generate text data
            text = 'gender:{}\nage:{}\nethnicity:{}\nglass:{}\nemotion:{}\nmouth:{}\nskin:{}'.format(gender, age, ethnicity, glass, emotion, mouthstatus, skinstatus)
        else:
            # If there is no attribute parameters, values are defined for below script 
            text = ''
            headpose_roll = 0
            
        # Enclose detected face with rectangle
        face_rectangle = face['face_rectangle']
        face_pos = get_face_pos(list(face_rectangle.values()), headpose_roll)
        img_draw.polygon(face_pos, outline='lime')

        ## Display text information on the image 
        
        # calculate minimam x positon and minimum y positon of face rectangle
        min_x = min([x for x, y in face_pos])
        min_y = min([y for x, y in face_pos])
      
        # Get text size
        text_w, text_h = img_draw.textsize(text)

        # Positon tuning of text
        # (This code is not suitable for any cases. just temporary )
        if (min_x-2-text_w >= 0):
            img_draw.text((min_x-2-text_w, min_y), text, fill='lime')
        else:
            img_draw.text((min_x, min_y-2-text_h), text, fill='lime')
               
        # Gaze direction
        if 'landmark' in face: 
            # Get center of eye
            right_eye_center_x = face['landmark']['right_eye_center']['x']
            right_eye_center_y = face['landmark']['right_eye_center']['y']
            left_eye_center_x = face['landmark']['left_eye_center']['x']
            left_eye_center_y = face['landmark']['left_eye_center']['y']
            
            # Get geze direction from the eye center
            # unit vector of eye gaze * 'alpha' 
            # 'alpha' is coefficient for easy to see eye gaze line on the screen 
            alpha = 100
            r_gaze_x = alpha*right_eye_gaze['vector_x_component']
            r_gaze_y = alpha*right_eye_gaze['vector_y_component']
            l_gaze_x = alpha*left_eye_gaze['vector_x_component']
            l_gaze_y = alpha*left_eye_gaze['vector_y_component']
            
            img_draw.line([(right_eye_center_x, right_eye_center_y), (right_eye_center_x + r_gaze_x, right_eye_center_y + r_gaze_y)], fill='lime', width=1)
            img_draw.line([(left_eye_center_x, left_eye_center_y), (left_eye_center_x + l_gaze_x, left_eye_center_y + l_gaze_y)], fill='lime', width=1)
            
    
    #Save file    
    img.save(os.path.basename(file_path)[:-4] + '_attributes.png')
    img.show()
    
    #Check landmarks. These are displayed on other image file. 
    img2 = Image.open(file_path)
    img_draw2 = ImageDraw.Draw(img2)
    
    for face in data['faces']:
        if 'landmark' in face:
            for key in face['landmark'].keys():
                x = face['landmark'][key]['x']
                y = face['landmark'][key]['y']
                img_draw2.ellipse((x-1, y-1, x+1, y+1), fill='lime', outline='lime')
        else:
            continue

    #Save file    
    img2.save(os.path.basename(file_path)[:-4] + '_landmarks.png')
    img2.show()
        
    print('program end')

if __name__ == '__main__':
    
    # get command line arguments 
    if len(sys.argv) < 3:
        print('Argument is not enough. Add image filename and save filename.')
        sys.exit()
    else:
        imgfile = sys.argv[1]
        savefile = sys.argv[2]
    
    face_detection(imgfile, savefile)
    