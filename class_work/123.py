import tkinter as tk
import win32print
import win32ui


def print_text(mass, expiration):
    printer_name = win32print.GetDefaultPrinter()
    hprinter = win32print.OpenPrinter(printer_name)
    printer_info = win32print.GetPrinter(hprinter, 2)

    printer_handle = win32ui.CreateDC()
    printer_handle.CreatePrinterDC(printer_name)
    printer_handle.StartDoc('PrintDoc')
    printer_handle.StartPage()

    x = 100  # Горизонтальная позиция для текста
    y = 100  # Вертикальная позиция для текста

    text = f"Масса товара: {mass} г\nСрок годности: {expiration} дней"

    for line in text.split('\n'):
        printer_handle.TextOut(x, y, line)
        y += 20  # Переместиться на следующую строку (20 - это произвольное расстояние между строками)

    printer_handle.EndPage()
    printer_handle.EndDoc()
    printer_handle.DeleteDC()


def submit():
    mass = mass_entry.get()
    expiration = expiration_entry.get()
    copies = int(copies_entry.get())

    for _ in range(copies):
        print_text(mass, expiration)


# Создаем главное окно
root = tk.Tk()
root.title("Пример программы с GUI")

# Создаем и настраиваем элементы интерфейса
mass_label = tk.Label(root, text="Масса товара (г):")
mass_label.pack()
mass_entry = tk.Entry(root)
mass_entry.pack()

expiration_label = tk.Label(root, text="Срок годности (дней):")
expiration_label.pack()
expiration_entry = tk.Entry(root)
expiration_entry.pack()

copies_label = tk.Label(root, text="Количество копий:")
copies_label.pack()
copies_entry = tk.Entry(root)
copies_entry.pack()

submit_button = tk.Button(root, text="Печать", command=submit)
submit_button.pack()

# Запуск главного цикла программы
root.mainloop()
