'''
Created on Sep 29, 2013

@author: KHANHTRINH
'''
import math
from decimal import Decimal, ExtendedContext, setcontext
ExtendedContext.prec = 60
setcontext(ExtendedContext)
#from decimal import getcontext
def detect_triangle(a, b, c):
#    getcontext().prec = 10
    #if False not in [type(i) in [float, int] for i in (x,y,z)]
    #if type[a,b,c] in [float, int]:
    if ((type(a) in [float, long, int]) and (type(b) in [float, long, int]) and (type(c) in [float, long, int])
        and ((a >= 0) and (a <= (2**32-1))) and ((b >= 0) and (b <= (2**32-1))) and ((c >= 0) and (c <= (2**32-1)))):
        if (((Decimal(a) + Decimal(b)) > Decimal(c)) 
            and ((Decimal(a) + Decimal(c)) > Decimal(b)) 
                and ((Decimal(c) + Decimal(b)) > Decimal(a))):
            if a == b and b == c and c == a:
                return"Tam giac deu\n"
            elif (a == b) or (b == c) or (c == a):
                e = 1e-10
                if ((math.fabs(Decimal(c)**2 - Decimal(b)**2 - Decimal(a)**2) < e and a==b) 
                    or (math.fabs(Decimal(b)**2 - Decimal(c)**2 - Decimal(a)**2) < e and a==c) 
                        or (math.fabs(Decimal(a)**2 - Decimal(b)**2 - Decimal(c)**2) < e and b==c)):
                    return "Tam giac vuong can\n"
                else:
                    return"Tam giac can\n"
            elif ((math.fabs(Decimal(c)**2 - Decimal(b)**2 - Decimal(a)**2) < 1e-14) 
                or (math.fabs(Decimal(b)**2 - Decimal(c)**2 - Decimal(a)**2) < 1e-14) 
                    or (math.fabs(Decimal(a)**2 - Decimal(b)**2 - Decimal(c)**2) < 1e-14)):
                return"Tam giac vuong\n"
            else:
                return"Tam giac binh thuong\n" 
        else:
            return "Khong phai tam giac\n"
    else:
        return "Gia tri dau vao khong phu hop\n" 
    
    
