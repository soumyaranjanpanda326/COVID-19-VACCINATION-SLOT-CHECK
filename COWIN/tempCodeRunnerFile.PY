from cgitb import text
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pytz
import requests

software_version = 'v1.1'

top_left_frame_bg = "#5c4ce1"
top_right_frame_bg = "#867ae9"


app = Tk() # object of tkinter

# app geometry and components
app.geometry("700x400")
app.title(f"Vaccine availability checker {software_version}")
app.iconbitmap('D:\Python Projects\Cowin API\COWIN\IMGS\download.ico')
app.resizable(False,False)
app.config(background='#293241')

# add frames

frame1 = Frame(app,height= 120,width=180,bg = top_left_frame_bg,bd = 1 , relief=FLAT)
frame1.place(x = 0 , y = 0)
frame2 = Frame(app,height= 120,width=520,bg = top_right_frame_bg,bd = 1 , relief=FLAT)
frame2.place(x = 180, y = 0)

frame3 = Frame(app,height= 30,width=700,bg = 'black',bd = 1 , relief=FLAT)
frame3.place(x = 0,y = 120)


# entry box
pincode_text_var = StringVar()
pincode_text = Entry(app,width= 11 , bg = '#eaf2ae',fg = "black" , font = 'verdana 11', textvariable=pincode_text_var)
pincode_text.place(x = 220,y = 40)
pincode_text['textvariable'] = pincode_text_var

date_text_var = StringVar()
date_text = Entry(app,width= 11 , bg = '#eaf2ae',fg = "black" , font = 'verdana 11', textvariable=date_text_var)
date_text.place(x = 380,y = 40)
date_text['textvariable'] = date_text_var


# button
search_vaccine_image = PhotoImage(file="D:\Python Projects\Cowin API\COWIN\IMGS\search.png")
search_vaccination_btn = Button(app,width = 25, bg = top_right_frame_bg, relief=RAISED,command='', image=search_vaccine_image)
search_vaccination_btn.place(x = 600,y = 30)

# labels
label_date_now = Label(text = "Current Data", bg = top_left_frame_bg , font= ' verdana 12 bold'  )
label_date_now.place(x = 20, y = 40)

label_time_now = Label(text = "Current time", bg = top_left_frame_bg , font= ' verdana 12 bold'  )
label_time_now.place(x = 20, y = 60)

label_pincode = Label(text = "Pincode", bg = top_right_frame_bg , font= ' verdana 11 bold'  )
label_pincode.place(x = 220 , y = 15 )

label_date = Label(text = "Date", bg = top_right_frame_bg , font= ' verdana 11 bold'  )
label_date.place(x = 380 , y = 15 )

label_dateformat = Label(text = "[DD-MM-YYYY]", bg = top_right_frame_bg , font= ' verdana 7 bold'  )
label_dateformat.place(x = 420 , y = 18 )

label_search_vaccine = Label(text = "Search \nAvailable vaccine", bg = top_right_frame_bg , font= ' verdana 11 bold'  )
label_search_vaccine.place(x = 550 , y = 65 )

label_head_result = Label(text=" Status       \tCentre-Name\t              Age-Group    Vaccine       Dose_1     Dose_2     Total", bg = 'black', fg='white', font = 'Verdana 8 bold')
label_head_result.place(x=10, y=125)

app.mainloop()

