import PyPDF2
import tkinter as tk

#Gui of the program
window = tk.Tk()
#print(help(tk.Tk))
window.geometry("600x300")
window.title("PDF tool")

r=5
c=6
print(type(r))
tk.Button(text="click", borderwidth=1).grid(row=r, column=c)


#It's work in progress




if  __name__ == "__main__":
    window.mainloop()










































