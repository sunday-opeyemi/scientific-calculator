from tkinter import *
from math import *
#from tkinter.messagebox import *
fval = sval= 0
text = showans = None
status =True
operate = screentext= ""
myval = ''
π = 3.141592
e = 2.718281
state = 'on'
bON = 'ON'

def press(num):
	global showans, screentext, status
	status = True
	txt = num
	myval = screentext.get()
	if myval == '0':
		showans.set(str(txt))
	elif screentext.get()=="":
		pass
	else:
		showans.set(0)
		showans.set(str(myval) + str(txt))	

def Onoff():
	global showans, state, bON
	bON = StringVar()
	ON = Button(root, textvariable = bON, fg = 'black', bg = 'red',command = lambda: Onoff(), height = 1, width = 7)
	ON.grid(row = 8, column = 0)
	if state == 'on':
		showans.set(0)
		bON.set('OFF')
		state ='off'
	else:
		showans.set('')
		bON.set('ON')
		state='on'

def calculate(cal):
	global showans, operate, fval
	operate = cal
	fval = screentext.get()
	status = True
	if screentext.get()=="":
		pass
	else:
		showans.set(0)

def clear():
	global showans, status
	if screentext.get()=="":
		pass
	else:
		showans.set(0)
		status = True
		
def check_operator():
	global operate, fval, sval, showans, status
	if status:
		sval= screentext.get()
		status =False
	else:
		fval = screentext.get()

def equal2():
	global operate, fval, sval, showans, status
	check_operator()
	if screentext.get()=="":
		pass
	else:
		try:
			if operate == '+':
				answer = float(fval) + float(sval)
				showans.set(answer)
			elif operate == '-':
				answer = float(fval) - float(sval)
				showans.set(answer)
			elif operate == '*':
				answer = float(fval) * float(sval)
				showans.set(answer)
			elif operate == '/':
				answer = float(fval) / float(sval)
				showans.set(answer)
			elif operate == 'x^y':
				answer = float(fval) ** float(sval)
				showans.set(answer)
		except:
			showans.set('Error')

		
def trig(trigfun):
	if screentext.get()=="":
		pass
	else:
		try:
			if trigfun == 'ln':
				fval = screentext.get()
				showans.set(1/log10(float(fval)))
			elif trigfun == 'log':
				fval = screentext.get()
				answer = log10(float(fval))
				showans.set(answer)

			elif trigfun == 'sin':
				fval = screentext.get()
				answer = sin(float(fval))
				showans.set(answer)
			elif trigfun == 'cos':
				fval = screentext.get()
				answer = cos(float(fval))
				showans.set(answer)
			elif trigfun == 'tan':
				fval = screentext.get()
				answer = tan(float(fval))
				showans.set(answer)
			elif trigfun == '!':
				fval = screentext.get()
				answer = factorial(float(fval))
				showans.set(answer)
			elif trigfun == 'x^2':
				fval = screentext.get()
				answer = float(fval) ** 2
				showans.set(answer)
			elif trigfun == 'π':
				fval = screentext.get()
				π = 3.141592
				answer = π
				showans.set(answer)
		except:
			#showinfo("Error Message", "wrong operation performed")
			showans.set('Error')
	
def plusminus():
	fval = screentext.get()
	answer = '-' + fval 
	if screentext.get()=="":
		pass
	else:
		showans.set(0)
		showans.set(answer)
    
def screen():
	global showans, screentext
	showans = StringVar()
	screentext = Entry(root, width=35, textvariable = showans)
	screentext.grid(columnspan = 4)

