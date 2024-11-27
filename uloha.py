import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def main():

    try:
        count = int(entry_count.get())
    except ValueError:
        count = 50  # Default
    # Generovanie čísel
    numbers = [random.uniform(-15, 35) / 5 for _ in range(count)]

    # Počítanie kladných a záporných čísel
    positive_count = len([num for num in numbers if num > 0])
    negative_count = len([num for num in numbers if num < 0])

    # Zobraziť výsledky
    messagebox.showinfo("Výsledok", f"Počet kladných čísel: {positive_count}\n"
                                    f"Počet záporných čísel: {negative_count}")

    # Parametre pre graf
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(numbers, marker='o', linestyle='-', color='b')
    ax.axhline(0, color='red', linestyle='--', linewidth=0.8)
    ax.set_title("Graf vygenerovaných čísel")
    ax.set_xlabel("Index čísel")
    ax.set_ylabel("Hodnota")
    ax.grid(True)

    # Zobrazenie grafu v GUI
    for widget in canvas_frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    canvas.draw()

# Nastavenie hlavného okna
root = tk.Tk()
root.title("Programovacie techniky")

# Text okna
info_label = tk.Label(root, text="Programovacie techniky\n\nDaria Tronko\n\n"
                                 "Zadanie úlohy: 20. Vygenerujte pole 50 náhodných desatinných čísiel z intervalu -15 až 35, \nkaždé z nich vydeľte číslom 5, vypíšte počet záporných a kladných čísiel,\n a zobrazte graf hodnôt.", 
                                 font=("Arial", 12))
info_label.pack(pady=10)

# Zadanie voliteľneho parametra
info_label = tk.Label(root, text="Voliteľný parameter: zadajte počet čísel (štandardne 50):", font=("Arial", 12))
info_label.pack(pady=10)

# Vstupné pole pre voliteľný parameter
entry_count = tk.Entry(root, font=("Arial", 12))
entry_count.pack(pady=5)

# Tlačidlo Štart
generate_button = tk.Button(root, text="Start", command=main, font=("Arial", 12))
generate_button.pack(pady=10)

# Ram pre graf
canvas_frame = tk.Frame(root)
canvas_frame.pack(pady=10)

# Funkcia na zatvorenie programu
def on_close():
    root.destroy()
    exit()

root.protocol("WM_DELETE_WINDOW", on_close)

# Start programu
root.mainloop()
