def descuento(total:float) -> float:
    if total > 50000:
        total = total * 0.90
    return total 

def calcular_compra(cantidad_productos:int) -> float:
    total = 0.0
    cantidad_caros = 0
    maximo_precio = 0.0

    for i in range(cantidad_productos):
        precio = 0.0
        while precio < 1 or precio > 100000:
            entrada_precio = input(f"Ingrese el precio del producto {i+1} (entre 1 y 100000):")

            try:
                precio = float(entrada_precio)
                if precio < 1 or precio > 100000:
                    print("precio fuera de rango. intente de nuevo.")
            except ValueError:
                print("Valor no valido. Introdusca un numero.")

    total += precio
    
    if precio > 10000:
        cantidad_caros += 1
    
    if precio > maximo_precio:
        maximo_precio = precio 
    
    importe_final = descuento(total)

    print(f"El precio mas alto es: {maximo_precio}")
    print(f"Productos que superan los $10.000: {cantidad_caros}")
    print(f"El importe total acumulado es: {total}")
    print(f"El importe fianl a pagar es: {importe_final}")

    return importe_final