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
'1234PT': [89990, 10],
'4321PT': [79990, 4],
'1111PT': [139990, 1],
'1212PT': [59990, 13],
'2121PT': [49990, 22],
'2222PT': [99990, 7],
'3131PT': [119990, 4],
'1313PT': [109990, 5]
}

def cant_modelos_marca():
    pass

def cant_dispon_marca():
    pass

def cant_disp_talla():
    pass

def busca_por_precio():
    pass

def busca_tamaño_ruedas():
    pass

def actualiza_precio_stock():
    pass




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