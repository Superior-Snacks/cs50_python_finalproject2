import tkinter
from tkinter import ttk

units = {
    "metric_lenght":[eniter scope of metric lenght units],
    "imperial_lenght":[eniter scope of imperial lenght units],
    "metric_weight":[eniter scope of metric weight units],
    "imperial_weight":[eniter scope of imperial weight units],
}
def main():
    display()

def convert_weight(x, untitx, y, unity):
    



def convert_length(x, y):
    ...
def convert_tempeture(x, y):
    ...
def convert_currency(x, y):
    ...
def get_currency():
    ...

def display(output):
    window = tkinter.Tk()
    window.title("first window")
    window.geometry("400x200")

    style = ttk.Style()
    style.configure("TLabel", font=("Segoe UI", 12))
    style.configure("TButton", font=("Segoe UI", 11), padding=6)

    label = tkinter.Label(window, text=output)
    label.pack(pady=10)
    window.mainloop()

if __name__ == "__main__":
    main()