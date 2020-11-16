# -*- coding: utf-8 -*-
import serial

t = serial.Serial('COM3', 9600)
b = t.read(3)
y = 0
p = 0
while b[0] != 170 or b[1] != 170 or b[2] != 4:
    b = t.read(3)
    print(b)
if b[0] == b[1] == 170 and b[2] == 4:
    a = b + t.read(5)
    print(a)
    if a[0] == 170 and a[1] == 170 and a[2] == 4 and a[3] == 128 and a[4] == 2:
        while 1:
            a = t.read(8)
            sum = ((0x80 + 0x02 + a[5] + a[6]) ^ 0xffffffff) & 0xff
            if a[0] == a[1] == 170 and a[2] == 32:
                y = 1
            else:
                y = 0
            if a[0] == 170 and a[1] == 170 and a[2] == 4 and a[3] == 128 and a[4] == 2:
                p = 1
            else:
                p = 0
            if sum != a[7] and y != 1 and p != 1:
                print("wrroy1")
                b = t.read(3)
                c = b[0]
                d = b[1]
                e = b[2]
                print(b)
                while c != 170 or d != 170 or e != 4:
                    c = d
                    d = e
                    e = t.read()
                    if c == (b'\xaa' or 170) and d == (b'\xaa' or 170) and e == b'\x04':
                        g = t.read(5)
                        print(g)
                        if c == b'\xaa' and d == b'\xaa' and e == b'\x04' and g[0] == 128 and g[1] == 2:
                            a = t.read(8)
                            print(a)
                            break
            if a[0] == 170 and a[1] == 170 and a[2] == 4 and a[3] == 128 and a[4] == 2:
                high = a[5]
                low = a[6]
                rawdata = (high << 8) | low
                if rawdata > 32768:
                    rawdata = rawdata - 65536
                sum = ((0x80 + 0x02 + high + low) ^ 0xffffffff) & 0xff
                if sum == a[7]:
                    vaul.append(rawdata)
                if sum != a[7]:
                    print("wrroy2")
                    b = t.read(3)
                    c = b[0]
                    d = b[1]
                    e = b[2]
                    while c != 170 or d != 170 or e != 4:
                        c = d
                        d = e
                        e = t.read()
                        if c == b'\xaa' and d == b'\xaa' and e == b'\x04':
                            g = t.read(5)
                            if c == b'\xaa' and d == b'\xaa' and e == b'\x04' and g[0] == 128 and g[1] == 2:
                                a = t.read(8)
                                break
            if a[0] == a[1] == 170 and a[2] == 32:
                c = a + t.read(28)
                print("Attention:"+str(c[32]))
                print("Meditation:"+str(c[34]))




