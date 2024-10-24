import numpy as np
import argparse
from PIL import Image
from utils.progress_bar import progress_bar  # Importa la barra de progreso que ya tienes implementada
from utils.colores import random_color, rojo, verde, azul, reset

def filtro_erosion_maximo(imagen: Image, matriz_size=3):

    # Dimensiones de la imagen
    ancho, alto = imagen.size

    # Imagen a regresar
    nueva_imagen = imagen.copy().convert('L')

    # Imagen en tonos de gris
    imagen_tonos_gris = imagen.convert('L')
    
    # Desplazamiento
    step = matriz_size // 2

    # Calcular el número total de píxeles a procesar (excluyendo bordes)
    total_pixeles = (ancho - 2 * step) * (alto - 2 * step)
    pixeles_procesados = 0
    ultimo_porcentaje_mostrado = 0

    # Colores randoms
    color = random_color()

    # Iteramos sobre la imagen
    for x in range(step, ancho - step):
        for y in range(step, alto - step):
            bloque = imagen_tonos_gris.crop((x - step, y - step, x + step, y + step))
            # Obtenemos el maximo
            maximo = np.max(np.array(bloque).flatten())
            # Colocamos el valor mas grande
            nueva_imagen.putpixel((x,y), int(maximo))
            # Actualizamos el contador de píxeles procesados
            pixeles_procesados += 1
            # Calcular el porcentaje de progreso actual
            porcentaje_actual = (pixeles_procesados / total_pixeles) * 100
            # Mostrar el progreso solo si ha aumentado en un múltiplo de 2%
            if porcentaje_actual - ultimo_porcentaje_mostrado >= 2:
                progress_bar(pixeles_procesados, total_pixeles, color)
                ultimo_porcentaje_mostrado = porcentaje_actual
                color = random_color()

    # Mostramos el ultimo progreso 
    progress_bar(pixeles_procesados, total_pixeles, color)   
    print(verde+f"Imagen con filtro erosion maximo creada ʕ•ᴥ•ʔ"+reset)

    return nueva_imagen

def filtro_erosion_minimo(imagen: Image, matriz_size=3):

    # Dimensiones de la imagen
    ancho, alto = imagen.size

    # Imagen a regresar
    nueva_imagen = imagen.copy().convert('L')

    # Imagen en tonos de gris
    imagen_tonos_gris = imagen.convert('L')
    
    # Desplazamiento
    step = matriz_size // 2

    # Calcular el número total de píxeles a procesar (excluyendo bordes)
    total_pixeles = (ancho - 2 * step) * (alto - 2 * step)
    pixeles_procesados = 0
    ultimo_porcentaje_mostrado = 0

    # Colores randoms
    color = random_color()

    # Iteramos sobre la imagen
    for x in range(step, ancho - step):
        for y in range(step, alto - step):
            bloque = imagen_tonos_gris.crop((x - step, y - step, x + step, y + step))
            # Obtenemos el minimo
            minimo = np.min(np.array(bloque).flatten())
            # Colocamos el valor mas pequeño
            nueva_imagen.putpixel((x,y), int(minimo))
            # Actualizamos el contador de píxeles procesados
            pixeles_procesados += 1
            # Calcular el porcentaje de progreso actual
            porcentaje_actual = (pixeles_procesados / total_pixeles) * 100
            # Mostrar el progreso solo si ha aumentado en un múltiplo de 2%
            if porcentaje_actual - ultimo_porcentaje_mostrado >= 2:
                progress_bar(pixeles_procesados, total_pixeles, color)
                ultimo_porcentaje_mostrado = porcentaje_actual
                color = random_color()

    # Mostramos el ultimo progreso 
    progress_bar(pixeles_procesados, total_pixeles, color)   
    print(verde+f"Imagen con filtro erosion minimo creada ʕ•ᴥ•ʔ"+reset)
    
    return nueva_imagen

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programa que aplica el filtro erosion a una imagen")

    # Argumentos no opcionales
    parser.add_argument("imagen", help="Ruta de la imagen de entrada")
    parser.add_argument("salida", help="Ruta del archivo de salida")
    # Banderas -h (ocultar) y -r (revelar)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-max', '--max', action='store_true', help="Filtro erosion maximo")
    group.add_argument('-min', '--min', action='store_true', help="Filtro erosion minimo")

    # Argumentos opcionales (Matriz Size)
    parser.add_argument("--ms", type=int, default=3, help="Tamaño de la matriz, 3 por default")

    # Parseamos los argumentos
    args = parser.parse_args()

    # Cargamos la imagen
    imagen = None
    try:
        imagen = Image.open(args.imagen)
    except Exception as e:
        print(rojo+f"Error al cargar la imagen: {e}"+reset)
        exit()

    if args.max:
        # Aplicamos el filtro erosion maximo y la guardamos
        filtro_erosion_maximo(imagen=imagen, matriz_size=args.ms).save(args.salida)

    if args.min:
        # Aplicamos el filtro erosion minimo y la guardamos
        filtro_erosion_minimo(imagen=imagen, matriz_size=args.ms).save(args.salida)

    

    

    


