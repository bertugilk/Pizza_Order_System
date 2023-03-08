from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pandas as pd

class payment:
    def __init__(self,total_cost,order_info):
        self.total_cost = total_cost
        self.order_info = order_info # örn: 2 adet klasik pizza 1 adet et sosu.
        self.name=0
        self.cardNum=0
        self.password=0
        self.identification_number=0
    def screen(self):
        # Gui:
        self.screen = Tk()
        self.screen.title("A.I. Pizza")
        self.canvas = Canvas(self.screen, width=1000, height=600, bg="black")
        self.canvas.place(relx=0.84, rely=0.35, anchor='ne')
        image = ImageTk.PhotoImage(Image.open("data/bg.jpg"))
        self.canvas.create_image(-700, 0, anchor=NW, image=image)
        self.canvas.pack()
        self.screen.resizable(False, False)

        self.canvas.create_text((500, 50), text=self.order_info, font="MSGothic 18 bold", fill="#00FF00")
        self.canvas.create_text((500, 90), text=f"Toplam Borcunuz = {self.total_cost} TL", font="MSGothic 18 bold",
                                fill="#FF0000")


        self.canvas.create_text((200, 250), text="Ad: ", font="MSGothic 18 bold", fill="#00FFFF")
        self.canvas.create_text((120, 300), text="Kimlik Numarası: ", font="MSGothic 18 bold", fill="#00FFFF")
        self.canvas.create_text((130, 350), text="Kart Numarası: ", font="MSGothic 18 bold", fill="#00FFFF")
        self.canvas.create_text((180, 400), text="Şifre: ", font="MSGothic 18 bold", fill="#00FFFF")

        name_var=StringVar()
        id_var = StringVar()
        card_var = StringVar()
        password_var = StringVar()

        def pay():
            print("Öde")
            name = name_var.get()
            id = id_var.get()
            cardNo = card_var.get()
            password = password_var.get()

            costDatas = []
            orderDatas  = []
            nameDatas = []
            idDatas = []
            cardNoDatas = []
            passwordDatas = []

            costDatas.append(self.total_cost)
            orderDatas.append(self.order_info)
            nameDatas.append(name)
            idDatas.append(id)
            cardNoDatas.append(cardNo)
            passwordDatas.append(password)

            dict = {'name':nameDatas,
                    'id':idDatas,
                    'cardNo':cardNoDatas,
                    'password':passwordDatas,
                    'total_cost':costDatas,
                    'order':orderDatas}

            df = pd.DataFrame(dict)
            print(df)
            df.to_csv('Data/Orders_Database.csv', mode='a', index=False, header=False)

            messagebox.showinfo("Order Message","Ödeme işleminiz başarıyla yapıldı afiyet olsun :)")

            name_var.set("")
            id_var.set("")
            card_var.set("")
            password_var.set("")

        pay_button = Button(text="Ödeme Yap", bg="dark green", activebackground="lightgreen", fg="white",
                       font=('Helvetica', 15, 'bold'), width=15, height=2, command=pay)
        pay_button.place(relx=0.2, rely=0.8, anchor='nw')

        name_entry = Entry(self.screen, textvariable=name_var, font=('calibre', 12, 'normal'))
        name_entry.place(relx=0.23, rely=0.4, anchor='nw')

        id_entry = Entry(self.screen, textvariable=id_var, font=('calibre', 12, 'normal'))
        id_entry.place(relx=0.23, rely=0.483, anchor='nw')

        card_entry = Entry(self.screen, textvariable=card_var, font=('calibre', 12, 'normal'))
        card_entry.place(relx=0.23, rely=0.57, anchor='nw')

        pass_entry = Entry(self.screen, textvariable=password_var, font=('calibre', 12, 'normal'))
        pass_entry.place(relx=0.23, rely=0.65, anchor='nw')

        self.screen.mainloop()