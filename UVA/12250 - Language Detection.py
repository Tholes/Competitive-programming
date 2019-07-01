palabras = {"HELLO":"ENGLISH", "HOLA":"SPANISH", "HALLO": "GERMAN", "BONJOUR": "FRENCH", "CIAO": "ITALIAN", "ZDRAVSTVUJTE": "RUSSIAN"}
n = input()
contador = 0
while n != "#":
    contador += 1
    if n in palabras:
        print("Case "+repr(contador)+": " + palabras[n])
    else:
        print("Case "+repr(contador)+": " +"UNKNOWN")
    
    n = input()