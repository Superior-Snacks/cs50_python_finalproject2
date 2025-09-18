import tkinter
from tkinter import ttk
import requests
import re

currencies = ['AUD','BGN','BRL','CAD','CHF','CNY','CZK','DKK','EUR','GBP','HKD','HUF','IDR','ILS','INR','ISK',
                'JPY','KRW','MXN','MYR','NOK','NZD','PHP','PLN','RON','SEK','SGD','THB','TRY','USD','ZAR']
weight = {
    # Metric (SI, in grams)
    "yg": 1e-24,"zg": 1e-21,"ag": 1e-18,"fg": 1e-15,"pg": 1e-12,"ng": 1e-9,"µg": 1e-6,"mg": 1e-3,"cg": 1e-2,"dg": 1e-1,
    "g": 1.0,"dag": 1e1,"hg": 1e2,"kg": 1e3,"Mg": 1e6,
    # Imperial → grams
    "gr": 0.06479891,"dr": 1.771845,"oz": 28.349523125,"lb": 453.59237,"st": 6350.29318,
    "qr": 12700.58636,"cwt_us": 45359.237,"cwt_uk": 50802.34544,"ton_us": 907184.74,"ton_uk": 1016046.9088}
length = {
    # Metric (SI, in meters)
    "ym": 1e-24,"zm": 1e-21,"am": 1e-18,"fm": 1e-15,"pm": 1e-12,"nm": 1e-9,"µm": 1e-6,"mm": 1e-3,"cm": 1e-2,"dm": 1e-1,
    "m": 1.0,"dam": 1e1,"hm": 1e2,"km": 1e3,"Mm": 1e6,"Gm": 1e9,"Tm": 1e12,
    # Imperial → meters
    "in": 0.0254,"ft": 0.3048,"yd": 0.9144,"ch": 20.1168,"fur": 201.168,"mi": 1609.344,"lea": 4828.032}
volume = {
    # Metric (SI, in liters)
    "yl": 1e-24,"zl": 1e-21,"al": 1e-18,"fl": 1e-15,"pl": 1e-12,"nl": 1e-9,"µl": 1e-6,
    "ml": 1e-3,"cl": 1e-2,"dl": 1e-1,"l": 1.0, "dal": 1e1,"hl": 1e2,"kl": 1e3,
    # Imperial (US) → liters
    "floz_us": 0.0295735,"gill_us": 0.118294,"pt_us": 0.473176,"qt_us": 0.946353,"gal_us": 3.78541,
    # Imperial (UK) → liters
    "floz_uk": 0.0284131,"gill_uk": 0.142065,"pt_uk": 0.568261, "qt_uk": 1.13652,"gal_uk": 4.54609}
def main():
    app = Display
    app.root.mainloop()

def convert_weight(amount, old, new):
    if old.lower() == new.lower():
        return amount
    if (old in weight) and (new in weight):
        grams = amount * weight[old]
        result = grams / weight[new]
        return result
    else:
        return "input error"

def convert_length(amount, old, new):
    if old.lower() == new.lower():
        return amount
    if (old in length) and (new in length):
        meters = amount * length[old]
        result = meters / length[new]
        return result
    else:
        return "input error"

def convert_volume(amount, old, new):
    if old.lower() == new.lower():
        return amount
    if (old in volume) and (new in volume):
        liters = amount * volume[old]
        result = liters / volume[new]
        return result
    else:
        return "input error"

def convert_temperature(amount, old, new):
    if old.lower() == new.lower():
        return amount
    if old in ["C", "c"]:
        if new in ["F", "f"]:
            return amount * 9/5 +32
        elif new in ["K","k"]:
            return amount + 273.15
    elif old in ["F", "f"]:
        if new in ["C", "c"]:
            return (amount - 32) * 5/9
        elif new in ["K","k"]:
            return (amount - 32) * 5/9 + 273.15
    elif old in ["K","k"]:
        if new in ["C","c"]:
            return amount - 273.15
        elif new in ["F","f"]:
            return (amount - 273.15) * 9/5 + 32
    else:
        return "input error"

def convert_currency(amount, old, new):
    if old.lower() == new.lower():
        return amount
    if (old.upper() in currencies) and (new.upper() in currencies):
        return amount * get_currency(old.upper())[new.upper()]

def get_currency(base):
    url =f"https://api.frankfurter.app/latest?from={base}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["rates"]

def decide(amount, old, new):
    return amount

class Display:
    def init(self):
        self.root = tkinter.Tk()
        self.root.title("Quick Converter")
        self.root.attributes("-topmost", True)
        self.root.geometry("360x200")
        self.root.withdraw()

        tkinter.Label(self.root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = tkinter.Entry(self.root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        tkinter.Label(self.root, text="From unit:").grid(row=1, column=0, padx=10, pady=10)
        self.from_entry = tkinter.Entry(self.root)
        self.from_entry.grid(row=1, column=1, padx=10, pady=10)

        tkinter.Label(self.root, text="To unit:").grid(row=2, column=0, padx=10, pady=10)
        self.to_entry = tkinter.Entry(self.root)
        self.to_entry.grid(row=2, column=1, padx=10, pady=10)

        self.result_label = tkinter.Label(self.root, text="Result: --")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        convert_button = tkinter.Button(self.root, text="Convert", command=self.on_convert)
        convert_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.root.grid_columnconfigure(1, weight=1)
        self.root.bind("<Return>", lambda e: self.on_convert())

    def on_convert(self):
        amount = float(self.amount_entry.get())
        old = self.from_entry.get()
        new = self.to_entry.get()
        result = decide(amount, old, new)
        self.result_label.config(text=f"Result: {result:,.6g} {new}")


if __name__ == "__main__":
    main()