#!/usr/bin/python

# GUI Code for PiMotor Shield V2
# Developed by: SB Components

# Author: Ankur
# Project: RPi Motor Shield

import tkinter as tkinter
import PiMotor

m1 = PiMotor.Motor("MOTOR1", 1)
m2 = PiMotor.Motor("MOTOR2", 1)
m3 = PiMotor.Motor("MOTOR3", 1)
m4 = PiMotor.Motor("MOTOR4", 1)

ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3)
ar = PiMotor.Arrow(4)


def Start(check):
    print(check)
    print("check")


def M1Start():
    speed = float(w1.get())
    motor_button[0].configure(bg='green', activebackground="gray")
    motor_button[1].configure(bg='white', activebackground="red")
    print("Motor1 Start Running")
    print("-->Speed @ %s" % speed)
    if var1.get() == 1:
        m1.forward((speed))
    elif var1.get() == 2:
        m1.reverse(speed)
    else:
        print("M1 - Error")
        m1.stop()


def M1Stop():
    motor_button[0].configure(bg='white', activebackground="green")
    motor_button[1].configure(bg='red', activebackground="gray")
    print("Motor1 Stop")
    m1.stop()


def M2Start():
    speed = float(w2.get())
    motor_button[2].configure(bg='green', activebackground="gray")
    motor_button[3].configure(bg='white', activebackground="red")
    print("Motor2 Start Running")
    print("-->Speed @ %s" % speed)
    if var2.get() == 1:
        m2.forward((speed))
    elif var2.get() == 2:
        m2.reverse(speed)
    else:
        print("M2 - Error")
        m2.stop()


def M2Stop():
    motor_button[2].configure(bg='white', activebackground="green")
    motor_button[3].configure(bg='red', activebackground="gray")
    print("Motor2 Stop")
    m2.stop()


def M3Start():
    speed = float(w3.get())
    motor_button[4].configure(bg='green', activebackground="gray")
    motor_button[5].configure(bg='white', activebackground="red")
    print("Motor3 Start Running")
    print("-->Speed @ %s" % speed)
    if var3.get() == 1:
        m3.forward((speed))
    elif var3.get() == 2:
        m3.reverse(speed)
    else:
        print("M3 - Error")
        m3.stop()


def M3Stop():
    motor_button[4].configure(bg='white', activebackground="green")
    motor_button[5].configure(bg='red', activebackground="gray")
    print("Motor3 Stop")
    m3.stop()


def M4Start():
    speed = float(w4.get())
    motor_button[6].configure(bg='green', activebackground="gray")
    motor_button[7].configure(bg='white', activebackground="red")
    print("Motor4 Start Running")
    print("-->Speed @ %s" % speed)
    if var4.get() == 1:
        m4.forward((speed))
    elif var4.get() == 2:
        m4.reverse(speed)
    else:
        print("M4 - Error")
        m4.stop()


def M4Stop():
    motor_button[6].configure(bg='white', activebackground="green")
    motor_button[7].configure(bg='red', activebackground="gray")
    print("Motor4 Stop")
    m4.stop()


def A1_On():
    arrow_canvas[2].itemconfig(1, fill='blue')
    button_led[4].configure(bg="green", activebackground="gray")
    button_led[5].configure(bg="gray", activebackground="red")
    print("Arrow-F ON")
    af.on()


def A1_Off():
    arrow_canvas[2].itemconfig(1, fill='white')
    button_led[4].configure(bg="gray", activebackground="green")
    button_led[5].configure(bg="red", activebackground="red")
    print("Arrow-F OFF")
    af.off()


def A2_On():
    arrow_canvas[1].itemconfig(1, fill='red')
    button_led[0].configure(bg="green", activebackground="gray")
    button_led[1].configure(bg="gray", activebackground="red")
    print("Arrow-L ON")
    al.on()


def A2_Off():
    arrow_canvas[1].itemconfig(1, fill='white')
    button_led[0].configure(bg="gray", activebackground="green")
    button_led[1].configure(bg="red", activebackground="red")
    print("Arrow-L OFF")
    al.off()


