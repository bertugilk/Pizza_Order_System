from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import datetime
import main
import time
import payment_screen

now = datetime.datetime.now()
date = datetime.datetime.strftime(now, '%c')

#Classes:
classic=main.Classic_Pizza()
margherita=main.Margherita()
Turk=main.Turk_Pizzasi()
olive=main.Olive()
meat=main.Meat()
onion=main.Onion()

#Gui:
screen = Tk()
var=IntVar()
screen.title("A.I. Pizza")
canvas = Canvas(screen, width=1000, height=600,bg="black")
canvas.place(relx=0.84, rely=0.35, anchor='ne')
image = ImageTk.PhotoImage(Image.open("data/bg.jpg"))
canvas.create_image(-700, 0, anchor=NW, image=image)
canvas.pack()
screen.resizable(False, False)

total_cost = 0
minus_value = 0

canvas.create_text((380, 100), text="A.I. Pizza", font="MSGothic 40 bold", fill="#00BFFF")
canvas.create_text((140, 200), text="Pizza Çesitleri", font="MSGothic 25 bold", fill="#FF1493")
canvas.create_text((470, 200), text="Sos Çesitleri", font="MSGothic 25 bold", fill="#FF1493")
canvas.create_text((110, 20), text=str(date), font="MSGothic 12 bold", fill="#FFFFFF")

#Pizzas:
canvas.create_text((90, 270), text="Klasik Pizza\n(80 TL)", font="MSGothic 18 bold", fill="#00FFFF")
canvas.create_text((84, 340), text="Margherita\n(100 TL)", font="MSGothic 18 bold", fill="#00FFFF")
canvas.create_text((82, 410), text="Türk Pizza\n(150 TL)", font="MSGothic 18 bold", fill="#00FFFF")

classicNum=classic.piece
margheritaNum=margherita.piece
TurkNum=Turk.piece

classicLabel = Label(bg='#000000', fg="#00FFFF", font=('Showcard Gothic', 17, 'bold'))
classicLabel.place(relx=0.32, rely=0.42, anchor='ne')
classicLabel['text'] = ("{0}".format(classicNum))

margheritaLabel = Label(bg='#000000', fg="#00FFFF", font=('Showcard Gothic', 17, 'bold'))
margheritaLabel.place(relx=0.32, rely=0.54, anchor='ne')
margheritaLabel['text'] = ("{0}".format(margheritaNum))

TurkLabel = Label(bg='#000000', fg="#00FFFF", font=('Showcard Gothic', 17, 'bold'))
TurkLabel.place(relx=0.32, rely=0.64, anchor='ne')
TurkLabel['text'] = ("{0}".format(TurkNum))

# Sauces:
canvas.create_text((400, 270), text="Olive\n(10 TL)", font="MSGothic 18 bold", fill="#00FFFF")
canvas.create_text((400, 340), text="Meat\n(30 TL)", font="MSGothic 18 bold", fill="#00FFFF")
canvas.create_text((405, 410), text="Onion\n(20 TL)", font="MSGothic 18 bold", fill="#00FFFF")

oliveNum=olive.piece
meatNum=meat.piece
onionNum=onion.piece

oliveLabel = Label(bg='#000000', fg="#00FFFF", font=('Showcard Gothic', 17, 'bold'))
oliveLabel.place(relx=0.59, rely=0.42, anchor='ne')
oliveLabel['text'] = ("{0}".format(oliveNum))

meatLabel = Label(bg='#000000', fg="#00FFFF", font=('Showcard Gothic', 17, 'bold'))
meatLabel.place(relx=0.59, rely=0.54, anchor='ne')
meatLabel['text'] = ("{0}".format(meatNum))

onionLabel = Label(bg='#000000', fg="#00FFFF", font=('Showcard Gothic', 17, 'bold'))
onionLabel.place(relx=0.59, rely=0.64, anchor='ne')
onionLabel['text'] = ("{0}".format(onionNum))

#Total cost:
totalLabel = Label(bg='#000000', fg="#BA55D3", font=('Showcard Gothic', 17, 'bold'))
totalLabel.place(relx=0.97, rely=0.03, anchor='ne')
totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

