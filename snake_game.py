from tkinter import *
import numpy as np
from lib import lib
import random
import time

root=Tk()

height=650
width=1000
xn=40
yn=35
height-=height%yn
width-=width%xn
y_cell=height//yn
x_cell=width//xn

C = Canvas(root, bg="white", height=height, width=width)
C.pack()

for i in range (1,yn):
	C.create_line(0, y_cell*i, width, y_cell*i)
for i in range (1,xn):
	C.create_line(x_cell*i, 0, x_cell*i, height)

def move(snake):
	global food
	over=False
	C.create_rectangle(snake[0][1]*x_cell,snake[0][0]*y_cell,(snake[0][1]+1)*x_cell,(snake[0][0]+1)*y_cell, fill="white")
	if snake[-1][0]==food[0] and snake[-1][1]-food[1]==1 and v==-1:
		snake.append(food)
		rand=snake[0][0]*xn+snake[0][1]
		food=[rand//xn,rand%xn]
		while food in snake:
			rand=int(random.random()*(xn*yn))
			food=[rand//xn,rand%xn]
		C.create_rectangle(food[1]*x_cell,food[0]*y_cell,(food[1]+1)*x_cell,(food[0]+1)*y_cell, fill="Black")
	elif snake[-1][0]==food[0] and snake[-1][1]-food[1]==-1 and v==1:
		snake.append(food)
		rand=snake[0][0]*xn+snake[0][1]
		food=[rand//xn,rand%xn]
		while food in snake:
			rand=int(random.random()*(xn*yn))
			food=[rand//xn,rand%xn]
		C.create_rectangle(food[1]*x_cell,food[0]*y_cell,(food[1]+1)*x_cell,(food[0]+1)*y_cell, fill="Black")
	elif snake[-1][1]==food[1] and snake[-1][0]-food[0]==1 and v==2:
		snake.append(food)
		rand=snake[0][0]*xn+snake[0][1]
		food=[rand//xn,rand%xn]
		while food in snake:
			rand=int(random.random()*(xn*yn))
			food=[rand//xn,rand%xn]
		C.create_rectangle(food[1]*x_cell,food[0]*y_cell,(food[1]+1)*x_cell,(food[0]+1)*y_cell, fill="Black")
	elif snake[-1][1]==food[1] and snake[-1][0]-food[0]==-1 and v==-2:
		snake.append(food)
		rand=snake[0][0]*xn+snake[0][1]
		food=[rand//xn,rand%xn]
		while food in snake:
			rand=int(random.random()*(xn*yn))
			food=[rand//xn,rand%xn]
		C.create_rectangle(food[1]*x_cell,food[0]*y_cell,(food[1]+1)*x_cell,(food[0]+1)*y_cell, fill="Black")
	elif snake[-1][0]==yn-1 and v==-2:
		print("Game over")
		over=True
		snake.clear()
	elif snake[-1][0]==0 and v==2:
		print("Game over")
		over=True
		snake.clear()
	elif snake[-1][1]==xn-1 and v==1:
		print("Game over")
		over=True
		snake.clear()
	elif snake[-1][1]==0 and v==-1:
		print("Game over")
		over=True
		snake.clear()
	else:
		for i in range (0,len(snake)-1):
			snake[i]=snake[i+1]
		if v==1:
			if [snake[-1][0],snake[-1][1]+1] in snake:
				print("Game Over")
				over=True
			else:
				snake[-1]=[snake[-1][0],snake[-1][1]+1]
		elif v==-1:
			if [snake[-1][0],snake[-1][1]-1] not in snake:
				snake[-1]=[snake[-1][0],snake[-1][1]-1]
			else:
				print("Game Over")
				over=True
		elif v==2:
			if [snake[-1][0]-1,snake[-1][1]] in snake:
				print("Game Over")
				over=True
			else:
				snake[-1]=[snake[-1][0]-1,snake[-1][1]]
		else:
			if [snake[-1][0]+1,snake[-1][1]] in snake:
				print("Game Over")
				over=True
			else:
				snake[-1]=[snake[-1][0]+1,snake[-1][1]]
	for j in snake:
		C.create_rectangle(j[1]*x_cell,j[0]*y_cell,(j[1]+1)*x_cell,(j[0]+1)*y_cell, fill="green")
	if not over:
		root.after(100, lambda : move(snake))
def turn(event):
	global v
	x=event.x-width/2
	y=height/2-event.y
	if y-(height/width)*x>0 and y+(height/width)*x>0 and abs(v)==1:
		v=2
	if y-(height/width)*x>0 and y+(height/width)*x<0 and abs(v)==2:
		v=-1
	if y-(height/width)*x<0 and y+(height/width)*x>0 and abs(v)==2:
		v=1
	if y-(height/width)*x<0 and y+(height/width)*x<0 and abs(v)==1:
		v=-2
v=1
snake=list([[0,0],[0,1],[0,2]])
rand=snake[0][0]*xn+snake[0][1]
food=[rand//xn,rand%xn]
while food in snake:
	rand=int(random.random()*(xn*yn))
	food=[rand//xn,rand%xn]
C.create_rectangle(food[1]*x_cell,food[0]*y_cell,(food[1]+1)*x_cell,(food[0]+1)*y_cell, fill="Black")
for j in snake:
	C.create_rectangle(j[1]*x_cell,j[0]*y_cell,(j[1]+1)*x_cell,(j[0]+1)*y_cell, fill="green")
B1 = Button(root, text ="Start", relief=RAISED, command = lambda : move(snake))
B1.pack()
C.bind('<Button-1>', turn)
root.mainloop()