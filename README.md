# carga_cmbd_grd
Script para generar archivo .txt de carga de datos demográficos y traslados de pacientes hospitalizados de TeamCoder, desde BBDD IEEH.

## Instalación

Es necesario contar con instalación de python 3.7 y realizar los siguientes pasos para el correcto funcionamiento.

**Extracción de repositorio**

```
git clone https://github.com/vhevia11/carga_cmbd_grd.git
```

## Requerimientos

**Numpy**

```
pip install numpy
```

**Pandas**
```
pip install pandas
```

## Ejecución del programa

Para ejecutar el programa es necesario abrir la terminal, ingresar a la carpeta donde está alojado el proyecto y ejecutar la siguiente línea:

```
python carga_masiva.py
```
## Outputs

En la misma carpeta se generará un archivo .txt llamdo "altas_grd", el cual contendrá la estandarización y normalización de cada una de las variables alojadas en la BBDD IEEH, para ahora ser cargado directamente en la interfaz de TeamCoder.
