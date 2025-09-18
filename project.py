import tkinter
from tkinter import ttk

length = {
        # Metric (SI, in meters)
        "ym": 1e-24,"zm": 1e-21,"am": 1e-18,"fm": 1e-15,"pm": 1e-12,"nm": 1e-9,"µm": 1e-6,"mm": 1e-3,"cm": 1e-2,"dm": 1e-1,
        "m": 1.0,"dam": 1e1,"hm": 1e2,"km": 1e3,"Mm": 1e6,"Gm": 1e9,"Tm": 1e12,
        # Imperial → meters
        "in": 0.0254,"ft": 0.3048,"yd": 0.9144,"ch": 20.1168,"fur": 201.168,"mi": 1609.344,"lea": 4828.032
    }
def main():
    display()

def convert_weight(x, untitx, unity):
    ...
    



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