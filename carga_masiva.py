import pandas as pd
from preprocesamiento import *

#Formato fecha para normalizar todas las fechas registradas en el IEEH
formato = '%d/%m/%Y %H:%M'

#Nombre archivo con registros IEEH
archivo = 'IEEH.xlsx'
largo= 10
identificador_hospital = 'HMET'
identificador_episodio = 'H'
codigo_ss = '110'

#Leer tabla y convertir en dataframe
IEEH = pd.read_excel(archivo)

#Se define tipo de actividad hospitalizados y estado de codificación
IEEH['TIPO_ACTIVIDAD'] = 1
IEEH['ESTADO'] = 1
IEEH['CUMPLIMENTACION'] = 1

#Es necesario utilizar la siguiente función para agregar correlativos y moldear número de ficha al igual que el HIS utilizado
normalize_nro_ficha(IEEH,largo,identificador_hospital)
#Es necesario utilizar la siguiente función para agregar correlativos y moldear número de episodio al igual que el HIS utilizado
normalize_nro_episodio(IEEH,largo,identificador_episodio)
#Es necesario utlizar la siguiente función para normalizar la fecha de nacimiento del paciente al formato establecido por TeamCoder
normalize_fecha_nac(IEEH,formato)
#Es necesario utlizar la siguiente función para normalizar el sexo del paciente al formato establecido por TeamCoder
normalize_sexo(IEEH)
#Es necesario utlizar la siguiente función para normalizar la fecha de ingreso del paciente al formato establecido por TeamCoder
normalize_fecha_ingreso(IEEH,formato)
#Es necesario normalizar el tipo de ingreso (no considera ingresos obstetricos)
normalize_tipo_ingreso(IEEH)
#Es necesario normalizar la previsión de los pacientes al formato establecido en TeamCoder
normalize_prev(IEEH)
#Es necesario obtener y normalizar el formato de la provincia de procedencia
IEEH = normalize_provincia(IEEH)
#Es necesario utlizar la siguiente función para normalizar la fecha de egreso del paciente al formato establecido por TeamCoder
IEEH = normalize_fecha_egreso(IEEH,formato)
#Es necesario normalizar el destino al alta a la codificación de TeamCoder
normalize_destino_alta(IEEH)
#Es necesario normalizar los rut de médicos al formato establecido en TeamCoder
normalize_rut_med(IEEH)
#Es necesario normalizar los rut de pacientes al formato establecido en TeamCoder
normalize_rut_pac(IEEH)
#Es necesario normalizar la procedencia a la codificación impuesta por Sigesa
normalize_procedencia(IEEH,codigo_ss)
#Es necesario utlizar la siguiente función para normalizar las fechas de traslado del paciente al formato establecido por TeamCoder
normalize_fechas_traslado(IEEH, formato)
#Es necesario utilizar la siguiente función para normalizar las leyes previsionales del IEEH a la codificación de TeamCoder
normalize_ley_prev(IEEH)
#Es necesario normalizar y estandarizar las especialidades al formato exigido 
normalize_especialidad(IEEH)
#Es necesario normalizar el tipo de ocupación
normalize_tipo_ocp(IEEH)
#Es necesario normalizar la glosa ocupacional al formato exigido
normalize_glos_ocp(IEEH)
#Es necesario normalizar la etnia del paciente
normalize_etnia(IEEH)
#Es necesario convertir en número el código del hospital de referencia
normalize_cod_hosp(IEEH)
#Es necesario normalizar el código de cada unidad funcional
normalize_uf(IEEH)

IEEH = IEEH.replace('nan','')

GRD = estructura_grd(IEEH)

GRD.to_csv('altas_grd.txt', sep='|', index=False)