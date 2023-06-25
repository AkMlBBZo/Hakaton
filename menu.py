import tkinter as tk
from tkinter import filedialog
import shutil
import os
import main

def choose_file():
    file_path = filedialog.askopenfilename()
    shutil.copy(file_path, mypath)  # Копирование файла в mypath

def submit_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text and os.path.exists(mypath):  # Проверка наличия текста и выбранного файла
        main.main(text)


# Создание главного окна
root = tk.Tk()


mypath = os.path.abspath(__file__)
mypath = os.path.dirname(mypath) 

# Создание кнопки для выбора файла
file_button = tk.Button(root, text="Выбрать файл", command=choose_file)
file_button.pack()

# Создание текстового поля
text_entry = tk.Text(root)
text_entry.pack()

# Создание кнопки для отправки текста
submit_button = tk.Button(root, text="Отправить", command=submit_text)
submit_button.pack()

# Запуск главного цикла
root.mainloop()
