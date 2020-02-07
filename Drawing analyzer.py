from tkinter import *
import numpy as np
import sys
np.set_printoptions(threshold=np.inf)
root = Tk()
stdoutOrigin=sys.stdout 
sys.stdout = open("shapesss.txt", "w")
height=500
width=600
size=100
shapes=4
height-=height%size
width-=width%size
x_cell=width//size
y_cell=height//size
shape=['ababab']*4

C = Canvas(root, bg="white", height=height, width=width)
C.pack()

F = Frame(root, bg='blue',height=50,width=width)
F.pack()

count=0
map=np.zeros([size,size],dtype=np.int8)
info=np.zeros([shapes,size,size],dtype=np.int8)

for i in range (1,size):
	C.create_line(0, y_cell*i, width, y_cell*i)
	C.create_line(x_cell*i, 0, x_cell*i, height)

def Save(map,info):
	global count
	if count<4:
		for i in range (0,size):
			for j in range (0,size):
				C.create_rectangle(i*x_cell, j*y_cell, (i+1)*x_cell, (j+1)*y_cell, fill="white")
				info[count,i,j]=map[i,j]
				map[i,j]=0
		shape[count]=entry.get()
		count+=1
	print(info[count-1])
def pencil(event):
	pos=[event.y//y_cell,event.x//x_cell]
	map[pos[0],pos[1]]=1
	C.create_rectangle(pos[1]*x_cell, pos[0]*y_cell, (pos[1]+1)*x_cell, (pos[0]+1)*y_cell, fill="black")

def brush(event):
	pos=[event.y//y_cell,event.x//x_cell]
	if pos[0]+2<=size-1 and pos[0]-2>=0 and pos[1]+2<=size-1 and pos[1]-2>=0:
		map[pos[0],pos[1]]=1
		C.create_rectangle((pos[1]+0)*x_cell, (pos[0]+0)*y_cell, (pos[1]+1)*x_cell, (pos[0]+1)*y_cell, fill="black")
		map[pos[0]+2,pos[1]]=1
		C.create_rectangle((pos[1])*x_cell, (pos[0]+2)*y_cell, (pos[1]+1)*x_cell, (pos[0]+3)*y_cell, fill="black")
		map[pos[0]+1,pos[1]]=1
		C.create_rectangle((pos[1])*x_cell, (pos[0]+1)*y_cell, (pos[1]+1)*x_cell, (pos[0]+2)*y_cell, fill="black")
		map[pos[0]-2,pos[1]]=1
		C.create_rectangle((pos[1])*x_cell, (pos[0]-2)*y_cell, (pos[1]+1)*x_cell, (pos[0]-1)*y_cell, fill="black")
		map[pos[0]-1,pos[1]]=1
		C.create_rectangle((pos[1])*x_cell, (pos[0]-1)*y_cell, (pos[1]+1)*x_cell, (pos[0])*y_cell, fill="black")
		map[pos[0]+2,pos[1]+1]=1
		C.create_rectangle((pos[1]+1)*x_cell, (pos[0]+2)*y_cell, (pos[1]+2)*x_cell, (pos[0]+3)*y_cell, fill="black")
		map[pos[0]+1,pos[1]+1]=1
		C.create_rectangle((pos[1]+1)*x_cell, (pos[0]+1)*y_cell, (pos[1]+2)*x_cell, (pos[0]+2)*y_cell, fill="black")
		map[pos[0]-2,pos[1]+1]=1
		C.create_rectangle((pos[1]+1)*x_cell, (pos[0]-2)*y_cell, (pos[1]+2)*x_cell, (pos[0]-1)*y_cell, fill="black")
		map[pos[0]-1,pos[1]+1]=1
		C.create_rectangle((pos[1]+1)*x_cell, (pos[0]-1)*y_cell, (pos[1]+2)*x_cell, (pos[0])*y_cell, fill="black")
		map[pos[0]+2,pos[1]-1]=1
		C.create_rectangle((pos[1]-1)*x_cell, (pos[0]+2)*y_cell, (pos[1])*x_cell, (pos[0]+3)*y_cell, fill="black")
		map[pos[0]+1,pos[1]-1]=1
		C.create_rectangle((pos[1]-1)*x_cell, (pos[0]+1)*y_cell, (pos[1])*x_cell, (pos[0]+2)*y_cell, fill="black")
		map[pos[0]-2,pos[1]-1]=1
		C.create_rectangle((pos[1]-1)*x_cell, (pos[0]-2)*y_cell, (pos[1])*x_cell, (pos[0]-1)*y_cell, fill="black")
		map[pos[0]-1,pos[1]-1]=1
		C.create_rectangle((pos[1]-1)*x_cell, (pos[0]-1)*y_cell, (pos[1])*x_cell, (pos[0])*y_cell, fill="black")
		map[pos[0]+2,pos[1]+2]=1
		C.create_rectangle((pos[1]+2)*x_cell, (pos[0]+2)*y_cell, (pos[1]+3)*x_cell, (pos[0]+3)*y_cell, fill="black")
		map[pos[0]+1,pos[1]+2]=1
		C.create_rectangle((pos[1]+2)*x_cell, (pos[0]+1)*y_cell, (pos[1]+3)*x_cell, (pos[0]+2)*y_cell, fill="black")
		map[pos[0]-2,pos[1]+2]=1
		C.create_rectangle((pos[1]+2)*x_cell, (pos[0]-2)*y_cell, (pos[1]+3)*x_cell, (pos[0]-1)*y_cell, fill="black")
		map[pos[0]-1,pos[1]+2]=1
		C.create_rectangle((pos[1]+2)*x_cell, (pos[0]-1)*y_cell, (pos[1]+3)*x_cell, (pos[0])*y_cell, fill="black")
		map[pos[0]+2,pos[1]-2]=1
		C.create_rectangle((pos[1]-2)*x_cell, (pos[0]+2)*y_cell, (pos[1]-1)*x_cell, (pos[0]+3)*y_cell, fill="black")
		map[pos[0]+1,pos[1]-2]=1
		C.create_rectangle((pos[1]-2)*x_cell, (pos[0]+1)*y_cell, (pos[1]-1)*x_cell, (pos[0]+2)*y_cell, fill="black")
		map[pos[0]-2,pos[1]-2]=1
		C.create_rectangle((pos[1]-2)*x_cell, (pos[0]-2)*y_cell, (pos[1]-1)*x_cell, (pos[0]-1)*y_cell, fill="black")
		map[pos[0]-1,pos[1]-2]=1
		C.create_rectangle((pos[1]-2)*x_cell, (pos[0]-1)*y_cell, (pos[1]-1)*x_cell, (pos[0])*y_cell, fill="black")
		map[pos[0],pos[1]+1]=1
		C.create_rectangle((pos[1]+1)*x_cell, (pos[0]+0)*y_cell, (pos[1]+2)*x_cell, (pos[0]+1)*y_cell, fill="black")
		map[pos[0],pos[1]-1]=1
		C.create_rectangle((pos[1]-1)*x_cell, (pos[0]+0)*y_cell, (pos[1])*x_cell, (pos[0]+1)*y_cell, fill="black")
		map[pos[0],pos[1]+2]=1
		C.create_rectangle((pos[1]+2)*x_cell, (pos[0]+0)*y_cell, (pos[1]+3)*x_cell, (pos[0]+1)*y_cell, fill="black")
		map[pos[0],pos[1]-2]=1
		C.create_rectangle((pos[1]-2)*x_cell, (pos[0]+0)*y_cell, (pos[1]-1)*x_cell, (pos[0]+1)*y_cell, fill="black")
		
	else:
		map[pos[0],pos[1]]=1
		C.create_rectangle(pos[1]*x_cell, pos[0]*y_cell, (pos[1]+1)*x_cell, (pos[0]+1)*y_cell, fill="black")

def Check(map,info):
	for i in range (0,size):
		for j in range (0,size):
			if map[i,j]==1:
				C.create_rectangle(j*x_cell, i*y_cell, (j+1)*x_cell, (i+1)*y_cell, fill="white")
	mappa =np.zeros([size,size],dtype=np.int8)
	mappan=np.zeros([size,size],dtype=np.int8)
	for i in range (0,size):
		cot=0
		for j in range (0,size):
			if map[i,j]==0:
				cot+=1
		if cot!=size:
			row1=i
			break
	for j in range (0,size):
		cot=0
		for i in range (0,size):
			if map[i,j]==0:
				cot+=1
		if cot!=size:
			col1=j
			break
	for i in range (size-1,-1,-1):
		cot=0
		for j in range (size-1,-1,-1):
			if map[i,j]==0:
				cot+=1
		if cot!=size:
			row2=i
			break
	for i in range (size-1,-1,-1):
		cot=0
		for j in range (size-1,-1,-1):
			if map[j,i]==0:
				cot+=1
		if cot!=size:
			col2=i
			break
	row_factor = size//(row2-row1+1)
	row_rem    = size% (row2-row1+1)
	col_factor = size//(col2-col1+1)
	col_rem    = size% (col2-col1+1)

	for i in range (row1,row2+1):
		ct=0
		for j in range (col1,col2+1):
			for k in range (0,col_factor):
				mappa[i,ct]=map[i,j]
				ct+=1
			if col_rem!=0:
				col_rem-=1
				mappa[i,ct]=map[i,j]
				ct+=1
		while ct!=size:
			mappa[ct]=0
			ct+=1
	for i in range (0,size):
		ct=0
		for j in range (row1,row2+1):
			for k in range (0,row_factor):
				mappan[ct,i]=mappa[j,i]
				ct+=1
			if row_rem!=0:
				row_rem-=1
				mappa[ct,i]=map[j,i]
				ct+=1
		while ct!=size:
			mappan[ct,i]=0
			ct+=1

	min=size**2
	J=[0]*len(info)
	for i in range (0,len(info)):
		for j in range (0,size):
			for k in range (0,size):
				J[i]+=(info[i][j][k]-mappan[j][k])**2
		if min>=J[i]:
			min=J[i]
			sh=i
	#4 shapes are admissible only
	print("The shape you've drawn is",shape[sh])
	Clear(map)
def Clear(map):
	for i in range (0,size):
		for j in range (0,size):
			if map[j,i]==1:
				C.create_rectangle(i*x_cell, j*y_cell, (i+1)*x_cell, (j+1)*y_cell, fill="white")
				map[j,i]=0

B1 = Button(F, text ="Check", relief=RAISED, command = lambda : Check(map,info))
B1.place(relx=0.45,rely=0)
B2 = Button(F, text ="Save", relief=RAISED, command = lambda : Save(map,info))
B2.place(relx=0.15,rely=0)
B3 = Button(F, text ="Clear", relief=RAISED, command = lambda : Clear(map))
B3.place(relx=0.75,rely=0)
entry = Entry(F, bg='white')
entry.place(relx=0.25, rely=0.6,relwidth=0.4, relheight=0.4)
C.bind('<B3-Motion>', brush)
C.bind('<B1-Motion>', pencil)

root.mainloop()
