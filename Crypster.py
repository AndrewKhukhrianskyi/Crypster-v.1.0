from tkinter import *
from random import randint
from tkinter import messagebox as mb
import base64
def crypt():
    text_func = text.get(1.0, END)
    crypto = ""
    key = ''
    for i in range(len(text_func)):
        key += chr(randint(65,90))
    for i, j in enumerate(text_func):
        oper = (ord(j)+ord(key[i]))
        crypto+=chr(oper % 26 + 65)
    text.delete(1.0, END)
    text.insert(1.0, crypto)
    key_text.insert(1.0, key)
    mb.showinfo("Окошко", "Данные зашифрованы!")

        

def decrypt():
    crypto = text.get(1.0,END)
    key = key_text.get(1.0, END)
    dec = ""
    for i, j in enumerate(crypto):
        num = (ord(j) - ord(key[i % len(key)]))
        dec += chr(num % 26 + ord('A'))
    text.delete(0.0, END)
    text.insert(0.0, dec)
    key_text.delete(0.0,END)
    mb.showinfo("Окошко","Данные дешифрованы!")

def IntVar_Func():
    if var.get() == 1:
        crypt()
        
    else:
        
        decrypt()
        
def TopLevel_base_enc():
    crypt = text.get(1.0, END).encode('utf-8')
    result = base64.b64encode(crypt)
    text.delete(0.0, END)
    text.insert(0.0, result)
    

def TopLevel_base_dec():
    crypt = text.get(1.0,END).encode('utf-8')
    result = base64.b64decode(crypt) 
    text.delete(0.0, END)
    text.insert(0.0, result)
    

def yes_no():
    ans = mb.askyesno(title = "Вопрос", message = "Строка с шифром будет стерта. Вы уверены, что хотите сделать это?")
    if ans == True:
        TopLevel_base_enc()
        mb.showinfo("Окошко", "Данные закодированы!")
    else:
        pass

def yes_no2():
    ans = mb.askyesno(title = "Вопрос", message = "Строка с шифром будет стерта. Вы уверены, что хотите сделать это?")
    if ans == True:
        TopLevel_base_dec()
        mb.showinfo("Окошко", "Данные декодированы!")  
    else:
        pass

def xor():
    crypt = text.get(0.0,END)
    key_save = key_text.get(0.0, END)
    crypt = crypt+key_save
    key = randint(1,2000000)
    res = ''
    for i,j in enumerate(crypt):
        num = (ord(j) ^ key)
        res += chr(num%26 + 65)
    text.delete(0.0, END)
    text.insert(0.0, res)
    key_text.delete(0.0, END)
    key_text.insert(0.0, key)
    mb.showinfo("Окошко", "Данные заXORирилсь :)")



        
   
     
    
       
root = Tk()
mainmenu = Menu(root) 
root.config(menu=mainmenu)
root.geometry("200x200")
root.title("Crypster")
root.resizable(False,False)
var = IntVar()
var_base = IntVar()
lab_txt = Label(text = "Данные: ")
lab_txt.pack(anchor = W)
text = Text(width = 15, height = 1)
text.pack(anchor = N)
lab_key_text = Label(text = "Ключ: ")
lab_key_text.pack(anchor = W)
key_text = Text(width = 15, height = 1)
key_text.pack(anchor = N)
rb = Radiobutton(variable = var, text = "Шифровка", value = 1)
rb.pack(anchor = W)
rb_2 = Radiobutton(variable = var, text = "Дешифровка", value = 2)
rb_2.pack(anchor = W)
main_button = Button(text = "Жмяк!", command = IntVar_Func)
main_button.pack(anchor = S)
base_menu = Menu(mainmenu, tearoff=0)
base_menu.add_command(label ="BASE Кодировка", command = yes_no)
base_menu.add_command(label ="BASE Декодирование", command = yes_no2)
base_menu.add_command(label ="XOR Шифрование", command = xor)
mainmenu.add_cascade(label = "Опции", menu = base_menu)



root.mainloop()


