from tkinter import *
import numpy as np
root = Tk()

# select the size of mesh
height = 600
width = 1300
# select the number of meshes in both directions
xn=100
yn=50
#Choose initial and final cell locations
st=[1,3]
end=[49,39]

#Leave the rest to us
count=0
height=(height//yn)*yn
width=(width//xn)*xn
y_cell=height//yn
x_cell=width//xn
mem=np.zeros([yn,xn],dtype=np.int16)
mem-=2
map=np.zeros([yn,xn],dtype=np.int8)

C = Canvas(root, bg="white", height=height, width=width)
C.pack()
for i in range (1,yn):
	C.create_line(0, y_cell*i, width, y_cell*i)
for i in range (1,xn):
	C.create_line(x_cell*i, 0, x_cell*i, height)

def create_barrier(event):
	pos=[event.y//y_cell,event.x//x_cell]
	cox=pos[1]*x_cell
	coy=pos[0]*y_cell
	C.create_rectangle(cox, coy, cox+x_cell, coy+y_cell, fill="black")
	map[pos[0],pos[1]]=-1

def define_nodes(event):
	global end
	global count
	global st
	if count==0:
		st=[event.y//y_cell,event.x//x_cell]
		count+=1
		cox=st[1]*x_cell 
		coy=st[0]*y_cell
		mem[st[0],st[1]]=0
		C.create_rectangle(cox, coy, cox+x_cell, coy+y_cell, fill="#fb0")
	else:
		end=[event.y//y_cell,event.x//x_cell]
		count+=1
		cox=end[1]*x_cell 
		coy=end[0]*y_cell
		C.create_rectangle(cox, coy, cox+x_cell, coy+y_cell, fill="#fb0")

def closest_path(map,pos):
	stack0=np.zeros([xn+yn,2],dtype=np.int16)
	stack0-=1
	step=0
	stack0[0]=[pos[0],pos[1]]
	while stack0[0][0]!=-1:
		stack1=np.zeros([xn+yn,2],dtype=np.int16)
		stack1-=1
		ar=0
		for k in stack0:
			if k[0]!=-1:
				if k[0]<yn-1 and map[k[0]+1,k[1]]!=-1 and mem[k[0]+1,k[1]]==-2:
					stack1[ar]=[k[0]+1,k[1]]
					ar+=1
					mem[k[0]+1,k[1]]=step+1
				if k[1]<xn-1 and map[k[0],k[1]+1]==0 and mem[k[0],k[1]+1]==-2:
					stack1[ar]=[k[0],k[1]+1]
					ar+=1
					mem[k[0],k[1]+1]=step+1
				if k[0]>0 and map[k[0]-1,k[1]]==0 and mem[k[0]-1,k[1]]==-2:
					stack1[ar]=[k[0]-1,k[1]]
					ar+=1
					mem[k[0]-1,k[1]]=step+1
				if k[1]>0 and map[k[0],k[1]-1]==0 and mem[k[0],k[1]-1]==-2:
					stack1[ar]=[k[0],k[1]-1]
					ar+=1
					mem[k[0],k[1]-1]=step+1
		step+=1
		stack0=stack1
def retract(mem,pos0,pos1):
	if mem[pos0,pos1]==-2:
		label = Label(root, text ="Cannot be reached", bg = 'yellow')
		label.place(relx=0.3 , rely=0, relwidth=0.45, relheight=0.25)
	elif mem[pos0,pos1]==0:
		return mem
	else:
		if pos0<yn-1 and mem[pos0,pos1]-mem[pos0+1,pos1]==1:
			C.create_rectangle((pos1)*x_cell, (pos0+1)*y_cell, (pos1+1)*x_cell, (pos0+2)*y_cell, fill='red')
			retract(mem,pos0+1,pos1)
		elif pos1<xn-1 and mem[pos0,pos1]-mem[pos0,pos1+1]==1:
			C.create_rectangle((pos1+1)*x_cell, (pos0)*y_cell, (pos1+2)*x_cell, (pos0+1)*y_cell, fill='red')
			retract(mem,pos0,pos1+1)
		elif pos0>0 and mem[pos0][pos1]-mem[pos0-1][pos1]==1:
			C.create_rectangle((pos1)*x_cell, (pos0-1)*y_cell, (pos1+1)*x_cell, (pos0)*y_cell, fill='red')
			retract(mem,pos0-1,pos1)
		elif pos1>0 and mem[pos0][pos1]-mem[pos0][pos1-1]==1:
			C.create_rectangle((pos1-1)*x_cell, (pos0)*y_cell, (pos1)*x_cell, (pos0+1)*y_cell, fill='red')
			retract(mem,pos0,pos1-1)

B1 = Button(root, text ="Find", relief=RAISED, command = lambda : closest_path(map,st))
B2 = Button(root, text ="Show", relief=RAISED, command = lambda : retract(mem,end[0],end[1]))
B1.pack()
B2.pack()
C.bind('<B1-Motion>', create_barrier)
C.bind('<Button-3>', lambda  event : define_nodes(event))
root.mainloop()