import funciones as fn
pedidos= []

while True:
    try:
        print("Bienvenido al sistema de pedidos Gaxplosive")
        print("*******************************************")
        print("1. Registrar pedido ")
        print("2. listar todos los pedidos ")
        print("3. Imprimir hoja de ruta")
        print("4. salir del programa ")

        opc= input("ingrese su opcion: ")

        if opc ==1:
            fn.registrar_pedido(pedidos)
        elif opc == 2:
            fn.listar_pedidos(pedidos)
        elif opc==3:
            fn.Imprimir_ruta(pedidos)
        elif opc==4:
            break
    except ValueError:
        print ("ingrese una opcion valida")
        