import tkinter as tk
import random

form = tk.Tk()
form.config(bg='turquoise')
form.title('Password Creator')

# Pencere boyutunu al
window_width = 500
window_height = 300

# Pencereyi ortala
screen_width = form.winfo_screenwidth()
screen_height = form.winfo_screenheight()

x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

form.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
form.resizable(width=False, height=False)

etiket3 = tk.Label(text='', fg='white', bg='purple', font='Arial 11 bold')
etiket3.place(relx=0.5, rely=0.63, anchor='center')

def password_create():
    Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    password = ""
    for i in range(0, 15):
        password += random.choice(Chars)
    etiket3.config(text=password)

etiket = tk.Label(text="Şifre Oluşturucuya Hoşgeldiniz !", font='Arial 16 bold', fg='purple', bg='turquoise', anchor='center')
etiket.place(relx=0.5, rely=0.1, anchor='center')

etiket2 = tk.Label(form, text='Butona Tıklayarak Şifre Oluşturabilirsiniz', fg='black', font='Arial 11 bold', bg='turquoise')
etiket2.place(relx=0.5, rely=0.35, anchor='center')

buton = tk.Button(form, text='Şifre Oluştur', fg='white', bg='purple', command=password_create, font='Arial 11 italic bold', anchor='center')
buton.place(relx=0.5, rely=0.5, anchor='center')

form.mainloop()
