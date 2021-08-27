
def main():
    pass
edad =  int(input("Ingresa tu edad:"))
documento = str(input("¿Tienes identificación oficial?(s/n):"))
if edad >=18 and documento == "s":
    print ("Trámite de licencia concedido")
elif (edad >=18 or edad >0<18) and documento == "n":
    print ("No cumples requisitos")
elif documento != ("s" or "n") or edad < 0:
    print ("Respuesta incorrecta")
else:
    print ("No cumples requisitos")


if __name__ == '__main__':
    main()
