import tkinter
from tkinter import ttk

length = {
        # Metric (SI, in meters)
        "ym": 1e-24,"zm": 1e-21,"am": 1e-18,"fm": 1e-15,"pm": 1e-12,"nm": 1e-9,"µm": 1e-6,"mm": 1e-3,"cm": 1e-2,"dm": 1e-1,
        "m": 1.0,"dam": 1e1,"hm": 1e2,"km": 1e3,"Mm": 1e6,"Gm": 1e9,"Tm": 1e12,
        # Imperial → meters
        "in": 0.0254,"ft": 0.3048,"yd": 0.9144,"ch": 20.1168,"fur": 201.168,"mi": 1609.344,"lea": 4828.032
    }
weight = {
        # Metric (SI, in grams)
        "yg": 1e-24,"zg": 1e-21,"ag": 1e-18,"fg": 1e-15,"pg": 1e-12,"ng": 1e-9,"µg": 1e-6,"mg": 1e-3,"cg": 1e-2,"dg": 1e-1,
        "g": 1.0,"dag": 1e1,"hg": 1e2,"kg": 1e3,"Mg": 1e6,
        # Imperial → grams
        "gr": 0.06479891,"dr": 1.771845,"oz": 28.349523125,"lb": 453.59237,"st": 6350.29318,
        "qr": 12700.58636,"cwt_us": 45359.237,"cwt_uk": 50802.34544,"ton_us": 907184.74,"ton_uk": 1016046.9088
    }
volume = {
        # Metric (SI, in liters)
        "yl": 1e-24,"zl": 1e-21,"al": 1e-18,"fl": 1e-15,"pl": 1e-12,"nl": 1e-9,"µl": 1e-6,
        "ml": 1e-3,"cl": 1e-2,"dl": 1e-1,"l": 1.0, "dal": 1e1,"hl": 1e2,"kl": 1e3,
        # Imperial (US) → liters
        "floz_us": 0.0295735,"gill_us": 0.118294,"pt_us": 0.473176,"qt_us": 0.946353,"gal_us": 3.78541,
        # Imperial (UK) → liters
        "floz_uk": 0.0284131,"gill_uk": 0.142065,"pt_uk": 0.568261, "qt_uk": 1.13652,"gal_uk": 4.54609
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