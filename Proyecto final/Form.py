from tkinter import *

# Manipulacion de datos del registro
def send_data():
  username_info = username.get()
  password_info = password.get()
  fullname_info = fullname.get()
  age_info = str(age.get())
  print(username_info,"\t", password_info,"\t", fullname_info,"\t", age_info)
 
#  Abrir y escribir datos en un archivo
  file = open("user.txt", "a")
  file.write(username_info)
  file.write("\t")
  file.write(password_info)
  file.write("\t")
  file.write(fullname_info)
  file.write("\t")
  file.write(age_info)
  file.write("\t\n")
  file.close()
  print(" Nuevo usuario registrado. Usuario: {} | Nombre completo: {}   ".format(username_info, fullname_info))
 
#  Eliminar datos del evento anterior
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  fullname_entry.delete(0, END)
  age_entry.delete(0, END)

# Crear nueva instancia
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Formulario")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "Formulario | Gomez de Jesus y Retamozo", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()

# Definir campos de etiquetas
username_label = Label(text = "Nombre de usuario", bg = "#FFEEDD")
username_label.place(x = 22, y = 70)
password_label = Label(text = "Contraseña", bg = "#FFEEDD")
password_label.place(x = 22, y = 130)
fullname_label = Label(text = "Nombre completo", bg = "#FFEEDD")
fullname_label.place(x = 22, y = 190)
age_label = Label(text = "edad", bg = "#FFEEDD")
age_label.place(x = 22, y = 250)
 
# Obtener y almacenar datos de los usuarios
username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()
 
username_entry = Entry(textvariable = username, width = "40")
password_entry = Entry(textvariable = password, width = "40",  show = "*")
fullname_entry = Entry(textvariable = fullname, width = "40")
age_entry = Entry(textvariable = age, width = "40")
 
username_entry.place(x = 22, y = 100)
password_entry.place(x = 22, y = 160)
fullname_entry.place(x = 22, y = 220)
age_entry.place(x = 22, y = 280)
 
# Submit Button
submit_btn = Button(mywindow,text = "Guardar info", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 320)

mywindow.mainloop()
