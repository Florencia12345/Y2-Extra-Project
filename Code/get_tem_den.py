import pyneb as pn 
s3 = pn.Atom('S', 3)

num =0
while num < 44000: 
    num += 1000
    print('num =', num)
    print(s3.getTemDen(0.77379, tem = num, wave1 = 187078.08, wave2 = 334703.72))