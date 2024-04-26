from tkinter import *
from tkinter import ttk

import requests

def data_get():
    city= city_name.get()
    data =requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
# for data featch
    w_lable1.config(text=data["weather"][0]["main"])                    
    wdes_lable1.config(text=data["weather"] [0] ["description"])
    wtemp_lable1.config(text=str(data["main"] ["temp"]-273.15))
    wpres_lable1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Weather App")
win.config(bg = "pink")
win.geometry("500x500")

name_lable = Label(win,text ="Weather App",
                   font=("Time New Roman",30,"bold"))

name_lable.place(x=25,y=50,height=50,width=450)

# for suggestion name and opening drawer box

city_name= StringVar()
list_name =  ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text ="Weather App",values=list_name,
                   font=("Time New Roman",15,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)


w_lable = Label(win,text ="Weather climate",
                   font=("Time New Roman",15))

w_lable.place(x=25,y=260,height=50,width=210)
w_lable1 = Label(win,text ="",
                   font=("Time New Roman",15))

w_lable1.place(x=250,y=260,height=50,width=210)



wdes_lable = Label(win,text ="Weather description",
                   font=("Time New Roman",15))

wdes_lable.place(x=25,y=320,height=50,width=210)

wdes_lable1 = Label(win,text ="",
                   font=("Time New Roman",15))

wdes_lable1.place(x=250,y=320,height=50,width=210)



wtemp_lable = Label(win,text ="Temperature",
                   font=("Time New Roman",15))

wtemp_lable.place(x=25,y=380,height=50,width=210)
wtemp_lable1 = Label(win,text ="",
                   font=("Time New Roman",15))

wtemp_lable1.place(x=250,y=380,height=50,width=210)



wpres_lable = Label(win,text ="Pressure",
                   font=("Time New Roman",15))

wpres_lable.place(x=25,y=440,height=50,width=210)

wpres_lable1 = Label(win,text ="",
                   font=("Time New Roman",15))

wpres_lable1.place(x=250,y=440,height=50,width=210)

done_button =Button(win,text ="Done",
                   font=("Time New Roman",15,"bold"),command=data_get)

done_button.place(y=190,height=50,width=100,x=200 )



win.mainloop()