def A3_On():
    arrow_canvas[0].itemconfig(1, fill='red')
    button_led[2].configure(bg="green", activebackground="gray")
    button_led[3].configure(bg="gray", activebackground="red")
    print("Arrow-R ON")
    ar.on()


def A3_Off():
    arrow_canvas[0].itemconfig(1, fill='white')
    button_led[2].configure(bg="gray", activebackground="green")
    button_led[3].configure(bg="red", activebackground="red")
    print("Arrow-R OFF")
    ar.off()


def A4_On():
    arrow_canvas[3].itemconfig(1, fill='blue')
    button_led[6].configure(bg="green", activebackground="gray")
    button_led[7].configure(bg="gray", activebackground="red")
    print("Arrow-B ON")
    ab.on()


def A4_Off():
    arrow_canvas[3].itemconfig(1, fill='white')
    button_led[6].configure(bg="gray", activebackground="green")
    button_led[7].configure(bg="red", activebackground="red")
    print("Arrow-B OFF")
    ab.off()


window = tkinter.Tk()

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth() / 3 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 4 - windowHeight / 2)

# Position the window
window.geometry("680x600+{}+{}".format(positionRight, positionDown))

window.title("Motor Shield GUI")
window.resizable(False, False)

frame = tkinter.Frame(window)
frame.pack(fill='both', expand='1')
frame.configure(bg='black')

#  Arrows
polygon1 = [(5, 40, 80, 40, 80, 20, 110, 50, 80, 80, 80, 60, 5, 60)]
polygon2 = [(193, 40, 118, 40, 118, 20, 88, 50, 118, 80, 118, 60, 193, 60)]
polygon3 = [(45, 210, 45, 150, 25, 150, 55, 110, 85, 150, 65, 150, 65, 210)]
polygon4 = [(45, 0, 45, 55, 25, 55, 55, 105, 85, 55, 65, 55, 65, 0)]

VALUES = [(polygon1, "white", 100, 200, 380, 270),  # red
          (polygon2, "white", 100, 200, 100, 270),
          (polygon3, "white", 245, 100, 285, 60),  # blue
          (polygon4, "white", 245, 100, 285, 380)]

arrow_canvas = []
for b in range(4):
    canvas = tkinter.Canvas(frame, height=VALUES[b][2], width=VALUES[b][3],
                            highlightthickness=0, bd=0)
    canvas.configure(bg='black')
    canvas.create_polygon((VALUES[b][0]), fill=VALUES[b][1], outline="white",
                          width=1)
    canvas.place(x=VALUES[b][4], y=VALUES[b][5])
    arrow_canvas.append(canvas)

#  Arrow Canvas
VALUES = [(30, 60), (30, 380), (450, 380), (450, 60)]

for b in range(4):
    cmd = lambda x=b: FUNC[b][0]
    cmd = lambda x=b: FUNC[b][1]
    canvas = tkinter.Canvas(frame, bg="#383a39", height=200, width=200,
                            highlightthickness=0, bd=0)
    canvas.create_rectangle(195, 195, 5, 5, outline="white", width=4)
    canvas.place(x=VALUES[b][0], y=VALUES[b][1])

#  Motor Start/Stop Button
BUTTON = [(50, 205), (153, 205), (50, 525), (153, 525),
          (470, 205), (573, 205), (470, 525), (573, 525)]
FUNC = [("START", "white", "green", M1Start), ("STOP", "red", "gray", M1Stop),
        ("START", "white", "green", M2Start), ("STOP", "red", "gray", M2Stop),
        ("START", "white", "green", M3Start), ("STOP", "red", "gray", M3Stop),
        ("START", "white", "green", M4Start),
        ("STOP", "red", "gray", M4Stop), ]

motor_button = []
for b in range(8):
    cmd = lambda x=b: FUNC[b][2]
    m_button = tkinter.Button(frame, height=1, width=4, text=FUNC[b][0],
                              fg="black", bg=FUNC[b][1], command=FUNC[b][3],
                              highlightthickness=0,
                              activebackground=FUNC[b][2])
    m_button.place(x=BUTTON[b][0], y=BUTTON[b][1])
    motor_button.append(m_button)

