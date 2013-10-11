'''
Created on Oct 7, 2013

@author: KHANHTRINH
'''
import unittest
from random import randint
from Input import main
mystring = []   #test
dieukien = []   #cac bien va chuoi dieu kien
variable = []   #bien
maxlist = []    #Mang chua cac gia tri max
minlist = []    #Mang chua cac gia tri min
result = []     #Mang chua cac gia tri tra ve
inMain = False
#Kiem tra xem co nam trong doan comment hay khong
trongngoac = False
def checkin():
    return not trongngoac



'''
-------------------------------------------------------
Sap xep cac khoang theo chieu tang dan cua min
-DONE-
-------------------------------------------------------
'''
#Ham swap
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

#Sort
def bubblesort(A, B):
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if (A[j] < A[j-1]):
                swap(A, j, j-1)
                swap(B, j, j-1)
                

'''
-------------------------------------------------------
Doc tung dong file input
Neu nam trong doan comment => list: dieukien
-DONE-
-------------------------------------------------------
'''
with open("Input.py") as fp:
    for line in fp:
        #Tim duoc mien gia tri cua moi bien
        if line.strip() == "'''":
            trongngoac = checkin()
            continue
        if trongngoac == True:
            dieukien.append(line.strip())   #Ham strip de chuan hoa xau
        if "main" in line:
            inMain = True
        if (inMain == True) and ("return" in line):
            result.append(line[line.index("'")+1:len(line)-2]) 
        #if inMain == True:
            
        '''
        Kiem tra xem da o trong main chua.
        neu dang trong ham main thi tach cac phan return de tao ketqua
        '''
        #mystring.append(line)
        #print line
        

'''
-------------------------------------------------------
Tach nho cac dieu kien trong hang:
1. Tach ten bien => list: variable
2. Tra ve ket qua la list cac cum dieu kien: [[1; 5], [6; 10]]
-DONE-
-------------------------------------------------------
'''
def quantityOfCondition(conditionLine):
    tempVariable = conditionLine[0:conditionLine.index(":")]
    variable.append(tempVariable)
    temp1 = conditionLine[conditionLine.index(":")+2:len(conditionLine)]
    listOfTempCondition = []
    while temp1!="":
        listOfTempCondition.append(temp1[1:temp1.index("]")])   #substring
        temp1 = temp1[temp1.index("]")+1:len(temp1)]
    return listOfTempCondition

'''
----------------------------------------------------------------
Tach tung khoang trong cum [a; b] => minlist va maxlist
-DONE-
----------------------------------------------------------------
'''
def detailOfListCondition(listcondition):
    emax=[]
    emin=[]
    for eachCondition in listcondition:
        mini = eachCondition[0:eachCondition.index(";")]
        maxi = eachCondition[eachCondition.index(";")+2:len(eachCondition)]
        emax.append(int(maxi))
        emin.append(int(mini))
    bubblesort(emin,emax)
    maxlist.append(emax)
    minlist.append(emin)


'''
----------------------------------------------------------------
Chay ham detailOfListCondition o tren de insert vao maxList, min List
-DONE-
----------------------------------------------------------------
'''
def insertValueToArray():
    for i in range(len(dieukien)):
        detailOfListCondition(quantityOfCondition(dieukien[i]))

def TotalTestCase():
    n = 1
    for i in range(len(minlist)):
        n = n * len(minlist[i])
    return n
#print AListCondition[1]

'''
-------------------------------------------------------
Ham xac dinh xem dieu kien dau vao la dung hay sai
**** can xem xet
-------------------------------------------------------
'''
def checkConditionFailure(maxList, minList):
    if len(maxlist) != len(minList):    #Neu do dai 2 phan khong bang nhau thi FAIL
        #print "do dai 2 mang khong bang nhau"
        return False
    else:
        for j in range(len(maxList)):
            for i in range(1,len(maxList[j])):
                if (maxList[j][i] <= maxList[j][i-1]) or (minList[j][i] <= minList[j][i-1]) or (minList[j][i] <= maxList[j][i-1]):
                    return False
    return True



insertValueToArray()
#print result
#print TotalTestCase()
checkFail = checkConditionFailure(maxlist, minlist)
#print checkFail

#print variable
#print minlist
#print maxlist

'''
Ham sinh random tu 2 mang max va min
'''
def randomList(minlist, maxlist):
    mangRandom = minlist
    for i in range(len(minlist)):
        for j in range(len(minlist[i])):
            mangRandom[i][j] = randint(minlist[i][j], maxlist[i][j])
    return mangRandom


#print randomList(minlist, maxlist)


'''
Component 2
'''
bandau = randomList(minlist, maxlist)
listSau = bandau[0]

def getAllValue(list1, list2):
    listRs=[]
    for i in range(len(list1)):
        for j in range(len(list2)):
            listRs = listRs + [list1[i] + [list2[j]]]
    return listRs


def createTestCase(inputArr):
    listRtL = []
    for i in range(len(inputArr[0])):
        listRtL = listRtL + [[inputArr[0][i]]]
    listRsL = getAllValue(listRtL, inputArr[1])
    i = 2
    while i < len(inputArr):
        listRsL = getAllValue(listRsL, inputArr[i])
        i = i+1
    return listRsL

#print createTestCase(bandau)
    
'''
Component 3
'''
listTest = createTestCase(bandau)
tongTest = len(listTest)
n = len(variable)

class TestSequense(unittest.TestCase):
        pass

def test_generator(a, b):
    def test(self):
        self.assertEqual(a,b)
        #print a
    return test

if __name__ == '__main__':
    #print checkFail
    if checkFail == False:
        raise Exception("Invalid input")
        #setattr(TestSequense, "Exception: Input Data is Invalid", "")
    else:
        for i in range(tongTest):
            test_name = 'test_%s' % (i+1)
            
            value = 'main('
            for j in range(n-1):
                value = value + '%d'%listTest[i][j] + ','
            value = value + '%d'%listTest[i][len(listTest[i])-1] + ')'
            print main(*listTest[i])
            setOfTest = test_generator(main(*listTest[i]), "my unittest")
            setattr(TestSequense, test_name, setOfTest)
    
    unittest.main()