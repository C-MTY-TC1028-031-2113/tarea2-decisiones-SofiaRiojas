import math 

def main():
    # Escribe tu código abajo de esta línea
    pass
a = int(input("Da el valor de a:"))
b = int(input("Da el valor de b:"))
c = int(input("Da el valor de c:"))
if ((b**2)-4*a*c) < 0:
    print ("Raices Complejas")
elif a == 0 and b == 0:
    print ("No tiene solucion")
elif a == 0 and b != 0:
    x3 = -c/ b
    print (x3)
else:
  x1 = (-b + math.sqrt(b**2-(4*a*c))) / (2*a)
  x2 = (-b-math.sqrt((b**2-(4*a*c))))/(2*a)  
  print(x1)
  print(x2)

if __name__ == '__main__':
    main()
