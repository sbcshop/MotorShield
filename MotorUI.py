#!/usr/bin/python

# GUI Code for PiMotor Shield V2
# Developed by: SB Components
# Author: Ankur
# Project: RPi Motor Shield

import tkinter as tkinter
import PiMotor

m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3) 
ar = PiMotor.Arrow(4)

def Start(check):
    print (check)
    print("check")
    
    
def M1Start():
    speed = float(w1.get())
    print ("Motor1 Start Running")
    print("-->Speed @ %s" % speed)
    if var1.get() == 1:
        m1.forward((speed))
    elif var1.get() == 2:
        m1.reverse(speed)
    else:
        print("M1 - Error")
        m1.stop()

def M1Stop():
    print ("Motor1 Stop")
    m1.stop()

def M2Start():
    speed = float(w2.get())
    print ("Motor2 Start Running")
    print("-->Speed @ %s" % speed)
    if var2.get() == 1:
        m2.forward((speed))
    elif var2.get() == 2:
        m2.reverse(speed)
    else:
        print("M2 - Error")
        m2.stop()

def M2Stop():
    print ("Motor2 Stop")
    m2.stop()

def M3Start():
    speed = float(w3.get())
    print ("Motor3 Start Running")
    print("-->Speed @ %s" % speed)
    if var3.get() == 1:
        m3.forward((speed))
    elif var3.get() == 2:
        m3.reverse(speed)
    else:
        print("M3 - Error")
        m3.stop()

def M3Stop():
    print ("Motor3 Stop")
    m3.stop()

def M4Start():
    speed = float(w4.get())
    print ("Motor4 Start Running")
    print("-->Speed @ %s" % speed)
    if var4.get() == 1:
        m4.forward((speed))
    elif var4.get() == 2:
        m4.reverse(speed)
    else:
        print("M4 - Error")
        m4.stop()

def M4Stop():
    print ("Motor4 Stop")
    m4.stop()

def A1_On():
    print ("Arrow-F ON")
    af.on()
    
def A1_Off():
    print ("Arrow-F OFF")
    af.off()

def A2_On():
    print ("Arrow-L ON")
    al.on()
    
def A2_Off():
    print ("Arrow-L OFF")
    al.off()

def A3_On():
    print ("Arrow-R ON")
    ar.on()
    
def A3_Off():
    print ("Arrow-R OFF")
    ar.off()

def A4_On():
    print ("Arrow-B ON")
    ab.on()
    
def A4_Off():
    print ("Arrow-B OFF")
    ab.off()
    
    
window = tkinter.Tk()
window.geometry('680x600')
window.title("Motor Shield GUI")
window.configure(background="#383a39")
frame = tkinter.Frame(window)
frame.pack(fill='both',expand='1')


polygon1 = [(5,40, 80,40, 80,20, 110,50, 80,80, 80,60, 5,60)]
polygon2 = [(193,40, 118,40, 118,20, 88,50, 118,80, 118,60, 193,60)]
polygon3 = [(45,210, 45,140, 25,140, 55,95, 85,140, 65,140, 65,210)]
polygon4 = [(45,0, 45,60, 25,60, 55,115, 85,60, 65,60, 65,0  )]

VALUES = [(polygon1, "red",  100, 200, 380, 270),(polygon2,"red",  100, 200, 100, 270),
          (polygon3, "blue", 250, 100, 285, 60), (polygon4,"blue", 250, 100, 285, 380)]

for b in range(4):
    canvas = tkinter.Canvas(frame,height=VALUES[b][2],width=VALUES[b][3],highlightthickness=0,bd=0)
    canvas.create_polygon((VALUES[b][0]),fill=VALUES[b][1],outline="white",width=1)
    canvas.place(x=VALUES[b][4],y=VALUES[b][5])
  
VALUES = [(30,  60), (30, 380), (450, 380), (450, 60)]

for b in range(4):
    cmd = lambda x=b: FUNC[b][0]
    cmd = lambda x=b: FUNC[b][1]
    canvas = tkinter.Canvas(frame,bg="#383a39",height = 200,width = 200,highlightthickness=0,bd=0)
    canvas.create_rectangle(190,190,10,10,outline="white",width=4)
    canvas.place(x=VALUES[b][0],y=VALUES[b][1])

BUTTON = [(50 ,200), (153, 200), (50, 520), (153, 520),
          (470, 200), (573, 200), (470, 520), (573, 520)]
