
def eliminar():
    myDictionary = {'key1': ["Hola"]}
    quejas = str(myDictionary['key1'])
    char_to_replace = {'[': '',
                       ']': '',
                       "'": ''}
    for key, value in char_to_replace.items():
        quejas = quejas.replace(key,value)
    print(quejas)
eliminar()

