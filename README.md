# Capstone GitFlow Test
Repositorio de evaluación diagnóstica de GitFlow de Fernando Balladares C.

## Versión
Python 3.9.x

## Requisitos
Para ejecutar el programa se requieren las siguientes librerías:

* Pandas
* NumPy

### Dataset
Para ejecutar el programa también se necesita el [dataset utilizado](https://www.kaggle.com/datasets/prathamsharma123/farmers-protest-tweets-dataset-raw-json?resource=download) (JSON).

## Ejecución
El archivo principal a ejecutar es `main.py`:
```
python main.py
```

## Parámetros
En la sección de parámetros del archivo `parameters.py` se pueden configurar los siguientes parámetros:

* `DATA_PATH`: Indica la ruta del archivo JSON con los datos.
* `WAITING_TIME`: Indica el tiempo de espera antes de poder volver a ingresar otra opción en el menú principal.
* `VALID_OPTIONS`: Indica la lista de opciones válidas de acuerdo a las funciones disponibles.
* `EXIT_OPTION`: Indica la opción que se utilizará para terminar el programa en el menú principal. **NOTA:** Esta opción también debe estar incluida en `VALID_OPTIONS`.