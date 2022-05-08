#import PdfFileWriter and PdfFileReader
#class from PyPDF2 library

from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *
#create a PdfFileWriter object
out = PdfFileWriter()

#open out PDF file with the PDFFileReader
#Program to make a simple
#login screen

import tkinter as tk
root = tk.Tk()

#setting the windows size
root.geometry("800x400")
bg = PhotoImage( file = "file.png")

labell = Label(root,image=bg)
labell.place(x=0,y=0)

root.title('PDF ENCRYPTOR')
#declaring string variable
#for storing name and password

name_var = tk.StringVar()
passw_var =tk.StringVar()
newname_var = tk.StringVar()
#defining a function that will
#get the name and password and print them on the screen
def submit():
    name =name_entry.get()
    password=passw_var.get()
    newname=newname_var.get()

    root.destroy()
#creating a label for name using widget label
name_label = tk.Label(root, text='File Name', font=('calibre',10,'bold'))

#creating a entry for input name using widget entry
name_entry = tk.Entry(root,textvariable= name_var,font=('calibre',10,'normal'))

#creating a label for Note
note_label = tk.Label(root, text= 'NOE: FILE NAME AND THE ENCRYPTED FILE NAME SHOULD CONTAIN ".pdf" EXTENSION',font=('calibre',8))
#creating a label for password
passw_label= tk.Label(root,text='Password',font=('calibre',10,'bold'))
#creating a label for des
d_label = tk.Label(root, text='DESIGNED BY: KUNAL CHAWLA',font=('calibre',8))
#creating a entry for password
passw_entry = tk.Entry(root, textvariable=passw_var,font=('calibre',10,'normal'))
#creating a label for encrypted file name 
newname_label = tk.Label(root, text='Encrypted File Name',font=('calibre',10,'bold'))
#creating a entry for encrypted file name
newname_entry = tk.Entry(root,textvariable= newname_var, font =('calibre',10,'normal'))
#creating a button using the widget button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command= submit)
#placing the label and entry in the required position using grid method
name_label.grid(row=0,column=0)
name_entry.grid (row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
newname_label.grid(row=2,column=0)
newname_entry.grid(row=2,column=1)
sub_btn.place(x=120,y=90)
note_label.place(x=300,y=5)
d_label.place(x=600,y=350)
#performing an infinite loop for the window to display
root.mainloop()
#open encrypted PDF file with PdfFileReader
file = PdfFileReader(name_var.get())

#store correct password in a variable passwprd.
password = passw_var.get()

#check if the opened file is actually encrypted 
if file.isEncrypted:
    #if encrypted, decrypt it with the password
    file.decrypt(password)

    #iterate through every page of the file and add it t out new file

    for idx in range (file.numPages):
        #get the page at index idx
        page = file.getPage(idx)
        #add it to the output file
        out.addPage(page)

    #open a new file "myfile_decypted.pdf"
    with open (newname_var.get(),"wb")as f:
        #write our decrypted PDF to this file
        out.write(f)
    #print success message when done
    print("File decrypted Successfully.")
else:
    #if file is not encrypted,print the message
    print("File already decrypted.")
