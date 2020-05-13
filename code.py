#AKINATOR CWC'11

#import sys

from tkinter import *
from tkinter.ttk import *
#import Image

	
def open_window_2():
	window_2 = Toplevel()
	window_2.title("CwcGinie")
	window_2.geometry('3000x3000')
	
	
	def raina():
		lblinstruct = Label(window_2, text="Your character is Suresh Raina")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=10)
			
			
	def yuvi():
		lblinstruct = Label(window_2, text="Your character is Yuvraj Singh")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=10)
			
	
	def cancer():
		lblinstruct = Label(window_2, text="Has your character survived Cancer ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=7)
		btn28 = Button(window_2, text="Yes", command=yuvi)
		btn29 = Button(window_2, text="No", command=raina)
		btn28.grid(column=0, row=8)
		btn29.grid(column=1, row=8)
	
	
	
	def bhajji():
		lblinstruct = Label(window_2, text="Your character is Harbhajan Singh")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=12)
			
			
	def ashwin():
		lblinstruct = Label(window_2, text="Your character is Ravichandran Ashwin")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=12)
	
	
	def ashbhajji():
		lblinstruct = Label(window_2, text="Is your character a South Indian or does he wear a Pagri")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=9)
		btn25 = Button(window_2, text="Wears a Pagri", command=bhajji)
		btn26 = Button(window_2, text="From South India", command=ashwin)
		btn25.grid(column=0, row=10)
		btn26.grid(column=1, row=10)
	
	def yusuf():
		lblinstruct = Label(window_2, text="Your character is Yusuf Pathan")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=10)
	
	def brother():
		lblinstruct = Label(window_2, text="Does your character have a ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=7)
		btn23 = Button(window_2, text="Famous Brother", command=yusuf)
		btn24 = Button(window_2, text="or Not", command=ashbhajji)
		btn23.grid(column=0, row=8)
		btn24.grid(column=1, row=8)
	
	
	def rightleft3():
		lblinstruct = Label(window_2, text="Is your character ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=5)
		btn22 = Button(window_2, text="Right Handed", command=brother)
		btn27 = Button(window_2, text="Left Handed", command=cancer)
		btn22.grid(column=0, row=6)
		btn27.grid(column=1, row=6)
	
	
	def nehra():
		lblinstruct = Label(window_2, text="Your character is Ashish Nehra")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=10)
	
	def zaheer():
		lblinstruct = Label(window_2, text="Your character is Zaheer Khan")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=10)
	
	def rcb():
		lblinstruct = Label(window_2, text="Has our charcter been ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=7)
		btn16 = Button(window_2, text="RCB bowling Coach", command=nehra)
		btn17 = Button(window_2, text="or Not", command=zaheer)
		btn16.grid(column=0, row=8)
		btn17.grid(column=1, row=8)
	
	
	def sreesanth():
		lblinstruct = Label(window_2, text="Your character is S. Sreesanth")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=11)
	
	def munaf():
		lblinstruct = Label(window_2, text="Your character is Munaf Patel")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=11)
	
	
	def controversies():
	
		lblinstruct = Label(window_2, text="Was your character involved in controversies ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=9)
	
		btn16 = Button(window_2, text="Yes", command=sreesanth)
		btn17 = Button(window_2, text="No", command=munaf)
		btn16.grid(column=0, row=10)
		btn17.grid(column=1, row=10)
	
	
	def piyush():
		lblinstruct = Label(window_2, text="Your character is Piyush Chawla")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=10)
	
	
	def spinfast():
		lblinstruct = Label(window_2, text="What kind of bowler is your character ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=7)
		btn14 = Button(window_2, text="Spin", command=piyush)
		btn15 = Button(window_2, text="Fast", command=controversies)
		btn14.grid(column=0, row=8)
		btn15.grid(column=1, row=8)
	
	
	def rightleft2():
	
		lblinstruct = Label(window_2, text="Is your character a : ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=5)
		btn13 = Button(window_2, text="Right Arm", command=spinfast)
		btn18 = Button(window_2, text="Left Arm", command=rcb)
		btn13.grid(column=0, row=6)
		btn18.grid(column=1, row=6)
		#rightleft.mainloop()
	
	def dhoni():
		lblinstruct = Label(window_2, text="Your character is Mahendra Singh Dhoni")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=10)
	
	def kohli():
		lblinstruct = Label(window_2, text="Your character is Virat Kohli")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=10)
	
	
	def wicketkeeper():
		lblinstruct = Label(window_2, text="Is your character a : ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=7)
		btn7=Button(window_2, text="Wicketkeeper", command=dhoni)
		btn8=Button(window_2, text=" or Not", command=kohli)
		btn7.grid(column=0, row=9)
		btn8.grid(column=1, row=9)
	
	def sehwag():
		lblinstruct = Label(window_2, text="Your character is Virender Sehwag")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=11)
	
	def sachin():
		lblinstruct = Label(window_2, text=" Your character is Sachin Tendulkar")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=11)
	
	def god():
		lblinstruct = Label(window_2, text="Is your character : ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=9)
		btn7=Button(window_2, text="Nicknamed God", command=sachin)
		btn8=Button(window_2, text="No", command=sehwag)
		btn7.grid(column=0, row=10)
		btn8.grid(column=1, row=10)
		
	def gambhir():
		lblinstruct = Label(window_2, text="Your character is Gautam Gambhir")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=9)
	
	
	
	def rightleft():
	
		lblinstruct = Label(window_2, text="Is your character : ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=7)
		btn5 = Button(window_2, text="Right Handed", command=god)
		btn6 = Button(window_2, text="Left Handed", command=gambhir)
		btn5.grid(column=0, row=8)
		btn6.grid(column=1, row=8)
		#rightleft.mainloop()
	

	def purebatsman():
		lblinstruct = Label(window_2, text="Is your character a : ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=5)
		btn4 = Button(window_2, text="Opener", command=rightleft)
		btn9 = Button(window_2, text="Not an Opener", command=wicketkeeper)
		btn4.grid(column=0, row=6)
		btn9.grid(column=1, row=6)
		#purebatsman.mainloop()
		
	def go():
	
		lblinstruct = Label(window_2, text="Is your character a : ")
		lblinstruct.config(font=("Courier", 15))
		lblinstruct.grid(column=0, row=1)
	
		btn3 = Button(window_2, text="Pure Batsman", command=purebatsman)
		btn3.grid(column=0, row=2)
		btn12=Button(window_2, text="Pure Bowler", command=rightleft2)
		btn12.grid(column=0, row=3)
		btn21=Button(window_2, text="All Rounder",  command=rightleft3)
		btn21.grid(column=0, row=4)
		
	
		
	
	#cwcimage = PhotoImage(file="page2.png")
	#lab6=Label(image = cwcimage)
	#lab6.grid()
	lblinstruct = Label(window_2, text="Answer the following Questions that the Ginie will ask you.")
	lblinstruct.config(font=("Courier", 20))
	lblinstruct.grid(column=0, row=0)
	
	btn3 = Button(window_2, text="GO", command=go)
	btn3.grid(column=1, row=0)
	window_2.mainloop()	
	

	
	
	'''btn4=Button(window_2, text="Opener")
	
	btn5=Button(window_2, text="Right Handed")
	btn6=Button(window_2, text="Left Handed")
	btn7=Button(window_2, text="Nicknamed God")
	btn8=Button(window_2, text="No")
	btn9=Button(window_2, text="Not an Opener")
	btn10=Button(window_2, text="Wicketkeeper")
	tn11=Button(window_2, text="No")
	btn12=Button(window_2, text="Pure Bowler")
	btn13=Button(window_2, text="Right Arm")
	btn14=Button(window_2, text="Spin")
	tn15=Button(window_2, text="Fast")
	btn16=Button(window_2, text="Has had controvies")
	btn17=Button(window_2, text="Not")
	btn18=Button(window_2, text="Left Arm")
	btn19=Button(window_2, text="Delhite")
	btn20=Button(window_2, text="Not")
	btn21=Button(window_2, text="All Rounder")
	btn22=Button(window_2, text="Right Hand ")
	btn23=Button(window_2, text="Brother also in Indian Cricket")
	btn24=Button(window_2, text="Not")
	btn25=Button(window_2, text="South Indian")
	btn27=Button(window_2, text="Not")
	btn28=Button(window_2, text="Cancer Survivor")
	btn29=Button(window_2, text="Not")
	
	

1.MS Dhoni - wicketkeeper and captain
2.Virender Sehwag - batsman
3.Ravichandran Ashwin - All - Rounder
4.Piyush Chawla - All - Rounder
5.Gautam Gambhir - batsman
6.Harbhajan Singh - off spinner
7.Zaheer Khan - fast bowler
8.Virat Kohli - batsman
9.sreesanth - fast bowler
10.Ashish Nehra - seamer
11.Munaf Patel - seamer
12.Yusuf Pathan - allrounder
13.Suresh Raina - batsman
14.Sachin Tendulkar - batsman
15.Yuvraj Singh - batsman'''



	

		



def open_window_1():
	window_1 = Toplevel()
	window_1.title("CwcGinie")
	window_1.geometry('3000x3000')
	
	'''img1 = PhotoImage(file="page2.png")
	lab1=Label(image = img1)
	lab1.grid(column=0, row=1)'''
	
	def squad():

		lbl0 = Label(window_1, text="Squad:")
		lbl0.config(font=("Courier", 15))		
		lbl0.grid(column=1, row=3)
		
		lbl1 = Label(window_1, text="1.MS Dhoni - Wicketkeeper and Captain")
		lbl1.config(font=("Courier", 15))		
		lbl1.grid(column=1, row=4)
		
		lbl2 = Label(window_1, text="2.Virender Sehwag - Batsman")
		lbl2.config(font=("Courier", 15))
		lbl2.grid(column=1, row=5)
		
		lbl3 = Label(window_1, text="3.Ravichandran Ashwin - All - Rounder")
		lbl3.config(font=("Courier", 15))
		lbl3.grid(column=1, row=6)
		
		lbl4 = Label(window_1, text="4.Piyush Chawla - Leg Spinner")
		lbl4.config(font=("Courier", 15))
		lbl4.grid(column=1, row=7)
		
		lbl5 = Label(window_1, text="5.Gautam Gambhir - Batsman")
		lbl5.config(font=("Courier", 15))
		lbl5.grid(column=1, row=8)
		
		lbl6 = Label(window_1, text="6.Harbhajan Singh - All - Rounder")
		lbl6.config(font=("Courier", 15))
		lbl6.grid(column=1, row=9)
			
		lbl7 = Label(window_1, text="7.Zaheer Khan - Fast Bowler")
		lbl7.config(font=("Courier", 15))
		lbl7.grid(column=1, row=10)
			
		lbl8 = Label(window_1, text="8.Virat Kohli - Batsman")
		lbl8.config(font=("Courier", 15))
		lbl8.grid(column=1, row=11)
			
		lbl9 = Label(window_1, text="9.Sreesanth - Fast Bowler")
		lbl9.config(font=("Courier", 15))
		lbl9.grid(column=1, row=12)
			
		lbl10 = Label(window_1, text="10.Ashish Nehra - Seamer")
		lbl10.config(font=("Courier", 15))
		lbl10.grid(column=1, row=13)
			
		lbl11 = Label(window_1, text="11.Munaf Patel - Seamer")
		lbl11.config(font=("Courier", 15))
		lbl11.grid(column=1, row=14)
			
		lbl12 = Label(window_1, text="12.Yusuf Pathan - All - Rounder")
		lbl12.config(font=("Courier", 15))
		lbl12.grid(column=1, row=15)
			
		lbl13 = Label(window_1, text="13.Suresh Raina - All - Rounder")
		lbl13.config(font=("Courier", 15))
		lbl13.grid(column=1, row=16)
			
		lbl14 = Label(window_1, text="14.Sachin Tendulkar - Batsman")
		lbl14.config(font=("Courier", 15))
		lbl14.grid(column=1, row=17)
			
		lbl15 = Label(window_1, text="15.Yuvraj Singh - All - Rounder")
		lbl15.config(font=("Courier", 15))
		lbl15.grid(column=1, row=18)
		
		btn12=Button(window_1, text="START", command=open_window_2)
		btn12.grid(column=1, row=19)
		
	
	lbl2 = Label(window_1, text="Sit back...Relax...We'll take you back to CWC 2011 ")
	lbl2.config(font=("Courier", 20))
	lbl2.grid(column=0, row=1)
	
	btnok = Button(window_1, text="OK", command=open_window_2)
	btnok.grid(column=0, row=2)
	btnsq=Button(window_1, text="Show the Squad", command=squad)
	btnsq.grid(column=1, row=2)
	


		
	window_1.mainloop()




def open_window():
	top = Tk()
	top.title("CwcGinie1")
	

	#canvas = Canvas(top, width=300, height=200)
	#canvas.pack()
	#photo_2 = PhotoImage(file = "page2.png", master = window)
	#canvas.create_image(0, 0, anchor=NW, image=photo_2)
	
	top.geometry('1200x1200')
	'''img1 = PhotoImage(file="window2.png")
	lab1=Label(image = img1)
	lab1.grid(column=0, row=6)'''

	
	
	lbl2 = Label(top, text="Hey the followers of the cricket religion,here is a game for you.")
	
	
	
	lbl3 = Label(top, text="Think about a player from the 15 membered 2011 Indian cricket World cup squad.")
	lbl4 = Label(top, text="We ask you a set of questions,you answer it and then we tell you who it is.")
	lbl5 = Label(top, text="Isn't it Fun ? Yeah ? Let's start")
	lbl2.config(font=("Courier", 20))
	lbl3.config(font=("Courier", 20))
	lbl4.config(font=("Courier", 20))
	lbl5.config(font=("Courier", 20))
	lbl2.grid(column=0, row=1)
	lbl3.grid(column=0, row=2)
	lbl4.grid(column=0, row=3)
	lbl5.grid(column=0, row=4)
	


	
	btntwo = Button(top, text="START", command=open_window_1)

	btntwo.grid(column=0, row=10)
	
	
	top.mainloop()

window = Tk()
window.title("MyGinie")

lbl = Label(window, text="Let the Ginie guess the Cricketer in your Mind!?!")
lbl.config(font=("Courier", 30))
lbl.grid(column=0, row=0)


window.geometry('1200x1200')


img = PhotoImage(file="ginie.png")
lab=Label(image = img)
lab.grid(column=0, row=1)



#button=Button(window, text="", command=open_window)
#button.grid(column=1, row=6)

btn = Button(window, text="PLAY", command=open_window)

btn.grid(column=10, row=0)


window.mainloop()