def gui():
	global root, screen, clear, bON
	root = Tk()
	root.title("Simple Calculator")
	screen()
	Onoff()
	
	b1 = Button(root, text = '1', fg = 'black', bg = 'red', command = lambda: press(1), height = 1, width = 7)
	b1.grid(row = 2, column = 0)
	b2 = Button(root, text = '2', fg = 'black', bg = 'red', command = lambda: press(2), height = 1, width = 7)
	b2.grid(row = 2, column = 1)
	b3 = Button(root, text = '3', fg = 'black', bg = 'red',command = lambda: press(3), height = 1, width = 7)
	b3.grid(row = 2, column = 2)
	b4 = Button(root, text = '4', fg = 'black', bg = 'red',command = lambda: press(4), height = 1, width = 7)
	b4.grid(row = 3, column = 0)
	b5 = Button(root, text = '5', fg = 'black', bg = 'red',command = lambda: press(5), height = 1, width = 7)
	b5.grid(row = 3, column = 1)
	b6 = Button(root, text = '6', fg = 'black', bg = 'red',command = lambda: press(6), height = 1, width = 7)
	b6.grid(row = 3, column = 2)
	b7 = Button(root, text = '7', fg = 'black', bg = 'red',command = lambda: press(7), height = 1, width = 7)
	b7.grid(row = 4, column = 0)
	b8 = Button(root, text = '8', fg = 'black', bg = 'red',command = lambda: press(8), height = 1, width = 7)
	b8.grid(row = 4, column = 1)
	b9 = Button(root, text = '9', fg = 'black', bg = 'red',command = lambda: press(9), height = 1, width = 7)
	b9.grid(row = 4, column = 2)
	b0 = Button(root, text = '0', fg = 'black', bg = 'red',command = lambda: press(0), height = 1, width = 7)
	b0.grid(row = 5, column = 0)
	plus = Button(root, text = '+', fg = 'black', bg = 'red',command = lambda: calculate('+'), height = 1, width = 7)
	plus.grid(row = 2, column= 3)
	minus = Button(root, text = '-', fg = 'black', bg = 'red',command = lambda: calculate('-'), height = 1, width = 7)
	minus.grid(row = 3, column= 3)
	multiply = Button(root, text = 'X', fg = 'black', bg = 'red',command = lambda: calculate('*'), height = 1, width = 7)
	multiply.grid(row = 4, column= 3)
	divide = Button(root, text = '/', fg = 'black', bg = 'red',command = lambda: calculate('/'), height = 1, width = 7)
	divide.grid(row = 5, column= 3)
	power = Button(root, text = "x^y", fg = 'black', bg = 'red',command = lambda: calculate("x^y"), height = 1, width = 7)
	power.grid(row = 7, column= 0)
	fact = Button(root, text = "x!", fg = 'black', bg = 'red',command = lambda: trig("!"), height = 1, width = 7)
	fact.grid(row = 8, column= 2)
	loge = Button(root, text = "ln", fg = 'black', bg = 'red',command = lambda: trig("ln"), height = 1, width = 7)
	loge.grid(row = 7, column= 1)
	log10 = Button(root, text = "log", fg = 'black', bg = 'red',command = lambda: trig("log"), height = 1, width = 7)
	log10.grid(row = 8, column= 1)
	sine = Button(root, text = "sin", fg = 'black', bg = 'red',command = lambda: trig("sin"), height = 1, width = 7)
	sine.grid(row = 6, column= 0)
	cosine = Button(root, text = "cos", fg = 'black', bg = 'red',command = lambda: trig("cos"), height = 1, width = 7)
	cosine.grid(row = 6, column= 1)
	tangent = Button(root, text = "tan", fg = 'black', bg = 'red',command = lambda: trig("tan"), height = 1, width = 7)
	tangent.grid(row = 6, column= 2)
	point = Button(root, text = ".", fg = 'black', bg = 'red',command = lambda: press("."), height = 1, width = 7)
	point.grid(row = 7, column= 2)
	neg = Button(root, text = "+/-", fg = 'black', bg = 'red',command = lambda: plusminus(), height = 1, width = 7)
	neg.grid(row = 7, column= 3)
	pie = Button(root, text = "π", fg = 'black', bg = 'red',command = lambda: trig("π"), height = 1, width = 7)
	pie.grid(row = 8, column = 3)
	pow2 = Button(root, text = "x^2", fg = 'black', bg = 'red',command = lambda: trig("x^2"), height = 1, width = 7)
	pow2.grid(row = 6, column= 3)
		
	equalto = Button(root, text = '=', fg = 'black', bg = 'red',command = equal2, height = 1, width = 7)
	equalto.grid(row = 5, column= 2)
	clear = Button(root, text = 'Clear', fg = 'black', bg = 'red',command = clear, height = 1, width = 7)
	clear.grid(row = 5, column= 1)
	
	root.mainloop()

gui()

