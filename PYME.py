baseDeDatos = {"users": ["admin"], "passwords": ["admin1"]}
import os
import pyautogui
import time
import datetime as dt
from prettytable import PrettyTable
itemsDataBase = [[]]
dummyItemsDataBase = [[]]
contadorPrettyTable = 0
deleteWhile = 0
myTable = PrettyTable(['nombre del producto'.upper(),'product code'.upper(),'precio del producto'.upper(),'la cantidad disponible'.upper()])
#Primer menu para elegir que opcion desea el usuario
def PrimerMenu():
    i = True
    while i == True:
        x = int(input("Elija una opcion 1-Registrarse, 2- Iniciar Sesion, 3- Salir"))
        if x == 1:
            userRegister()
        elif x == 2:
            userLogin()
        elif x == 3:
            i = False
        else:
            print("Elija la opcion correcta")

def salir():
    print("Hasta luego")

def userRegister():
    global baseDeDatos
    usersRegister = input("Ingrese su nombre de usuario")
    baseDeDatos["users"].append(usersRegister)
    passwordRegister = input("ingrese su password")
    baseDeDatos["passwords"].append(passwordRegister)
    with open('dataBase.txt', 'w') as wf:
        writeUser = wf.write(''.join(baseDeDatos["users"]))
        writePassword = wf.write(''.join(baseDeDatos["passwords"]))
        print("Usuarios: ", baseDeDatos["users"], "Contrasenhas: ", baseDeDatos["passwords"])
    return writeUser and writePassword

def userLogin():
    #llama a la base de datos
    global baseDeDatos
    #solicita la informacion para el login
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
        inventarioMenu()
    for verify in range (len(baseDeDatos["users"])):
        # en este if lo que se hace es validar si los datos ingresados por el cliente son correctos
        if userLog == baseDeDatos["users"][verify] and passwordLog == baseDeDatos["passwords"][verify]:
            print("Inicio sesion correctamente")
        elif userLog != baseDeDatos["users"][verify] and passwordLog != baseDeDatos["passwords"][verify]:
            print("Datos incorrectos, intentelo nuevamente")

def readDataBase():
    with open('database.txt', 'r') as rf:
        read_f = rf.read().split()
        return read_f

def main():
    PrimerMenu()
    readDataBase()
    print(readDataBase())

def if_integer(string):
    if string[0] == ('-', '+'):
        return string[1:].isdigit()

    else:
        return string.isdigit()
def inventarioMenu():
    opcionInventario = int(input('\t'.expandtabs(40) + '<-----Choose an option----->'
                                                       '\n1-Add new item\n2-Modify existing item\n3-Delete an item\n4-Salir e imprimir reporte\n'))
    if opcionInventario == 1:
        inventarioAddItems()
    if opcionInventario == 2:
        inventarioModifyItem()
    if opcionInventario == 3:
        inventarioDeleteItem()
    if opcionInventario == 4:
         txtInventario()


