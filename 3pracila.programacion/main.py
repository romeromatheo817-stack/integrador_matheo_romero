from parcial import  *
entrada = input("Ingrese la cantidad de productos que se cargaran: ")
try: 
    cantidad = int(entrada)
    if cantidad > 0:
        resultado_final = calcular_compra(cantidad)
    else:
        print("La cantidad de productos debe ser mayor a 0.")
except ValueError:
    print("Por favor, ingrese un numero entero valido.")