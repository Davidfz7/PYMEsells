baseDeDatos = {"users": ["admin"], "passwords": ["admin1"]}
import os
import time
import pyautogui
from prettytable import PrettyTable
actualUser = 0
reclamos = {}
quantReclamos = 0
def PrimerMenu():
    x = int(input("Elija una opcion 1-Registrarse, 2- Iniciar Sesion, 3- Salir"))
    if x == 1:
        userRegister()
    if x == 2:
        userLogin()
    if x == 3:
        print('Adios')
    if x > 3:
        print('Solo hay 3 opciones XD, elija otra vez')
        PrimerMenu()


def salir():
    print("Hasta luego")

def userRegister():
    global baseDeDatos
    usersRegister = input("Ingrese su nombre de usuario")

    for verify in range (len(baseDeDatos["users"])):
        # en este if lo que se hace es validar si los datos ingresados por el cliente son correctos
        if usersRegister == baseDeDatos["users"][verify]:
            print("Ya existe este usuario, favor intentelo con un usuario diferente")
            pyautogui.hotkey('ctrl','l')
            PrimerMenu()
    baseDeDatos["users"].append(usersRegister)
    passwordRegister = input("ingrese su password")
    baseDeDatos["passwords"].append(passwordRegister)
    PrimerMenu()
def userLogin():
    global actualUser
    #llama a la base de datos
    global baseDeDatos
    #solicita la informacion para el login
    isIN = False
    userLog = input("Ingrese su nombre de usuario para iniciar sesion")
    passwordLog = input("ingrese su password para iniciar sesion")
    # el for lo que hace es correr el programa dependiendo de la cantidad de datos que hayan en los []
    if userLog == baseDeDatos["users"][0] and passwordLog == baseDeDatos["passwords"][0]:
        pyautogui.hotkey('ctrl', 'l')
        for i in range(3):
            time.sleep(0.5)
            print('.', end='')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','l')
        print('\n\t'.expandtabs(32)+'Inicio sesión como administrador correctamente')
        actualUser = baseDeDatos["users"][0]
        menuAdministrador()
    for verify in range (len(baseDeDatos["users"])):
        # en este if lo que se hace es validar si los datos ingresados por el cliente son correctos
        if userLog == baseDeDatos["users"][verify] and passwordLog == baseDeDatos["passwords"][verify]:
            print("Inicio sesion correctamente")
            print('Bienvenido', baseDeDatos["users"][verify])
            actualUser = baseDeDatos["users"][verify]
            pyautogui.hotkey('ctrl','l')
            isIN = True

    if isIN == True:
        menuCliente()
    if isIN == False:
        pyautogui.hotkey('ctrl','l')
        for i in range(3):
            time.sleep(0.5)
            print('.', end='')

        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'l')
        print('No existe esta cuenta')
        time.sleep(1.5)
        pyautogui.hotkey('ctrl', 'l')
        PrimerMenu()
def reclamosClientes():
    global quantReclamos
    global actualUser
    global reclamos
    pyautogui.hotkey('ctrl','l')
    keepGoin = True
    while keepGoin == True:
        if actualUser in reclamos:
            queja = input('Favor indique cual es su queja')
            reclamos[actualUser].append(queja)
            quantReclamos += 1
        else:
            queja = input('Favor indique cual es su queja')
            reclamos.update({actualUser: []})
            reclamos[actualUser].append(queja)
            quantReclamos += 1
        stop = input('Desea hacer mas quejas?')
        if stop == 'no':
            keepGoin = False
            print(reclamos)
            menuCliente()
def menuCliente():
    global actualUser
    selec = int(input('Que desea hacer?\n1-Ver inventario de productos\n2-Realizar una queja\n3-Log out'))
    if selec == 2:
        reclamosClientes()
    if selec == 3:
        tablaQuejas()
        actualUser = 0
        PrimerMenu()
def menuAdministrador():
    global actualUser
    selec = int(input('Bienvenido al menu de administrador, que desea realizar\n1-Opciones de inventario\n2-Reportes Generales\n3-Reclamos\n4-Cerrar sesion'))
    if selec == 3:
        tablaQuejas()
    if selec == 4:
        actualUser = 0
        PrimerMenu()

def tablaQuejas():
    global quantReclamos
    print('\t'.expandtabs(30)+'Quejas de los clientes')
    my_quejas_table = PrettyTable()
    my_quejas_table.add_column('Nombre del cliente', [actualUser])
    my_quejas_table.add_column('Comentarios: ', [eliminarChar(str(reclamos[actualUser]))])
    my_quejas_table.add_column('Cantidad de quejas realizadas: ', str(quantReclamos))
    print(my_quejas_table)

def eliminarChar(comentarios):
    global reclamos
    char_to_replace = {'[': '',
                       ']': '',
                       "'": ''}
    for key, value in char_to_replace.items():
        comentarios = comentarios.replace(key,value)
    return comentarios

PrimerMenu()