def inventarioAddItems():
        global dummyItemsDataBase
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.5)
        global contadorPrettyTable
        contadorPrettyTable = 0
        dummyVariable = True
        global itemsDataBase
        dummyWhile = True
        requiredData  = ['nombre del producto'.upper(),'product code'.upper(),'precio del producto'.upper(),'la cantidad disponible'.upper()]
        print('\n\t'.expandtabs(18) + '<-----Para agregar un nuevo item, favor ingresar los siguientes datos----->\n')
        while dummyVariable == True:
            j = (len(itemsDataBase)-1)
            for i in range(4):
                productName = input('\n' + requiredData[i] + '\n')
                if i == 2 or i ==3:
                    if if_integer(productName) == False:
                        print(requiredData[i] + ' DEBE SER UN NUMERO')
                        itemsDataBase.remove(itemsDataBase[len(itemsDataBase)-1])
                        itemsDataBase.append([])
                        if itemsDataBase == []:
                            itemsDataBase = [[]]

                        inventarioAddItems()
                itemsDataBase[j].append(productName)
                if len(itemsDataBase) >1:  ##Lo malo de esta validacion es que no evalua el primer array XD pero bueno me da igual y literal no la entiendo como la hice
                    for k in range(len(itemsDataBase)-1):
                        print(k)
                        if productName in itemsDataBase[k][1]:
                            print(productName)
                            print(
                                'Product code must be unique and cannot be repeated in any array, pls try it again')
                            itemsDataBase.remove(itemsDataBase[k + 1])
                            itemsDataBase.append([])
                            inventarioAddItems()

            time.sleep(0.1)

            pyautogui.hotkey('ctrl', 'l')

            addMore = input(
                '\n\t'.expandtabs(30) + 'Si desea add more items, favor escriba "confirmar"''\n\t'.expandtabs(
                    35) + 'Para elegir otra opcion, escriba "terminar"\n\t'.expandtabs(54)).upper()
            if addMore == 'CONFIRMAR':
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'l')
                dummyItemsDataBase.clear()
                itemsDataBase.append([])
                dummyItemsDataBase = itemsDataBase.copy()
                contador = len(itemsDataBase)
                for k in range(len(itemsDataBase)):
                    if itemsDataBase[k] == []:
                        print('Hola')

                        realLength = len(itemsDataBase) - k

                contadorPrettyTable = contador - realLength


                print('Ok... continuemos')
            elif addMore == 'TERMINAR':
                itemsDataBase.append([])
                dummyItemsDataBase.clear()
                dummyItemsDataBase = itemsDataBase.copy()
                contadorTerminar = len(itemsDataBase)
                disminuyoYo = 0
                for t in range(len(itemsDataBase)):
                    if itemsDataBase[t] == []:

                        disminuyoYo = len(itemsDataBase) - t

                contadorPrettyTable = contadorTerminar - disminuyoYo

                pyautogui.hotkey('ctrl', 'l')
                time.sleep(1)
                miTablaBonita()
                inventarioMenu()
                return itemsDataBase
                dummyVariable = False


