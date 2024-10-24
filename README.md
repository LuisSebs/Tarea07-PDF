# Tarea07: Filtro Erosión

<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXl0cGhud3NzZ2plYm1mZ2JleHNhdzc5d2p2NnRkOHRkY2dqaGc0NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iht1uqHE8YXwwMw52j/giphy.gif" width="240px"/>

# Dependencias

+ [Colorama](https://pypi.org/project/colorama/): `pip install colorama`
+ [Pillow](https://pypi.org/project/pillow/): `pip install pillow`
+ [Argparse](https://pypi.org/project/argparse/): `pip install argparse`

# Ejecución

Al ejecutar los ejemplos se generarán imagenes en el directorio `src/`

Para saber información sobre el programa y los parametros que acepta, ejecuta con **python** o **python3** el siguiente comando:

```bash
python3 filtro_erosion.py --help
```

## Ejemplos

### Filtro erosión máximo

**Sin especificar el tamaño de la matriz**
```bash
python3 filtro_erosion.py ./imagenes/poema.png ./poema_maximo.png -max
```

**Especificando el tamaño de la matriz**
```bash
python3 filtro_erosion.py ./imagenes/poema.png ./poema_maximo_5x5.png -max --ms 5
```

### Filtro erosión mínimo

**Sin especificar el tamaño de la matriz**
```bash
python3 filtro_erosion.py ./imagenes/poema.png ./poema_minimo.png -min
```

**Especificando el tamaño de la matriz**
```bash
python3 filtro_erosion.py ./imagenes/poema.png ./poema_minimo_5x5.png -min --ms 5
```

# Referencias:

+ [Blog de la morsa](https://la-morsa.blogspot.com/search?q=Erosi%C3%B3n)