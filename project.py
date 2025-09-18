import tkinter
from tkinter import ttk


def main():
    display()

def convert_weight(x, y):
    ...
def convert_length(x, y):
    ...
def convert_tempeture(x, y):
    ...
def convert_currency(x, y):
    ...
def get_currency():
    ...

def display():
    window = tkinter.Tk()
    window.title("first window")
    window.geometry("400x200")

    style = ttk.Style()
    style.configure("TLabel", font=("Segoe UI", 12))
    style.configure("TButton", font=("Segoe UI", 11), padding=6)

    label = tkinter.Label(window, text="Enter a number:")
    label.pack(pady=10)

    entry = ttk.Entry(window)
    entry.pack(pady=5)


    window.mainloop()

if __name__ == "__main__":
    main()