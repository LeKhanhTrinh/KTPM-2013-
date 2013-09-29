'''
Created on Sep 29, 2013

@author: KHANHTRINH
'''
import math
#from decimal import getcontext
def detect_triangle(a, b, c):
#    getcontext().prec = 10
    #if False not in [type(i) in [float, int] for i in (x,y,z)]
    #if type[a,b,c] in [float, int]:
    if ((type(a) in [float, long, int]) and (type(b) in [float, long, int]) and (type(c) in [float, long, int])
        and ((a > 0) and (a <= (2**32-1))) and ((b > 0) and (b <= (2**32-1))) and ((c > 0) and (c <= (2**32-1)))):
        if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):
            if a == b and b == c and c == a:
                return"Tam giac deu\n"
            elif (a == b) or (b == c) or (c == a):
                e = 1e-10
                if (math.fabs(c*c - b*b - a*a) < e) or (math.fabs(b*b - c*c - a*a) < e) or (math.fabs(a*a - b*b - c*c) < e):
                    return "Tam giac vuong can\n"
                else:
                    return"Tam giac can\n"
            elif (math.fabs(c*c - b*b - a*a) < 1e-10) or (math.fabs(b*b - c*c - a*a) < 1e-10) or (math.fabs(a*a - b*b - c*c) < 1e-10):
                return"Tam giac vuong\n"
            else:
                return"Tam giac binh thuong\n" 
        else:
            return "Khong phai tam giac\n"
    else:
        return "Gia tri dau vao khong phu hop\n" 
    
    
