import sys
sys.path.append("gen-py")
from Calc import CalculatorService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

puerto = 9090

transporte = TSocket.TSocket('localhost', puerto)
transporte = TTransport.TBufferedTransport(transporte)
protocolo = TBinaryProtocol.TBinaryProtocol(transporte)

cliente = CalculatorService.Client(protocolo)

# Abrir el transporte para conectarse con el servidor
transporte.open()

opcion = 0
while True:

    n1 = int(input("Introduce tu primer número: ") )
    n2 = int(input("Introduce tu segundo número: ") )

    print("""
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los dos números
    5) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",cliente.sumar(n1,n2))
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de",n1,"-",n2,"es igual a",cliente.restar(n1,n2))
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de",n1,"*",n2,"es igual a",cliente.multiplicar(n1,n2))
    elif opcion == 4:
        print(" ")
        print("RESULTADO: Al dividir",n1,"entre",n2,"es igual a",cliente.dividir(n1,n2))
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")

# Cerrar la conexión
transporte.close()