#defino la estructura del diccionario de smartfhones

patines={
'1234PT': ['Rollerblade', 38, 'bota rígida', 80, 'aluminio', 'intermedio', 'negro con rojo', 1.6, 'trasero', 'fitness'],
'4321PT': ['Powerslide', 37, 'bota blanda', 76, 'plástico reforzado', 'principiante', 'azul marino', 1.4, 'trasero', 'fitness'],
'1111PT': ['FR Skates', 39, 'bota rígida', 90, 'aluminio', 'avanzado', 'negro mate', 1.9, 'sin freno', 'urbano'],
'1212PT': ['Oxelo', 40, 'bota blanda', 72, 'plástico', 'principiante', 'gris con verde', 1.3, 'trasero', 'fitness'],
'2121PT': ['Rollerblade', 42, 'bota rígida', 84, 'aluminio', 'intermedio', 'negro con azul', 1.7, 'intercambiable', 'urbano'],
'2222PT': ['Fila', 36, 'bota blanda', 76, 'plástico reforzado', 'principiante', 'rosa con blanco', 1.2, 'trasero', 'fitness'],
'3131PT': ['Oxelo', 41, 'bota semirrígida', 80, 'aluminio', 'intermedio', 'gris con rojo', 1.5, 'trasero', 'fitness'],
'1313PT': ['Oxelo', 40, 'bota rígida', 100, 'aluminio', 'avanzado', 'negro con dorado', 2.0, 'sin freno', 'freestyle']
}

inventario={
'1234PT': [89990,10],
'4321PT': [79990,4],
'1111PT': [139990,1],
'1212PT': [59990,13],
'2121PT': [49990,2],
'2222PT': [99990,7],
'3131PT': [119990,4],
'1313PT': [109990,5]
}

def cant_modelos_marca():
    contador=0
    marca=input("Ingrese marca que desea buscar: ")
    for lista in patines.values():
        if marca.lower() == lista[0].lower():
            contador += 1 
    # Una vez recorrido todo el diccionario verifico si se encontraron coincidencias(fuera del ciclo for)
    if contador > 0 :
        print(f" Se encontraron {contador} modelos de patines de la marca {marca.upper()}")
    else:
        print(f" No hay patines de la marca {marca.upper()}")


def cant_dispon_marca():
    contador=0
    marca=input("Ingrese marca que desea buscar: ").lower()
    
    for clave, datos in patines.items():
        if datos[0].lower() == marca:
            if clave in inventario:
                stock = inventario[clave][1]  # El segundo elemento es la cantidad disponible
                contador= stock+contador

    if contador > 0 :
        print(f"\n Total de patines disponibles de la marca {marca.title()}: {contador}")
    else:
        print(f" No existe stock para la marca {marca.title()}")



def cant_disp_talla():
    totalPatines=0
    while True:
        try:
            talla=int(input(" Ingrese talla de patines a buscar(min:30-max:50) : "))
            if 30 <= talla <=50 :        
                for clave, valor in patines.items():
                    if talla == valor[1]:
                        totalPatines += inventario[clave][1] 
                break
            else:
                print("Ingrese un valor dentro de los límites (min:30-max:50)")
        except:
            print(" Error en el ingreso de la talla de patines  ")
    #fuera del ciclo de validacion
    if totalPatines != 0:
        print(f'Hay {totalPatines} patines de la talla {talla}.')   
    else:
        print(f'No hay patines disponibles en la talla {talla}.')

def busca_por_precio():
    while True:
        try:
            preciomax=int(input(" Ingrese un precio máximo en patines: $ "))
            preciomin=int(input(" Ingrese un precio mínimo en patines: $ "))
            if preciomin < 0 or preciomax < 0 :
                raise ValueError("❌ El precio debe ser positivo.")
            if preciomin > preciomax:
                raise ValueError("❌ El precio mínimo no puede ser mayor al máximo.")

            encontrado=False
            for clave,valor in inventario.items():
                if valor[0] >= preciomin and valor[0] <= preciomax:
                    print(f'Valor Patín: ${valor[0]} - {patines[clave]}')
                    encontrado = True
            if not encontrado: 
                print('No se encontraron patines en el rango de precio ingresado.')
            break
        except ValueError as ve:
            print(ve)
        except Exception:
            print("❌ Error inesperado. Ingrese valores numéricos válidos.")
       

def busca_tamaño_ruedas():
    encontrado=False
    while True:
        try:
            diametro=int(input("Ingrese diámetro de la rueda en mm.(70 a 100) : "))
            if 70 <= diametro <= 100 :
                for lista in patines.values():
                    if diametro == lista[3]:
                        print(lista)
                        encontrado = True
                break
            else:
                print(" El diametro de la rueda debe estar dentro de los rangos mínimos (70 a 100)")
        except:
            print(" ❌ Error inesperado. Ingrese valores numéricos válidos.")

    if  not encontrado:
        print('No se encontraron patines con ese diametro de rueda.')
        
        

def actualiza_precio_stock():
    existe = True
    
    while existe:
        codigo = input('Ingrese Código: ').upper()
        if codigo in inventario:
            existe = False
        else:
            print('Código de producto NO Existe!!')

    
    newPrecio = int(input("Ingrese nuevo precio:$ "))
    inventario[codigo][0] = newPrecio
    print('Precio Actualizado')
    print(inventario[codigo][0])

    newCant = int(input("Ingrese nueva cantidad: "))
    inventario[codigo][1] = newCant
    print(inventario[codigo][1])
    print('Cantidad Actualizada')




def Menu_principal():
    while True:
        print("---***-MENU PRINCIPAL TIENDA PATINES-***---")
        print(" 1.- Cantidad de modelos por marca.")
        print(" 2.- Cantidad de patines disponibles por marca")      
        print(" 3.- Cantidad de patines disponible por talla")        
        print(" 4.- Búsqueda por rango de precio")       
        print(" 5.- Búsqueda de patines por tamaño de rueda ")
        print(" 6.- Actualizar precio y/o cantidad")       
        print(" 7.- Salir")
              
        opcion=input(" Ingrese su opcion (1 a 7): ")

        if opcion == "1":
            cant_modelos_marca()       

        elif opcion == "2":
            cant_dispon_marca()
             
        elif opcion == "3":
            cant_disp_talla()
                
        elif opcion == "4":
            busca_por_precio()

        elif opcion == "5":
            busca_tamaño_ruedas()
                
        elif opcion == "6":
            actualiza_precio_stock()                

        elif opcion == "7":
            print("Programa terminado...")
            break      
        else:
            print("Ingrese una opción válida: 1 a 7 ")  


Menu_principal()                       