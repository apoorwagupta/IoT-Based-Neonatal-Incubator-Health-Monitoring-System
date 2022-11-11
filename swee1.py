from time import sleep
import tkinter as tk
from tkinter import Message, Text
from tkinter import font as tkFont
import serial
import yagmail
from time import strftime
from datetime import date
import datetime
import urllib.request
import csv
global pieces
global count
count=0
import http.client, urllib
pieces=['0','0','0','0','0']
myAPI = 'MEW6SJ45N9G6WE1L'
ser = serial.Serial('COM5',baudrate=9600)
fields = 'Date'+','+ 'Time'+',' +'Heart rate'+',' +'So2'+',' +'Temp'+','+ 'Humidity'+','+'Body temp'
filename = "university_records.csv"
baseURL = 'https://api.thingspeak.com/update?api_key='+myAPI
file = open(filename, "a")
print("Created file")
file = open(filename, "a")
file.write(fields+'\n')
file.close()
window = tk.Tk()
window.title("Lab Spectro Analysis")
message = tk.Label(window, text="Baby Health Monitoring ", bg="purple", fg="White", width=58, height=2,
				   font=('times', 30, 'italic bold'))
message.place(x=10, y=10)

data1 = tk.Label(window, text="", fg="black", width=10, height=1, font=('times', 30, 'bold'))
data1.place(x=0, y=200)
datas1 = tk.Label(window, text="", fg="Red", width=10, height=1, font=('times', 30, 'bold'))
datas1.place(x=0, y=250)
data2 = tk.Label(window, text="", fg="black", width=10, height=1, font=('times', 30, 'bold'))
data2.place(x=250, y=200)
datas2 = tk.Label(window, text="", fg="Red", width=10, height=1, font=('times', 30, 'bold'))
datas2.place(x=250, y=250)
data3 = tk.Label(window, text="", fg="black", width=10, height=1, font=('times', 30, 'bold'))
data3.place(x=500, y=200)
datas3 = tk.Label(window, text="", fg="Red", width=10, height=1, font=('times', 30, 'bold'))
datas3.place(x=500, y=250)
data4 = tk.Label(window, text="", fg="black", width=10, height=1, font=('times', 30, 'bold'))
data4.place(x=750, y=200)
datas4 = tk.Label(window, text="", fg="Red", width=10, height=1, font=('times', 30, 'bold'))
datas4.place(x=750, y=250)
data5 = tk.Label(window, text="", fg="black", width=10, height=1, font=('times', 30, 'bold'))
data5.place(x=1100, y=200)
datas5 = tk.Label(window, text=pieces[4], fg="Red", width=10, height=1, font=('times', 30, 'bold'))
datas5.place(x=1100, y=250)
def sendpush(condition):
	conn = http.client.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
	             urllib.parse.urlencode({
		             "token": "aumn1tzk7jq9m17sz8uqcizwgwq9bk",
		             "user": "uchoxvtez72q7aa85dm3tpc19ytkv2",
		             "message": condition,

	             }), {"Content-type": "application/x-www-form-urlencoded"})
	conn.getresponse()

def email():
	sub = "Daily Report for " + str(date.today())
	# mail information
	yag = yagmail.SMTP(user="i4usmriti@gmail.com", password='')
	body = "kindly Find Attachment"
	# sent the mail
	yag.send(
		to="i4usmriti@gmail.com",
		subject=sub,  # email subject
		contents=body,  # email body
		attachments=filename  # file attached
	)
def time1():
	global pretime
	global pieces
	global count
	date1 = date.today()
	string12 = strftime('%H:%M:%S %p')
	string = string12 + '\n' + str(date1)
	while ser.in_waiting>0:
		data = ser.readline().decode()
		pieces = data.split(" ")
		datafile = str(date1)+','+string12+',' +pieces[0] + ',' + pieces[1] + ',' + pieces[2] + ',' + pieces[3] + ',' + pieces[4]
		file = open(filename, "a")
		file.write(datafile)
		file.write('\n')
		file.close()
		conn = urllib.request.urlopen(
			baseURL + '&field1=' + str(pieces[0]) + '&field2=' + str(pieces[1]) + '&field3=' + str(
				pieces[2]) + '&field4=' + str(pieces[3]) + '&field5=' + str(pieces[4]))
		# Closing the connection
		conn.close()

		if float(pieces[4])>30 or float(pieces[0])<90 or float(pieces[2])>=37.8:
			condition ="Alert!! Body temp"+ str(pieces[4])+'\n'+"Alert!! Humidity="+ str(pieces[3])+'\n'+"Alert!! Temperature="+ str(pieces[2])+"Alert!! SpO2=" + str(pieces[1])+'\n'+"Alert!! Heart beat="+ str(pieces[0])
			sendpush(condition)
		break

	lbl.config(text=string)


	data1.config(text="BPM")
	data2.config(text="SpO2")
	data3.config(text="Temp")
	data4.config(text="Humidity")
	data5.config(text="B.Temp")
	datas1.config(text=pieces[0])
	datas2.config(text=pieces[1])
	datas3.config(text=pieces[2])
	datas4.config(text=pieces[3])
	datas5.config(text=pieces[4])
	lbl.after(1, time1)


lbl = tk.Label(window, font=('calibri', 18, 'bold'),
			   background='purple',
			   foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.place(relx=0.95,
		  rely=0.04,
		  anchor='ne')

btnExit = tk.Button(window, padx=16, pady=8, bd=10,
                 fg="black", font=('arial', 16, 'bold'),
                 width=5, text="Email",
                 command=email)
btnExit.place(x=550, y=500)
time1()
window.mainloop()
