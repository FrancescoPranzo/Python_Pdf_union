import PyPDF2
import tkinter as tk
from tkinter import filedialog
from object import pdf



window = tk.Tk()
#print(help(tk.Tk))
window.geometry("600x300")
window.title("PDF tool")

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
    print("sono nella funzione strana")

    global list_file_name
    print(list_file_name)
    #print(len(list_file_name))
    pd = pdf("arrigo", list_file_name[0])
    pd.open_myfile_read()


#aggiungere il parametro command
Button1 = tk.Button(text="Choose another file", command=file_choose)
Button1.grid(row=r, column=c)

Button2 = tk.Button(text="Generate a file", borderwidth=2, command=generate_file_pdf)
Button2.grid(row=2, column=2)



if  __name__ == "__main__":
    window.mainloop()
#work in progress
