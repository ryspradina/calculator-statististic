from tkinter import *
import tkinter.messagebox
import numpy as np
import statistics

def rata2(angkalist) :
    return sum(angkalist) / len(angkalist)

def stat(List) :
    mean = rata2(List)
    median = statistics.median(List)
    
    Q1 = np.percentile(List, 25)  # Q1    
    Q2 = np.percentile(List, 50)  # median
    Q3 = np.percentile(List, 75)  # Q3

    modus=statistics.mode(List)
    simpbaku=statistics.stdev(List)
    
    return [mean,median,modus,simpbaku,Q1,Q2,Q3]
        
def click() :
    text = txt.get()
    try :
        # input list angka
        List = [int(x) for x in text.split(',')]
        # menampilkan list
        lst = Label(text = List, relief=SUNKEN, width=20).grid(row=4,column=1)

        # mencari mean, median, dll dari List angka yang sudah di input
        star = stat(List)

        # menampilkan mean, median, modus, simpbaku, dan kuartil
        r = 5
        for i in range(len(star)):
            Label(text=star[i], relief=SUNKEN, width=20).grid(row=r,column=1)
            r = r + 1
    # kondisi jika terjadi error
    except statistics.StatisticsError as error :
        messagebox.showinfo('Warning', error)
        
    except ValueError as err:
        messagebox.showinfo('Warning', err)

window = Tk()
window.title("Kalkulator Statistika Deskriptif")

lbl1 = Label(window, text = "Masukan angka dan pisahkan dengan koma")
lbl1.grid(columnspan = 2, row = 0)

lbl2 = Label(window, text = "Contoh : 1,1,2")
lbl2.grid(columnspan = 2, row = 1)

# textarea
txt = Entry(window, width = 44)
txt.grid(columnspan = 2, row = 2)
txt.focus()

# button proses
btnProses = Button(window, text = "PROSES", command = click)
btnProses.grid(columnspan = 2, row = 3)

# menampilkan label bagian kiri
statsT = ['List','Mean','Median','Modus','Simpangan Baku','Q1','Q2','Q3']
r = 4
for x in statsT:
    Label(text=x, relief=RIDGE, width=17).grid(row=r,column=0)
    Label(relief=SUNKEN, width=20).grid(row=r,column=1)
    r = r + 1

window.mainloop()
