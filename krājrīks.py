from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("800x600")
window.title("Krājrīks")
window.configure(background = 'white')

#mainīgie
konta_nauda = 250
uzkrātie_procenti = float(0.00)
procentu_likme = 2
galvenais_konts = 3000
papildinājuma_summa_skaitlis = 0
izņēmuma_summa_skaitlis = 0

#dažas funkcijas
def plus_viens_papild():
    global papildinājuma_summa_skaitlis
    global galvenais_konts
    papildinājuma_summa_skaitlis += 1
    papildinājuma_summa.config(text=str(papildinājuma_summa_skaitlis))
    galvenais_konts -= 1
    teksts_atlikums.config(text=str(galvenais_konts))

def mīnus_viens_papild():
    global papildinājuma_summa_skaitlis
    global galvenais_konts
    papildinājuma_summa_skaitlis -= 1
    papildinājuma_summa.config(text=str(papildinājuma_summa_skaitlis))
    galvenais_konts += 1
    teksts_atlikums.config(text=str(galvenais_konts))

def add_amount(value):
    global papildinājuma_summa_skaitlis
    global galvenais_konts
    papildinājuma_summa_skaitlis += value
    galvenais_konts -= value
    update_display()

def reset_amount():
    global papildinājuma_summa_skaitlis
    global galvenais_konts
    papildinājuma_summa_skaitlis += galvenais_konts
    galvenais_konts = 0
    update_display()

def nosūtīt():
    global konta_nauda
    global galvenais_konts
    konta_nauda += papildinājuma_summa_skaitlis
    update_display()

def update_display():
    papildinājuma_summa.config(text=f"{papildinājuma_summa_skaitlis}")
    teksts_atlikums.config(text=f"{galvenais_konts}")
    konta_summa.config(text=f"{konta_nauda} EUR")

def plus_viens():
    global izņēmuma_summa_skaitlis
    global galvenais_konts
    izņēmuma_summa_skaitlis += 1
    izņēmuma_summa.config(text=str(izņēmuma_summa_skaitlis))
    galvenais_konts -= 1

def mīnus_viens():
    global izņēmuma_summa_skaitlis
    global galvenais_konts
    izņēmuma_summa_skaitlis -= 1
    izņēmuma_summa.config(text=str(izņēmuma_summa_skaitlis))
    galvenais_konts += 1

def pievienot_vērtību(value):
    global izņēmuma_summa_skaitlis
    global galvenais_konts
    izņēmuma_summa_skaitlis += value
    galvenais_konts -= value
    update_display_2()

def noņemt_vertību():
    global izņēmuma_summa_skaitlis
    global galvenais_konts
    izņēmuma_summa_skaitlis += galvenais_konts
    galvenais_konts = 0
    update_display_2()

def izņemt_funkcija():
    global konta_nauda
    global izņēmuma_summa_skaitlis
    konta_nauda -= izņēmuma_summa_skaitlis
    update_display_2()

def update_display_2():
     izņēmuma_summa.config(text=f"{izņēmuma_summa_skaitlis}")
     konta_summa.config(text=f"{konta_nauda}")

#teksts ar konta naudas summu
konta_summa = Label( window, text = f"{konta_nauda} EUR", font = ('Inter 20'), background = 'white' )
konta_summa.place(x = 350, y = 50)

#papildināt logs
def papildināt_logs():
    global papildinājuma_summa
    global teksts_atlikums
    logs_papildināt = Toplevel()
    logs_papildināt.title("Papildināt")
    logs_papildināt.geometry('500x500')
    logs_papildināt.configure(background = 'white')

    papildināt_logs_teksts_1 = Label(logs_papildināt, text = 'Papildināt', font = 'Inter 24', bg = 'white', fg = 'darkorange')
    papildināt_logs_teksts_1.place(x = 30, y = 20)

    konta_numurs = Label(logs_papildināt, text = 'Mans konts', font = 'Inter 14', bg = 'white')
    konta_numurs.place(x = 40, y = 80)

    no_konta = Label(logs_papildināt, text = 'No konta', font = 'Inter 8', bg = 'white', fg = '#ABABAB')
    no_konta.place(x = 35, y = 60)

    papildinājuma_summa = Label(logs_papildināt, text=str(papildinājuma_summa_skaitlis), font='Inter 32', bg='white')
    papildinājuma_summa.place(x=200, y=180)

    poga_plus_1 = Button(logs_papildināt, text = '+', command = plus_viens_papild)
    poga_plus_1.place(x = 300, y = 200)

    poga_mīnus_1 = Button(logs_papildināt, text = '-', command = mīnus_viens_papild)
    poga_mīnus_1.place(x = 180, y = 200)

    teksts_atlikums = Label(logs_papildināt, text = str(galvenais_konts), font = 'Inter 8', bg = 'white', fg = '#ABABAB')
    teksts_atlikums.place(x = 220, y = 240)

    teksts_EUR = Label(logs_papildināt, text = f'EUR', font = 'Inter 8', bg = 'white', fg = '#ABABAB')
    teksts_EUR.place(x = 260, y = 240)

    Button(logs_papildināt, text="+2", font="Inter 10", command=lambda: add_amount(2)).place(x=50, y=300)
    Button(logs_papildināt, text="+5", font="Inter 10", command=lambda: add_amount(5)).place(x=150, y=300)
    Button(logs_papildināt, text="+10", font="Inter 10", command=lambda: add_amount(10)).place(x=250, y=300)
    Button(logs_papildināt, text="+20", font="Inter 10", command=lambda: add_amount(20)).place(x=350, y=300)
    Button(logs_papildināt, text="Viss", font="Inter 10", command=reset_amount).place(x=450, y=300)

    nosūtīt_image = PhotoImage(file = "C:/images/nosūtīt.png")
    nosūtīt_poga = Button(logs_papildināt,text = 'nosūtīt',command = nosūtīt)
    nosūtīt_poga.place(x = 220, y = 370)

