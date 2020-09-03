import PyPDF2
import tkinter as tk
from tkinter import filedialog
import random

#improve the user interface. Working and studying...
window = tk.Tk()
#print(help(tk.Tk))
window.geometry("600x300")
window.title("PDF tool")

#function to extract a page
#for now it only extract the values from the entry
def get_value_from_entry():
    value = int(first.get())
    print(value)
#work in progress above
r=1
c=1
#print(type(r))
#lista = [ ]
list_file_name = [ ]
def file_choose():
    #file_name = filedialog.askopenfilename()
    global list_file_name
    list_file_name.append(filedialog.askopenfilename())
    print(list_file_name)


def generate_file_pdf():
    name_new_file = "file_unito"+str(random.randint(1,70))+".pdf"
    global list_file_name
    print("sono nella funzione genera")
    print("il nome del nuovo file è: " + str(name_new_file))
    i = 0
    print("il tipo di i è:" + str(type(i)))
    
    with open(name_new_file, "wb") as file_merged:
        writer = PyPDF2.PdfFileWriter()
        
        print("sono nel with di scrittura")
        
        for i in list_file_name:
            with open(i, "rb") as file_read:
                print(i)
                reader = PyPDF2.PdfFileReader(file_read, strict=False)
                len_pdf = reader.getNumPages()
                i = 0
                for i in range(0, len_pdf):
                    page = reader.getPage(i)
                    writer.addPage(page)
                writer.write(file_merged)

    list_file_name = [ ]
#aggiungere il parametro command
Button1 = tk.Button(text="Choose the files", command=file_choose)
Button1.grid(row=r, column=c)

Button2 = tk.Button(text="Generate a file", borderwidth=2, command=generate_file_pdf)
Button2.grid(row=2, column=2)
Button2 = tk.Button(text="Generate a file", borderwidth=2, command=generate_file_pdf)
Button2.grid(row=2, column=1)
label= tk.Label()
label.grid(row=4, column=1)
#add the funciton to extract a page from a certain file
first = tk.Entry()
first.grid(row=5, column=1)
Button_extract = tk.Button(text="extract a page")
Button_extract.grid(row=5, column=2)
#Read the values from the entry...

if  __name__ == "__main__":
    window.mainloop()