FUNC = [("START", "green", M1Start), ("STOP", "red",  M1Stop),
        ("START", "green", M2Start), ("STOP", "red",  M2Stop),
        ("START", "green", M3Start), ("STOP", "red",  M3Stop),
        ("START", "green", M4Start), ("STOP", "red",  M4Stop),]

for b in range(8):
    cmd = lambda x=b: FUNC[b][2]
    tkinter.Button(frame,height=2,width=4,text=FUNC[b][0],fg="#a1dbcd",bg=FUNC[b][1],command=FUNC[b][2],highlightthickness=0).place(x=BUTTON[b][0],y=BUTTON[b][1])

LABELS = [("Motor 1", 15, "OliveDrab1",  90, 75), ("Motor 2", 15, "OliveDrab1",  90, 395),
          ("Motor 3", 15, "OliveDrab1",  510, 75), ("Motor 4", 15, "OliveDrab1",  510, 395),
          ("Motor Shield", 30, "grey",  222, 0), ("Direction", 12, "SkyBlue1",  50, 100),
          ("Speed: in %", 12, "SkyBlue1",  50, 160), ("Direction", 12, "SkyBlue1",  50, 420),
          ("Speed: in %", 12, "SkyBlue1",  50, 480), ("Direction", 12, "SkyBlue1",  470, 100),
          ("Speed: in %", 12, "SkyBlue1",  470, 160), ("Direction", 12, "SkyBlue1",  470, 420),
          ("Speed: in %", 12, "SkyBlue1",  470, 480)]

for b in range(13):
    lbl = tkinter.Label(frame,text=LABELS[b][0],bg="#383a39",font=('times',LABELS[b][1],'bold'),fg=LABELS[b][2])
    lbl.place(x=LABELS[b][3],y=LABELS[b][4])

BUTTONS = [(130, 270), (130,330),(510, 270), (510,330),
            (280, 110), (358,110),(280, 500), (358,500)]
FUNC = [("ON","green2", "green", A2_On), ("OFF","red2", "red",  A2_Off),
        ("ON","green2", "green", A3_On), ("OFF","red2", "red",  A3_Off),
        ("ON","green2", "green", A1_On), ("OFF","red2", "red",  A1_Off),
        ("ON","green2", "green", A4_On), ("OFF","red2", "red",  A4_Off),]

for b in range(8):
    cmd = lambda x=b: FUNC[b][3]
    tkinter.Button(frame,height=2,width=2,bg="thistle",text=FUNC[b][0],activebackground=FUNC[b][1],fg=FUNC[b][2],bd=2,command=FUNC[b][3]).place(x=BUTTONS[b][0],y=BUTTONS[b][1])

var1 = tkinter.IntVar()
tkinter.Radiobutton(frame,highlightthickness=0,text="Forward", variable=var1,value=1).place(x=50,y=125)
tkinter.Radiobutton(frame,highlightthickness=0,text="Backward", variable=var1,value=2).place(x=130,y=125)
w1 = tkinter.Spinbox(width=5,values=(100,90,80,70,60,50,40,30,20,10))
w1.place(x=145,y=160)

var2 = tkinter.IntVar()
tkinter.Radiobutton(frame,highlightthickness=0,text="Forward", variable=var2,value=1).place(x=50,y=445)
tkinter.Radiobutton(frame,highlightthickness=0,text="Backward", variable=var2,value=2).place(x=130,y=445)
w2 = tkinter.Spinbox(width=5,values=(100,90,80,70,60,50,40,30,20,10))
w2.place(x=145,y=480)

var3 = tkinter.IntVar()
tkinter.Radiobutton(frame,highlightthickness=0,text="Forward", variable=var3,value=1).place(x=470,y=125)
tkinter.Radiobutton(frame,highlightthickness=0,text="Backward", variable=var3,value=2).place(x=550,y=125)
w3 = tkinter.Spinbox(width=5,values=(100,90,80,70,60,50,40,30,20,10))
w3.place(x=565,y=160)

var4 = tkinter.IntVar()
tkinter.Radiobutton(frame,highlightthickness=0,text="Forward", variable=var4,value=1).place(x=470,y=445)
tkinter.Radiobutton(frame,highlightthickness=0,text="Backward", variable=var4,value=2).place(x=550,y=445)
w4 = tkinter.Spinbox(width=5,values=(100,90,80,70,60,50,40,30,20,10))
w4.place(x=565,y=480)
