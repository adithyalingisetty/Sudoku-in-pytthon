from tkinter import *
from functools import partial
l=[]

#--------------------------Solve Button Module-----------------------------------------

def s1(l1):
  k=[]
  for i in l1:
    k+=i
  for i in range(81):
    l[i].set(k[i])
  return

#---------------------------------------------------------------------------------------

def possible(y,x,n,l1):
  for i in range(9):
    if l1[i][x]==str(n):
      return False
  for i in range(9):
    if l1[y][i]==str(n):
      return False
  x1=(x//3)*3
  y1=(y//3)*3
  for i in range(3):
    for j in range(3):
      if l1[y1+i][x1+j] == str(n):
        return False
  return True

#----------------------------------------------------------------------------------------

def solve(l1):
  for i in range(9):
    for j in range(9):
      if l1[i][j] == '':
        for n in range(1,10):
          if possible(i,j,n,l1):
            l1[i][j]=str(n)
            solve(l1)
            l1[i][j]=''
        return
  #print(l1)
  s1(l1)
#-----------------------------------------------------------------------------------------
  
def read():
  l1=[]
  for i in range(9):
    l1.append([l[j].get() for j in range(9*i,(9*i)+9)])
  solve(l1)

#-----------------------------Reset Button Module-----------------------------------------
  
def rem():
  for i in range(81):
    l[i].set('')

#------------------------------------------------------------------------------------------
    
c1=partial(read)
c2=partial(rem)
c=Tk()
c.geometry('500x500')
c.title('SUDOKU SOLVER')
c.configure(background="SteelBlue1")
w=Canvas(c)

#------------------------------- Label declaration-------------------------------------------

s= Label(c,text='Sudoku Solving',bg='SteelBlue1',font=('times new roman',30,'bold'))
s.pack(side=TOP)
a="""Note: Fill given numbers at exact positions"""
s= Label(c,text=a,bg='SteelBlue1',font=('times new roman',13,'bold'))
s.pack(side=BOTTOM)

#------------------------------ Entry declaration---------------------------------------------

for i in range(81):
    l.append(StringVar())
    
p=1
q=1
for i in range(1,82):
    e1=Entry(c,width=8,font=('calibre',13,'normal'),justify=CENTER,textvariable=l[i-1]).place(x=35+(40*p),y=30+(q*40),height=32,width=32)
    q+=1
    if(q%10==0):
        p+=1
        q=1
for i in range(81):
  l[i].set('')
  
#----------------------------- Button declaration---------------------------------------------

b1= Button(c,width=13,text='Solve',command=c1,font=('',10,'bold'),cursor='hand2')
b1.place(x=150,y=440,height=30,width=50)
b2= Button(c,width=13,text='Reset',command=c2,font=('',10,'bold'),cursor='hand2')
b2.place(x=250,y=440,height=30,width=50)

c.mainloop()
