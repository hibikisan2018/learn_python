#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Let's try Face Detection API of Face++!

"""
import requests
from PIL import Image, ImageDraw
import base64
import json
import os, sys
import math

def get_apikey():
    """
    API Keys are stored with the form of json in '.apikey' file, 
    which is put in the same folder as this script and 
    should be granted proper permisson.
    """

    #load API Keys
    with open('.apikey', 'r') as f:
        apikey = json.loads(f.read())
    
    return apikey['api_key'], apikey['api_secret']

def get_face_pos(p, r):
    """
    To rotate rectangle with angle 'r' degree
    Input: 
      p: face_rectangle = list [width, top, left, height] from Face Detection API response 
      r: headpose_roll angle(degree)
    Output:
      4 corner positions(x, y) of rotated rectangle
    """
    w, t, l, h = p[0], p[1], p[2], p[3]
    # Change degree to radian
    theta = math.radians(r)
    
    pos = [(l, t), (l+w, t), (l+w, t+h), (l, t+h)]
    center = (l+w/2, t+h/2)

    rotated_pos = []
    for point in pos:
        x = center[0] + (point[0]-center[0])*math.cos(theta) - (point[1]-center[1])*math.sin(theta) 
        y = center[1] + (point[0]-center[0])*math.sin(theta) + (point[1]-center[1])*math.cos(theta) 
        
        rotated_pos.append((x, y))

    return rotated_pos
    
def face_detection(imgfile, savefile):
# Face detection

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
    
    #POST to Web API
    #And return response data with the form of json
    res = requests.post(url, data=config)
    
    #Load json data
    data = json.loads(res.text)
    
    #Save json data to 'savefile'
    with open(savefile+'.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    data_json = json.dumps(data, indent=4)
    print(data_json)
    
    #Display image with response data from API    
    #Open original image file and create Image object
    img = Image.open(file_path)
    
    #Create ImageDraw Object for add response information
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
            
            # Add text data around each face
            text = 'gender:{}\nage:{}\nethnicity:{}\nglass:{}\nemotion:{}\nmouth:{}\nskin:{}'.format(gender, age, ethnicity, glass, emotion, mouthstatus, skinstatus)
            text_w, text_h = img_draw.textsize(text)
        else:
            # If there is no attribute parameters, no 'text' is described and headpose is to 0 degree 
            text = ''
            headpose_roll = 0
            
        # Enclose detected face with rectangle
        face_rectangle = face['face_rectangle']
        face_pos = get_face_pos(list(face_rectangle.values()), headpose_roll)
        img_draw.polygon(face_pos, outline='lime')

        # calculate minimam x positon and minimum y positon of face rectangle
        min_x = min([x for x, y in face_pos])
        min_y = min([y for x, y in face_pos])
      
        # Display text
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
            
            # Get vector of eye gaze
            r_gaze_x = 100*right_eye_gaze['vector_x_component']
            r_gaze_y = 100*right_eye_gaze['vector_y_component']
            l_gaze_x = 100*left_eye_gaze['vector_x_component']
            l_gaze_y = 100*left_eye_gaze['vector_y_component']
            
            img_draw.line([(right_eye_center_x, right_eye_center_y), (right_eye_center_x + r_gaze_x, right_eye_center_y + r_gaze_y)], fill='lime', width=1)
            img_draw.line([(left_eye_center_x, left_eye_center_y), (left_eye_center_x + l_gaze_x, left_eye_center_y + l_gaze_y)], fill='lime', width=1)
            
    
    #Save file    
    img.save(os.path.basename(file_path)[:-4] + '_attributes.png')
    img.show()
    
    #Check landmarks
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
    
    if len(sys.argv) < 3:
        print('Argument is not enough. Add image filename and save filename.')
        sys.exit()
    else:
        imgfile = sys.argv[1]
        savefile = sys.argv[2]
    
    face_detection(imgfile, savefile)
    