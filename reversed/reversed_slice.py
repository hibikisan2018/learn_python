import time
import sys
import matplotlib.pyplot as plt

def func(n):
    r = list(range(n))
    t0 = time.perf_counter()
    rev01 = reversed(r)
    t1 = time.perf_counter()
    rev02 = r[::-1]
    t2 = time.perf_counter()

    dt1 = t1-t0
    dt2 = t2-t1
    size01 = sys.getsizeof(rev01)
    size02 = sys.getsizeof(rev02)

    print(f'-- データ数：10^{i} --')
    print(f'reversed(): time: {dt1:.10f}(s), size: {size01}(bytes)')
    print(f'slice     : time: {dt2:.10f}(s), size: {size02}(bytes)')

    return dt1, dt2, size01/1024, size02/1024

x = []
y1 = []
y2 = []
s1 = []
s2 = []
for i in range(2, 7):
    dt1, dt2, size01, size02 = func(10**i)
    x.append(i)
    y1.append(dt1)
    y2.append(dt2)
    s1.append(size01)
    s2.append(size02)


fig, (ax1, ax2) = plt.subplots(ncols=2, nrows=1)
ax1.plot(x, y1, label='reserved()')
ax1.plot(x, y2, label='slice')
ax1.set_title('time')
ax1.set_xlabel('10^n')
ax1.set_ylabel('time(s)')
ax1.legend()
ax2.plot(x, s1, label='reserved()')
ax2.plot(x, s2, label='slice')
ax2.set_xlabel('10^n')
ax2.set_ylabel('size (kbytes)')
ax2.set_title('size')
ax2.legend()

plt.show()









