from tkinter import *
from tkinter import ttk

def Velocity():
    h = float(result.get())  #get คืออะไร?
    cal = (2 * 9.18 * h)**0.5
    showRes.set(f'มวล M ในอุดมคติเมื่อตกจากที่สูง :{h} เมตร จะมีอัตราเร็ว: {cal:,.2f} เมตรต่อวินาที')
    #showRes.set คือ คำwส่งอะไร?
GUI = Tk() #Tk คือ คำสั้งอะไร?
GUI.title('My Program')
GUI.geometry('500x500')
#ได้ขนาดหน้าจอ

FONT = ('Angsana',16)

L1 = Label(GUI, text='Hello World',font=FONT)
L1.grid(column = 12,row = 12)


result = StringVar()
showRes = StringVar()

E1 = Entry(GUI,textvariable=result)
E1.grid(column = 12,row = 14)

B1 = ttk.Button(GUI,text='กดเพื่อแสดงผลลัพธ์',command=Velocity)
B1.grid(column = 12,row = 80,ipadx=90)

L2 = Label(GUI,textvariable=showRes,font=FONT)
L2.grid(column = 0,row = 3,columnspan=1)

GUI.mainloop()




'''
def Velocity(h):
    cal = (2 * 9.18 * h)**0.5
    print(f'มวล M ในอุดมคติเมื่อตกจากที่สูง :{h} เมตร จะมีอัตราเร็ว: {cal:,.2f} เมตรต่อวินาที')

Velocity(5)

while True:
     h = float(input('กรุณากรอกความสูง(ม.): '))
     Velocity(h)
     print('------')
'''

    
