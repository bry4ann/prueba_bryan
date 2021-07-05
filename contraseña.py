#Un password seguro es el que contiene letras, números, más de 6 caracteres y un símbolo 
password = input("Ingrese una contraseña: ") # 
val_1 = False # números 
val_2 = False # letras  
val_3 = False # Caracter no alfanumérico 
largo = 0
#.     HolaMundo2
for letra in password:
  if letra.isnumeric() == True: # Que contenga número 
    val_1 = True
  if letra.isalpha() == True: # Que contenga letras 
    val_2 = True 
  if letra.isalnum() == False: # Que contenga símbolos 
    val_3 = True #La única forma que eso sea falso, es cuando es un carácter distinto a letras y números por tal razón estamos cumpliendo con la restricción
  largo = largo +1

if val_1 == True and val_2 == True and val_3 == True and largo >= 6: #si se cumple todas las restricciones 
  print("Password válido", val_1, val_2,val_3, largo)
else: 
  print("Password inválido", val_1, val_2,val_3, largo)