#Logs izņemt

def izņemt_logs():
    global izņēmuma_summa
    global teksts_atlikums
    logs_izņemt = Toplevel()
    logs_izņemt.title("Izņemt")
    logs_izņemt.geometry('500x500')
    logs_izņemt.configure(background = 'white')

    izņemt_logs_teksts_1 = Label(logs_izņemt, text = 'Izņemt', font = 'Inter 24', bg = 'white', fg = 'darkorange')
    izņemt_logs_teksts_1.place(x = 30, y = 20)

    izņēmuma_summa = Label(logs_izņemt, text=str(izņēmuma_summa_skaitlis), font='Inter 32', bg='white')
    izņēmuma_summa.place(x=200, y=180)

    poga_plus = Button(logs_izņemt, text = '+', command = plus_viens)
    poga_plus.place(x = 300, y = 200)

    poga_mīnus = Button(logs_izņemt, text = '-', command = mīnus_viens)
    poga_mīnus.place(x = 180, y = 200)

    Button(logs_izņemt, text="+2", font="Inter 10", command=lambda: pievienot_vērtību(2)).place(x=50, y=300)
    Button(logs_izņemt, text="+5", font="Inter 10", command=lambda: pievienot_vērtību(5)).place(x=150, y=300)
    Button(logs_izņemt, text="+10", font="Inter 10", command=lambda: pievienot_vērtību(10)).place(x=250, y=300)
    Button(logs_izņemt, text="+20", font="Inter 10", command=lambda: pievienot_vērtību(20)).place(x=350, y=300)
    Button(logs_izņemt, text="Viss", font="Inter 10", command=noņemt_vertību).place(x=450, y=300)

    nosūtīt_poga = Button(logs_izņemt,text = 'Iznemt',command = izņemt_funkcija)
    nosūtīt_poga.place(x = 220, y = 370)


#galvenās pogas
papildināt = PhotoImage(file = "Krajriks\images\papildināt.png")
izņemt = PhotoImage(file = "Krajriks\images\izņemt.png")
pieprasīt = PhotoImage(file = "Krajriks\images\pieprasīt.png")

poga_papildināt = Button(window, image = papildināt, command = papildināt_logs, borderwidth = 0, background = 'white')
poga_papildināt.place(x = 50, y = 120)

poga_izņmet = Button(window, image = izņemt, command = izņemt_logs, borderwidth = 0, background = 'white')
poga_izņmet.place(x = 310, y = 120)

poga_pieprasīt = Button(window, image = pieprasīt, command = papildināt_logs, borderwidth = 0, background = 'white')#Aizvieto ar jauna loga funkciju
poga_pieprasīt.place(x = 570, y = 120)

#pārējais teksts
teksts_uzkrātie_procenti = Label(window, text = f"Uzkrātie procenti", font = 'Inter 16', background = 'white')
teksts_uzkrātie_procenti.place(x = 50, y = 250)

procenti_uzkrātie_procenti = Label(window, text = f"{uzkrātie_procenti} EUR", font = 'Inter 16', background = 'white')
procenti_uzkrātie_procenti.place(x = 650, y = 250)

teksts_procentu_likme = Label(window, text = f"Procentu likme", font = 'Inter 16', background = 'white')
teksts_procentu_likme.place(x = 50, y = 300)

procenti_procentu_likme = Label(window, text = f"{procentu_likme} %", font = 'Inter 16', background = 'white')
procenti_procentu_likme.place(x = 670, y = 300)

uzkrāšanās_metodes = Label(window, text = 'Uzkrāšanas metodes', font = 'Inter 18 bold', background = 'white', fg = 'darkorange')
uzkrāšanās_metodes.place(x = 50, y = 370)

apaļošana_teksts = Label(window, text = 'Apaļošana', font = 'Inter 17 bold', background = 'white', fg = 'black')
apaļošana_teksts.place(x = 100, y = 400)

apaļošana_apraksts = Label(window, text = 'Saglabāt naudu no katra maksājuma ar karti', font = 'Inter 8 bold', background = 'white', fg = '#BAB3B3')
apaļošana_apraksts.place(x = 110, y = 435)

window.mainloop()
