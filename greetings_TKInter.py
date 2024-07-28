# Задача:
# Напишите программу на Python с использованием модуля tkinter, 
# которая позволяет пользователю ввести свое имя в окно ввода, 
# а затем выводит на экран сообщение "Привет, [имя]!".

import tkinter as tk

root=tk.Tk()
root.title ("Приветствие")

greet_label = tk.Label(root, text="Привет! Напиши, как тебя зовут.")
greet_label.pack()

entry=tk.Entry(root, text=" ")
entry.pack()

def display_name():
    name= entry.get()
    label.config (text = f"Hello, {name}! Приятно познакомиться :) ")


salut_button = tk.Button(root, text="Представиться", command=display_name)
salut_button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
