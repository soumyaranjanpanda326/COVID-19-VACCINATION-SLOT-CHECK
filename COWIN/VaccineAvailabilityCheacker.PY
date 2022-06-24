from cgitb import text 
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from unittest import result
from urllib import response
import pytz #timezone in python
import requests


IST = pytz.timezone('Asia/kolkata')
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




# labels
label_date_now = Label(text = "Current Data", bg = top_left_frame_bg , font= ' verdana 12 bold'  )
label_date_now.place(x = 20, y = 40)

label_time_now = Label(text = "Current time", bg = top_left_frame_bg , font= ' verdana 12 bold'  )
label_time_now.place(x = 20, y = 60)

label_pincode = Label(text = "Pincode", bg = top_right_frame_bg , font= 'verdana 11 bold'  )
label_pincode.place(x = 220 , y = 15 )

label_date = Label(text = "Date", bg = top_right_frame_bg , font= ' verdana 11 bold'  )
label_date.place(x = 380 , y = 15 )

label_dateformat = Label(text = "[DD-MM-YYYY]", bg = top_right_frame_bg , font= ' verdana 7 bold'  )
label_dateformat.place(x = 420 , y = 18 )

label_search_vaccine = Label(text = "Search \nAvailable vaccine", bg = top_right_frame_bg , font= ' verdana 11 bold'  )
label_search_vaccine.place(x = 550 , y = 65 )

label_head_result = Label(text=" Status       \tCentre-Name\t              Age-Group    Vaccine       Dose_1     Dose_2     Total", bg = 'black', fg='white', font = 'Verdana 8 bold')
label_head_result.place(x=10, y=125)


# Textbox for displaying results

result_box_avl = Text(app,height= 20 , width= 8, bg= '#293241', fg = '#ecfcff',relief=FLAT, font="verdana 10")
result_box_avl.place(x = 3 ,y =  152)

result_box_cent = Text(app,height= 20 , width= 30, bg= '#293241', fg = '#ecfcff',relief=FLAT, font="verdana 10")
result_box_cent.place(x = 75 ,y =  152)

result_box_age = Text(app,height= 20 , width= 8, bg= '#293241', fg = '#ecfcff',relief=FLAT, font="verdana 10")
result_box_age.place(x = 330 ,y =  152)

result_box_vacc = Text(app,height= 20 , width= 10, bg= '#293241', fg = '#ecfcff',relief=FLAT, font="verdana 10")
result_box_vacc.place(x = 400 ,y =  152)

result_box_D1 = Text(app,height= 20 , width= 7, bg= '#293241', fg = '#ecfcff',relief=FLAT, font="verdana 10")
result_box_D1.place(x = 480 ,y =  152)

result_box_D2 = Text(app,height= 20 , width= 7, bg= '#293241', fg = '#ecfcff',relief=FLAT, font="verdana 10")
result_box_D2.place(x = 550 ,y =  152)

result_box_D1_D2 = Text(app,height= 20 , width= 8, bg= '#293241', fg = '#ecfcff',relief=FLAT, font="verdana 10")
result_box_D1_D2.place(x = 620 ,y =  152)



# Detect Automatic Pincode

def fill_pincode_with_radio():
    curr_pincode = get_pincode_ipService(url)
    pincode_text_var.set(curr_pincode)
    

url = "https://ipinfo.io/postal"
def get_pincode_ipService(url):
    response_pincode = requests.get(url).text
    return response_pincode

# Realtime clock 

def updateClock():
    raw_TS = datetime.now(IST)
    date_now = raw_TS.strftime("%d %b %Y")
    time_now = raw_TS.strftime("%H:%M:%S %p")
    label_date_now.config(text=date_now)
    label_time_now.config(text= time_now)
    label_time_now.after(1000,updateClock)


# checkbox for current date

def insert_today_date():
    raw_TS = datetime.now(IST)
    formatted_now = raw_TS.strftime("%d-%m-%Y")
    date_text_var.set(formatted_now)




# API Call

def request_api_call(PINCODE,DATE):
    request_link =  f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={PINCODE}&date={DATE}"
    response = requests.get(request_link)
    resp_JSON = response.json()
    return resp_JSON

def clear_result_box():
    result_box_avl.delete('1.0',END)
    result_box_cent.delete('1.0',END)
    result_box_age.delete('1.0',END)
    result_box_vacc.delete('1.0',END)
    result_box_D1.delete('1.0',END)
    result_box_D2.delete('1.0',END)
    result_box_D1_D2.delete('1.0',END)


def search_vaccine_avl():
    clear_result_box()
    PINCODE = pincode_text_var.get().strip()
    DATE = date_text_var.get()
    resp_JSON = request_api_call(PINCODE,DATE)


    try:
        if len(resp_JSON['sessions']) == 0:
            messagebox.showinfo("INFO","Vaccine not yet arrived for the given date")

        for i in resp_JSON['sessions']:
            age_limit           = i['min_age_limit']
            center_name         = i['name']
            pincode             = i['pincode']
            vaccine_name        = i['vaccine']
            available_capacity  = i['available_capacity']
            qnty_dose_1         = i['available_capacity_dose1']
            qnty_dose_2         = i['available_capacity_dose2']
            slot_date           = i['date']

            if available_capacity > 0:
                curr_status = 'Available'
            else:
                curr_status = 'NA'
            
            if age_limit == 45:
                age_grp = '45+'
            else:
                age_grp = '18-44'

        
            result_box_avl.insert(END, f"{curr_status:^6s}")
            result_box_avl.insert(END,"\n")
            result_box_cent.insert(END, f"{center_name:<30.29s}")
            result_box_cent.insert(END,"\n")
            result_box_age.insert(END, f"{age_grp:<6s}")
            result_box_age.insert(END,"\n")
            result_box_vacc.insert(END, f"{vaccine_name:<8s}")
            result_box_vacc.insert(END,"\n")
            result_box_D1.insert(END, f"{qnty_dose_1:>5}")
            result_box_D1.insert(END,"\n")
            result_box_D2.insert(END, f"{qnty_dose_2:>5}")
            result_box_D2.insert(END,"\n")
            result_box_D1_D2.insert(END, f"{available_capacity:<5}")
            result_box_D1_D2.insert(END,"\n")
    except KeyError as KE:
        messagebox.showerror("ERROR","No Available center(s) for the given Pincode and date")
        print (pincode_text_var.get())

#checkbox
checkbox_today_var = IntVar()
today_date_checkbox = Checkbutton(app, text="Today", bg = top_right_frame_bg,variable=checkbox_today_var,onvalue=1,offvalue=0,command=insert_today_date)
today_date_checkbox.place(x = 380, y = 65)

chkbox_tomorrow_var = IntVar()
tomorrow_date_chkbox = Checkbutton(app, text='Tomorrow', bg= top_right_frame_bg, variable=chkbox_tomorrow_var, onvalue= 1, offvalue=0, state = DISABLED)
tomorrow_date_chkbox.place(x= 435, y= 65)



# button
search_vaccine_image = PhotoImage(file="D:\Python Projects\Cowin API\COWIN\IMGS\search.png")
search_vaccination_btn = Button(app,width = 25, bg = top_right_frame_bg, relief=RAISED,command=search_vaccine_avl, image=search_vaccine_image)
search_vaccination_btn.place(x = 600,y = 30)



# Radio Buttons
curr_loca_var = StringVar()
radio_location = Radiobutton(app,text = "Curent Location" , bg=top_right_frame_bg, variable=curr_loca_var,command=fill_pincode_with_radio)
radio_location.place(x = 225, y = 65)



updateClock()
app.mainloop()