def classicPlus():
    global classicNum, total_cost
    classicNum += 1
    total_cost += 80
    classicLabel['text'] = ("{0}".format(classicNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

def MargheritaPlus():
    global margheritaNum,total_cost
    margheritaNum += 1
    total_cost += 100
    margheritaLabel['text'] = ("{0}".format(margheritaNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))
def TurkPlus():
    global TurkNum,total_cost
    TurkNum += 1
    total_cost += 150
    TurkLabel['text'] = ("{0}".format(TurkNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

plus_classic = Button(text="+", bg="dark green",activebackground="lightgreen" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=classicPlus)
plus_classic.place(relx=0.2, rely=0.42, anchor='nw')

plus_Margherita = Button(text="+", bg="dark green",activebackground="lightgreen" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=MargheritaPlus)
plus_Margherita.place(relx=0.2, rely=0.54, anchor='nw')

plus_Turk = Button(text="+", bg="dark green",activebackground="lightgreen" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=TurkPlus)
plus_Turk.place(relx=0.2, rely=0.64, anchor='nw')

def classicMinus():
    global classicNum,total_cost,minus_value
    classicNum -= 1
    minus_value = 80
    if classicNum < 0:
        minus_value = 0
    if classicNum < 0:
        classicNum = 0
    total_cost -= minus_value
    classicLabel['text'] = ("{0}".format(classicNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

def MargheritaMinus():
    global margheritaNum,total_cost,minus_value
    margheritaNum -= 1
    minus_value = 100
    if margheritaNum < 0:
        minus_value = 0
    if margheritaNum < 0:
        margheritaNum = 0
    total_cost -= minus_value
    margheritaLabel['text'] = ("{0}".format(margheritaNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

def TurkMinus():
    global TurkNum,total_cost,minus_value
    TurkNum -= 1
    minus_value = 150
    if TurkNum < 0:
        minus_value = 0
    if TurkNum < 0:
        TurkNum = 0
    total_cost -= minus_value
    TurkLabel['text'] = ("{0}".format(TurkNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

minus_classic = Button(text="-", bg="dark red",activebackground="salmon" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=classicMinus)
minus_classic.place(relx=0.25, rely=0.42, anchor='nw')

minus_Margherita = Button(text="-", bg="dark red",activebackground="salmon" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=MargheritaMinus)
minus_Margherita.place(relx=0.25, rely=0.54, anchor='nw')

minus_Turk = Button(text="-", bg="dark red",activebackground="salmon" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=TurkMinus)
minus_Turk.place(relx=0.25, rely=0.64, anchor='nw')

def olivePlus():
    global oliveNum,total_cost
    oliveNum += 1
    total_cost += 10
    oliveLabel['text'] = ("{0}".format(oliveNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

def meatPlus():
    global meatNum,total_cost
    meatNum += 1
    total_cost += 30
    meatLabel['text'] = ("{0}".format(meatNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

def onionPlus():
    global onionNum,total_cost
    onionNum += 1
    total_cost += 20
    onionLabel['text'] = ("{0}".format(onionNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

plus_olive = Button(text="+", bg="dark green",activebackground="lightgreen" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=olivePlus)
plus_olive.place(relx=0.47, rely=0.42, anchor='nw')

plus_Meat = Button(text="+", bg="dark green",activebackground="lightgreen" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=meatPlus)
plus_Meat.place(relx=0.47, rely=0.54, anchor='nw')

plus_Onion = Button(text="+", bg="dark green",activebackground="lightgreen" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=onionPlus)
plus_Onion.place(relx=0.47, rely=0.64, anchor='nw')

def oliveMinus():
    global oliveNum,total_cost,minus_value
    oliveNum -= 1
    minus_value = 10
    if oliveNum < 0:
        minus_value = 0
    if oliveNum < 0:
        oliveNum = 0
    total_cost -= minus_value
    oliveLabel['text'] = ("{0}".format(oliveNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

def meatMinus():
    global meatNum,total_cost,minus_value
    meatNum -= 1
    minus_value = 30
    if meatNum < 0:
        minus_value = 0
    if meatNum < 0:
        meatNum = 0
    total_cost -= minus_value
    meatLabel['text'] = ("{0}".format(meatNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

def onionMinus():
    global onionNum,total_cost,minus_value
    onionNum -= 1
    minus_value = 20
    if onionNum < 0:
        minus_value = 0
    if onionNum < 0:
        onionNum = 0
    total_cost -= minus_value
    onionLabel['text'] = ("{0}".format(onionNum))
    totalLabel['text'] = ("Toplam Borcunuz = {0} TL".format(total_cost))

Minus_olive = Button(text="-", bg="dark red",activebackground="salmon" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=oliveMinus)
Minus_olive.place(relx=0.52, rely=0.42, anchor='nw')

Minus_Meat = Button(text="-", bg="dark red",activebackground="salmon" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=meatMinus)
Minus_Meat.place(relx=0.52, rely=0.54, anchor='nw')

Minus_Onion = Button(text="-", bg="dark red",activebackground="salmon" ,fg="white",
                      font=('Showcard Gothic', 13, 'bold'),width=2, height=1, command=onionMinus)
Minus_Onion.place(relx=0.52, rely=0.64, anchor='nw')

def order():
    if classicNum >=1 or margheritaNum >=1 or TurkNum >=1:
        messagebox.showinfo("Sipariş Notu", "Siparişiniz Hazırlanıyor...")
        time.sleep(2)
        screen.destroy()
        total_pizza = classicNum + margheritaNum + TurkNum
        total_sauce = oliveNum + meatNum + onionNum

        order_info = f"Toplam {total_pizza} adet pizza ve {total_sauce} adet sos siparişi verilmiştir."
        pay = payment_screen.payment(total_cost, order_info)
        pay.screen()

order = Button(text="Sipariş Ver", bg="dark green",activebackground="lightgreen" ,fg="white",
               font=('Helvetica', 13, 'bold'),width=15, height=2,command=order)
order.place(relx=0.2, rely=0.8, anchor='nw')

def classic_info():
    messagebox.showinfo("Klasik bilgi",classic.description)
Classicinfo_btn = Button(text="Bilgi",width=4, height=1,bg="white",font=('Helvetica', 11, 'bold'),command=classic_info)
Classicinfo_btn.place(relx=0.13, rely=0.45, anchor='nw')

def marg_info():
    messagebox.showinfo("Marg bilgi",margherita.description)
Classicinfo_btn = Button(text="Bilgi",width=4, height=1,bg="white",font=('Helvetica', 11, 'bold'),command=marg_info)
Classicinfo_btn.place(relx=0.13, rely=0.57, anchor='nw')

def Tr_info():
    messagebox.showinfo("Türk bilgi",Turk.description)
Classicinfo_btn = Button(text="Bilgi",width=4, height=1,bg="white",font=('Helvetica', 11, 'bold'),command=Tr_info)
Classicinfo_btn.place(relx=0.13, rely=0.68, anchor='nw')

if __name__ == '__main__':
    while True:
        screen.mainloop()
