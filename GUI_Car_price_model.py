import tkinter as tk
import pickle 
import pandas as pd

win = tk.Tk()
win.geometry("500x400")
win.title("Welcome to Car Price Predictor")
win.configure(bg="black")

def click():
    num1 =e1.get()
    num2 =int(e2.get())
    num3 =float(e3.get())
    num4 =int(e4.get())
    num5 =e5.get()
    num6 =e6.get()
    num7 =e7.get()
    num8 =int(e8.get())
    
    pipe=pickle.load(open('pipe.pkl','rb'))
    price_predict=pipe.predict(pd.DataFrame([[num1,num2,num3,num4,num5,num6,num7,num8]],columns=['Car_Name', 'Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type',
       'Seller_Type', 'Transmission', 'Owner']))
    
    l_click=tk.Label(win,text=price_predict,font="Times 15 bold").place(x=280,y=450)




l1 = tk.Label(win, text="Car Name:", font="Times 15 bold").place(x=40, y=80)
e1=tk.Entry(win,font="Times 15 bold")

l2 = tk.Label(win, text="Year:", font="Times 15 bold").place(x=40, y=140)
e2=tk.Entry(win,font="Times 15 bold")


l3 = tk.Label(win, text="Present_Price:", font="Times 15 bold").place(x=40, y=180)
e3=tk.Entry(win,font="Times 15 bold")

l4 = tk.Label(win, text="Kms_Driven:", font="Times 15 bold").place(x=40, y=220)
e4=tk.Entry(win,font="Times 15 bold")

l5 = tk.Label(win, text="Fuel_Type:", font="Times 15 bold").place(x=40, y=260)
e5=tk.Entry(win,font="Times 15 bold")


l6 = tk.Label(win, text="Seller_Type:", font="Times 15 bold").place(x=40, y=300)
e6=tk.Entry(win,font="Times 15 bold")


l7 = tk.Label(win, text="Transmission:", font="Times 15 bold").place(x=40, y=340)
e7=tk.Entry(win,font="Times 15 bold")


l8 = tk.Label(win, text="Owner:", font="Times 15 bold").place(x=40, y=380)
e8=tk.Entry(win,font="Times 15 bold")

b1=tk.Button(win,text="Predict",font="Times 15 bold",command=click).place(x=40,y=450)

e1.place(x=280,y=80)
e2.place(x=280,y=140)
e3.place(x=280,y=180)
e4.place(x=280,y=220)
e5.place(x=280,y=260)
e6.place(x=280,y=300)
e7.place(x=280,y=340)
e8.place(x=280,y=380)



win.mainloop()






