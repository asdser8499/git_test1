#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
alphabet = {}
infilename = input("파일 이름을 입력하시오 : ")
infile = open(infilename, "r")
rfile = infile.read()
infile.close()

for line in rfile:
    for ch in line:
        if ch in alphabet:
            alphabet[ch] += 1
        else:
            alphabet[ch] = 1
print(alphabet)


# In[ ]:


file = input("입력 파일 이름: ")
infile = open(file, "r")
rfile = infile.readlines()
infile.close()

file = input("출력 파일 이름: ")
outfile = open(file,"w")

total = 0
avg = 0
count = 0
for s in rfile:
    total += float(s)
    count += 1
avg = total / count

print("합계="+str(total), file = outfile, end ="\n")
print("평균="+str(avg), file = outfile, end ="")

outfile.close()


# In[ ]:


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calcPerimeter(self):
        self.calcperimeter = 3.14 * 2 * self.radius
    def calcArea(self):
        self.calcarea = 3.14 * self.radius**2
    def __str__(self):
        msg = "반지름: "+str(self.radius) +" 원의 면적: "+str(self.calcperimeter) +" 원의 둘레: "+str(self.calcarea)
        return msg

myCircle = Circle(100)
myCircle.calcPerimeter()
myCircle.calcArea()
print(myCircle)


# In[ ]:


from turtle import *

class MyTurtle(Turtle): 
    def drawSquare(self):
        for i in range(4):
            self.right(90)
            self.forward(100)
my_turtle = MyTurtle()
my_turtle.forward(100)
my_turtle.drawSquare()


# In[ ]:




