sectores=["centro", "colina", "industria"]
def registrar_pedido(pedidos):
    nombre= input("Ingrese su nombre y apellido:  ")
    direccion= input("ingrese direccion: ")
    sector=input("ingrese el sector: ").lower
    while sector not in sectores:
        print("ingrese una comuna valida")
        sector=input("ingrse su sector: ").lower
    while True:
        try:
            cilindro_5kg=int(input("Ingrese cantidad de cilindros: "))
            cilindro_15kg=int(input("ingrese cantidad de cilindros: "))
            cilindro_45kg=int(input("ingrese cantidad de cilindros: "))
        except:
            print("ingrese un cilindro valido")
        else:
            break
    pedidos.append ({
        "nombre":nombre,
        "direccion": direccion,
        "sector": sector,
        "cilindro_5kg":cilindro_5kg,
        "cilindro_15kg": cilindro_15kg,
        "cilindro_45kg": cilindro_45kg
    })
    print("su pedido ha sido ingresado con exito")


def listar_pedidos (pedidos):
    for pedido in pedidos:
        print(pedido)

def imprimir_pedidos (pedidos):
    import csv
    import json
    comuna_seleccion= input("ingrese la comuna que desea imprimir o aprete enter para imprimir todos ")
    if comuna_seleccion=="":
        nombre_archivo="planilla_todos.txt"
    elif comuna_seleccion==sectores:
        lista_comunas=[]
        for pedido in pedidos:
            if pedidos["sector"]:comuna_seleccion
            lista_comunas.append (pedido)
            nombre_archivo=f"planilla_{comuna_seleccion}.txt"
        else:
            print("ingrese un sector valido")
            return
    with open ("nombre_archivo", "w") as archivo:
        for pedido in lista_comunas:
            archivo.write(f"Nombre y apellido {pedido["nombre"]}\n")
            archivo.write(f"direccion {pedido["direccion"]}\n")
            archivo.write(f"sector{pedido["sector"]}\n")
            archivo.write(f"cilindro_5kg{pedido ["cilindro_5kg"]}\n")
            archivo.write(f"cilindro_15kg{pedido ["cilindro_15kg"]}\n")
            archivo.write(f"cilindro_45kg{pedido ["cilindro_45kg"]}\n")

    with open (f"{nombre_archivo}.csv", "w", newline="") as archivo:
        for pedido in lista_comunas:
            escritor=csv.writer(archivo)
            escritor.writerow(["nombre y apellido", "direccion", "sector", "cilindro_5kg", "cilindro_15kg", "cilindro_45kg"])
            escritor.writerow(pedido["nombre"])
            escritor.writerow(pedido["direccion"])
            escritor.writerow(pedido["sector"])
            escritor.writerow(pedido["cilindro_5kg"])
            escritor.writerow(pedido["cilindro_15kg"])
            escritor.writerow(pedido["cilindro_45kg"])

    with open (f"{nombre_archivo}.json", "w") as archivo:
        json.dump (pedidos, archivo)

 