def txtInventario():
    global myTable
    with open('baseDatos.txt', 'r+') as itemTxt:
        itemTxt.write('\t'.expandtabs(30) + '<---Registro inventario--->\n' + '\t'.expandtabs(34) + str(
            dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        writinMyTable = str(myTable)
        itemTxt.write('\n'+writinMyTable)
        itemTxt.read()
    #         len(requiredData)):  # Estuve un buen rato intentando hacer una tabla bonita con mi esfuerzo,pero, la verdad es que perdi mucho tiempo y prefiero descargar una libreria y ya esta XD.
    #     print(str(requiredData[i]), end="\t".expandtabs(5) + '|' + "\t".expandtabs(5))
    #     contador += 1
    #     if contador == 4:
    #         print("\n".__reduce__(5))
    #         for palosHorizontales in range(10):
    #             print("-", end="")
    #         print("\n")
    #         for palosVerticales in range(4):
    #             print('\t'.expandtabs(24) + "|", end="")
    # print('\n')
    # for i2 in range(len(itemsDataBase)):
    #     for j in range(len(itemsDataBase[i2])):
    #         print(str(itemsDataBase[i2][j]), end="\t".expandtabs(30))
    #


def miTablaBonita():

    global myTable
    global contadorPrettyTable
    theRow = []

    global itemsDataBase
    global dummyItemsDataBase
    dummyItemsDataBase.clear()
    dummyItemsDataBase = itemsDataBase.copy()
    myTable = PrettyTable(
        ['nombre del producto'.upper(), 'product code'.upper(), 'precio del producto'.upper(),
         'la cantidad disponible'.upper()])


    if itemsDataBase ==[[]]:
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(2)
        print('Actualmente la lista esta vacia, favor primero ingrese datos')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'l')
        inventarioMenu()
    for k in range(contadorPrettyTable):
        for i in range(len(dummyItemsDataBase)):
            for j in range(len(dummyItemsDataBase[i])):
                theRow.append(dummyItemsDataBase[i][j])
        myTable.add_row([theRow[0], theRow[1], theRow[2], theRow[3]])
        theRow.clear()
        dummyItemsDataBase.remove(dummyItemsDataBase[0])
        # contadorPrettyTable = 0


    return myTable
def inventarioModifyItem():
    global dummyItemsDataBase
    global itemsDataBase
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    modifyWhile = True
    while modifyWhile == True:
        if itemsDataBase == [[]]:
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(2)
            print('\n\t'.expandtabs(35) + 'Actualmente la lista esta vacia, favor primero ingrese datos')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'l')
            break
        print('\n\t'.expandtabs(30) + 'El inventario actual es el siguiente\n' + str(myTable))
        modifyItem = int(input('Que fila desea modificar'))
        pyautogui.hotkey('ctrl', 'l')
        try:
            selecValue = int(input('\n\t'.expandtabs(
                35) + 'Que desea modificar\n1-NOMBRE DEL PRODUCTO\n2-PRODUCT CODE\n3-PRECIO DEL PRODUCTO\n4-LA CANTIDAD DISPONIBLE'))
            if selecValue > 4:
                print('Deber ser una opcion menor a 4')
                pyautogui.hotkey('ctrl,', 'l')
            for t in range(len(itemsDataBase)):
                if itemsDataBase[t] == []:
                    print('Hola')
                    disminuyoYo = len(itemsDataBase) - t
                    print('Soy el disminuyo yo', disminuyoYo)
            print('Ubicacion lista', itemsDataBase[modifyItem - disminuyoYo][selecValue - 1])
            pyautogui.hotkey('ctrl', 'l')
            newValue = input('Seleccione el nuevo valor')
            if selecValue == 2:
                print('Entre')
                for m in range(len(itemsDataBase) - 1):
                    if newValue == itemsDataBase[m][1]:
                        print('Recuerde que no puede copiar product codes\n\nFavor intentelo nuevamente')
                        inventarioModifyItem()
            itemsDataBase[modifyItem - disminuyoYo].pop(selecValue - 1)
            itemsDataBase[modifyItem - disminuyoYo].insert(selecValue - 1, newValue)
            pyautogui.hotkey('ctrl', 'l')
            print(itemsDataBase)
            goOrStop = int(input('Click 1 to continue\n' + 'Click 2 to finish'))
        except Exception as e:
            print(e)
        if goOrStop == 2:
            dummyItemsDataBase.clear()
            dummyItemsDataBase = itemsDataBase.copy()

            modifyWhile = False
            print(dummyItemsDataBase)

    miTablaBonita()
    inventarioMenu()


def inventarioDeleteItem():
    contadorDelete = 0
    global dummyItemsDataBase
    global contadorPrettyTable
    global myTable
    global itemsDataBase
    global deleteWhile
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0)
    deleteWhile = True
    while deleteWhile:
        if itemsDataBase == [[]]:
            print('Actualmente la lista esta vacia')
            break
        print('\t'.expandtabs(25) + 'El inventario actual es el siguiente\n', myTable)
        lineaEliminar = input('\t'.expandtabs(25) + "Indique el codigo del producto que desea eliminar")
        for i in range(len(itemsDataBase)):
            if lineaEliminar in itemsDataBase[i][1]:
                theRowThatWnt = itemsDataBase.index(itemsDataBase[i])
                myTable.del_row(theRowThatWnt)
                itemsDataBase.remove(itemsDataBase[i])
                break
        if len(itemsDataBase) == 1:
            itemsDataBase.append([])
            # dummyItemsDataBase.remove(itemsDataBase[i])
            # dummyItemsDataBase.append([])
            contadorDelete += 1
        if itemsDataBase == [] or itemsDataBase == [[], []]:
            itemsDataBase = [[]]

            print(itemsDataBase)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(1)
        print(dummyItemsDataBase)
        print('Informacion del inventario actual\n' + str(myTable))

        goOrStop = int(input('Click 1 to continue\n' + 'Click 2 to finish'))
        if goOrStop == 2:
            dummyItemsDataBase.clear()
            dummyItemsDataBase = itemsDataBase.copy()
            print('Si entre go or stop')
            deleteWhile = False




    print(deleteWhile)
    print('Inventario menU')
    inventarioMenu()


main()
print(baseDeDatos)
