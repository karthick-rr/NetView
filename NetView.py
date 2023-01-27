import os
import nmap
import socket
from tkinter import *
from  tkinter import ttk

#Window creation and setting the values    

ws = Tk()
ws.title('NetView')

#frame for hosts

output_frame = Frame(ws)
output_frame.pack()
frame = ttk.Treeview(output_frame)
frame['columns'] = ('S.No', 'Name', 'IPv4', 'MAC','Namee')
frame.column("#0", width=0,  stretch=NO)
frame.column("S.No",anchor=CENTER,width=160)
frame.column("Name",anchor=CENTER,width=160)
frame.column("IPv4",anchor=CENTER,width=160)
frame.column("MAC",anchor=CENTER,width=160)
frame.column("Namee",anchor=CENTER,width=400)
frame.heading("S.No",text="S.No",anchor=CENTER)
frame.heading("Name",text="Device Name",anchor=CENTER)
frame.heading("IPv4",text="IPv4",anchor=CENTER)
frame.heading("MAC",text="MAC",anchor=CENTER)
frame.heading("Namee",text="Vendor",anchor=CENTER)
frame.pack(side='top',fill='both', expand=True)

#frame for admin 

output_frame1 = Frame(ws)
output_frame1.pack()
frame1 = ttk.Treeview(output_frame1)
frame1['columns'] = ('Role','Device Name', 'IPv4', 'MAC','Vendor')
frame1.column("#0", width=0,  stretch=NO)
frame1.column("Role",anchor=CENTER,width=160)
frame1.column("Device Name",anchor=CENTER,width=160)
frame1.column("IPv4",anchor=CENTER,width=160)
frame1.column("MAC",anchor=CENTER,width=160)
frame1.column("Vendor",anchor=CENTER,width=400)
frame1.heading("Device Name",text="This PC",anchor=CENTER)
frame1.heading("Role",text="Role",anchor=CENTER)
frame1.heading("IPv4",text="IPv4",anchor=CENTER)
frame1.heading("MAC",text="MAC",anchor=CENTER)
frame1.heading("Vendor",text="Vendor",anchor=CENTER)
frame1.pack(side='top',fill='both', expand=True)

#Split and List the ip address, Pass the argument.

nm = nmap.PortScanner()
hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)
t = ipaddress[::-1].index(".")
	
data = nm.scan(hosts=ipaddress[:-t]+'0/24', arguments='-sn  \n')
print(" Processing...")
#for find the Host machine MAC address

getmac=os.popen('getmac').read()
list1=getmac.split('\n')
getmac1=os.popen('getmac | findstr "Media"').read()
list2=getmac1.split('\n')
finallist=[x for x in list1 if x not in list2]
del finallist[0:2]
Mac=finallist[0]
Mac_addr=Mac[0:18]

#for find the Host vendor name

role='Admin'
find_Vendor=list(data['scan'][ipaddress]['vendor'].values())
Vendor_Name=""
if (len(find_Vendor)==1):
	Vendor_Name=s[0]

#Find the values based on the arguments and set the right place

#for Host machine details
frame1.insert(parent='',index='end',values=(role,hostname,ipaddress,Mac_addr,Vendor_Name))

#for Connected host detials
index = 1
for i in data['scan']:
	name = (data['scan'][i]['hostnames'][0]['name'])
	ipaddr = data['scan'][i]['addresses']['ipv4']
	s=list(data['scan'][i]['vendor'].values())
	Vendor_Name=""
	if (len(s)==1):
		Vendor_Name=s[0]
	if (i!=ipaddress):
		Mac_address = list(data['scan'][i]['vendor'].keys())
		frame.insert(parent='',index='end',iid=i,values=(str(index),name,ipaddr,Mac_address,Vendor_Name))
		index+=1
	else:
		frame.insert(parent='',index='end',iid=i,values=(str(index),hostname,ipaddr,Mac_addr,Vendor_Name))
		index+=1
print(" . \n . \n . \n . \n Completed Successfully.")
ws.mainloop()