#  Labels
LABELS = [("Motor 1", 15, "OliveDrab1", 90, 70),
          ("Motor 2", 15, "OliveDrab1", 90, 390),
          ("Motor 3", 15, "OliveDrab1", 510, 70),
          ("Motor 4", 15, "OliveDrab1", 510, 390),
          ("Motor Shield", 30, "White", 225, 5),
          ("Direction", 12, "SkyBlue1", 40, 95),
          ("Speed: in %", 12, "SkyBlue1", 50, 160),
          ("Direction", 12, "SkyBlue1", 40, 415),
          ("Speed: in %", 12, "SkyBlue1", 50, 480),
          ("Direction", 12, "SkyBlue1", 460, 95),
          ("Speed: in %", 12, "SkyBlue1", 470, 160),
          ("Direction", 12, "SkyBlue1", 460, 415),
          ("Speed: in %", 12, "SkyBlue1", 470, 480)]

for b in range(13):
    lbl = tkinter.Label(frame, text=LABELS[b][0], bg="#383a39",
                        font=('times', LABELS[b][1], 'bold'), fg=LABELS[b][2])
    lbl.place(x=LABELS[b][3], y=LABELS[b][4])

#  LED On/Off Buttons
BUTTONS = [(100, 270), (100, 330), (530, 270), (530, 330),
           (280, 110), (358, 110), (280, 500), (358, 500)]
FUNC = [("ON", "green2", "gray", A2_On), ("OFF", "red", "red", A2_Off),
        ("ON", "green2", "gray", A3_On), ("OFF", "red", "red", A3_Off),
        ("ON", "green2", "gray", A1_On), ("OFF", "red", "red", A1_Off),
        ("ON", "green2", "gray", A4_On), ("OFF", "red", "red", A4_Off), ]

button_led = []
for b in range(8):
    cmd = lambda x=b: FUNC[b][3]
    button_on_off = tkinter.Button(frame, height=1, width=3, text=FUNC[b][0],
                                   activebackground=FUNC[b][1], fg="white",
                                   bg=FUNC[b][2], bd=2, command=FUNC[b][3])
    button_on_off.place(x=BUTTONS[b][0], y=BUTTONS[b][1])
    button_led.append(button_on_off)

#  Motor Direction Radio Buttons
var1 = tkinter.IntVar()
var1.set(1)
tkinter.Radiobutton(frame, highlightthickness=0, text="Forward", variable=var1,
                    value=1).place(x=41, y=125)
tkinter.Radiobutton(frame, highlightthickness=0, text="Backward",
                    variable=var1, value=2).place(x=127, y=125)
w1 = tkinter.Spinbox(width=5, values=(100, 90, 80, 70, 60, 50, 40, 30, 20, 10))
w1.place(x=145, y=160)

var2 = tkinter.IntVar()
var2.set(1)
tkinter.Radiobutton(frame, highlightthickness=0, text="Forward", variable=var2,
                    value=1).place(x=41, y=445)
tkinter.Radiobutton(frame, highlightthickness=0, text="Backward",
                    variable=var2, value=2).place(x=127, y=445)
w2 = tkinter.Spinbox(width=5, values=(100, 90, 80, 70, 60, 50, 40, 30, 20, 10))
w2.place(x=145, y=480)

var3 = tkinter.IntVar()
var3.set(1)
tkinter.Radiobutton(frame, highlightthickness=0, text="Forward", variable=var3,
                    value=1).place(x=461, y=125)
tkinter.Radiobutton(frame, highlightthickness=0, text="Backward",
                    variable=var3, value=2).place(x=547, y=125)
w3 = tkinter.Spinbox(width=5, values=(100, 90, 80, 70, 60, 50, 40, 30, 20, 10))
w3.place(x=565, y=160)

var4 = tkinter.IntVar()
var4.set(1)
tkinter.Radiobutton(frame, highlightthickness=0, text="Forward", variable=var4,
                    value=1).place(x=461, y=445)
tkinter.Radiobutton(frame, highlightthickness=0, text="Backward",
                    variable=var4, value=2).place(x=547, y=445)
w4 = tkinter.Spinbox(width=5, values=(100, 90, 80, 70, 60, 50, 40, 30, 20, 10))
w4.place(x=565, y=480)
