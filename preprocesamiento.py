import pandas as pd
import numpy as np

def normalize_nro_ficha(IEEH, largo, identificador_hospital):
    IEEH['FICHA'] = IEEH['FICHA'].astype(str)
    IEEH['FICHA'] = IEEH['FICHA'].str.zfill(largo)
    IEEH['FICHA'] = str(identificador_hospital)+IEEH['FICHA'].astype(str)
    return (IEEH)

def normalize_nro_episodio(IEEH,largo,identificador_episodio):
    IEEH['NUM_ADM'] = IEEH['NUM_ADM'].astype(str)
    IEEH['NUM_ADM'] = IEEH['NUM_ADM'].str.zfill(largo)
    IEEH['NUM_ADM'] = str(identificador_episodio)+IEEH['NUM_ADM'].astype(str)
    return (IEEH)

def normalize_fecha_nac(IEEH, formato):
    IEEH['FECHA_NAC'] = IEEH['D_NAC'].astype(str)+'/'+IEEH['M_NAC'].astype(str)+'/'+IEEH['A_NAC'].astype(str)
    IEEH['FECHA_NAC'] =  pd.to_datetime(IEEH['FECHA_NAC']).dt.strftime(formato)
    return (IEEH)

def normalize_sexo(IEEH):
    IEEH.loc[IEEH['SEXO'] == 1, 'SEXO'] = '01'
    IEEH.loc[IEEH['SEXO'] == 2, 'SEXO'] = '02'
    IEEH.loc[IEEH['SEXO'] == 3, 'SEXO'] = '03'
    return (IEEH)

def normalize_fecha_ingreso(IEEH,formato):
    IEEH['FECHA_ING'] = IEEH['DIA_ING'].astype(str)+'/'+IEEH['MES_ING'].astype(str)+'/'+IEEH['ANO_ING'].astype(str)+' '+IEEH['HORA_ING'].astype(str)+':'+IEEH['MIN_ING'].astype(str)
    IEEH['FECHA_ING'] =  pd.to_datetime(IEEH['FECHA_ING']).dt.strftime(formato)
    return (IEEH)

def normalize_tipo_ingreso(IEEH):
    IEEH.loc[IEEH['PROCEDENCI'] == 1, 'TIPO_ING'] = '1'
    IEEH.loc[IEEH['PROCEDENCI'] == 3, 'TIPO_ING'] = '2'
    IEEH.loc[IEEH['PROCEDENCI'] == 4, 'TIPO_ING'] = '2'
    IEEH.loc[IEEH['PROCEDENCI'] == 5, 'TIPO_ING'] = '2'
    IEEH.loc[IEEH['PROCEDENCI'] == 6, 'TIPO_ING'] = '2'
    IEEH.loc[IEEH['PROCEDENCI'] == 7, 'TIPO_ING'] = '2'
    return (IEEH)

def normalize_prev(IEEH):
    IEEH['PREVI'] = IEEH['PREVI'].astype(str)
    IEEH['PREVI'] = '0'+IEEH['PREVI']
    IEEH['PREVI'] = IEEH['PREVI'].map(lambda x: str(x)[-2:])
    IEEH.loc[IEEH['PREVI'] == '01', 'PREVI'] = 'Fonasa'
    IEEH.loc[IEEH['PREVI'] == '02', 'PREVI'] = 'Isapre'
    IEEH.loc[IEEH['PREVI'] == '96', 'PREVI'] = 'Ninguna'
    IEEH.loc[IEEH['PREVI'] == '99', 'PREVI'] = 'Desconocido'
    IEEH['MOD'] = IEEH['MOD'].astype(str)
    IEEH['MOD'] = IEEH['MOD'].map(lambda x: str(x)[:1])
    IEEH.loc[IEEH['PREVI'] == 'Fonasa' , 'PREVI'] = IEEH['PREVI'].astype(str)+' '+IEEH['BENEF'].astype(str)+'-0'+IEEH['MOD'].astype(str)
    IEEH.loc[IEEH['PREVI'] == 'Isapre' , 'PREVI'] = 7
    IEEH.loc[IEEH['PREVI'] == 'Ninguna' , 'PREVI'] = 8
    IEEH.loc[IEEH['PREVI'] == 'Desconocido' , 'PREVI'] = 0
    IEEH.loc[IEEH['PREVI'] == 'Fonasa A-01' , 'PREVI'] = 1
    IEEH.loc[IEEH['PREVI'] == 'Fonasa B-01' , 'PREVI'] = 2
    IEEH.loc[IEEH['PREVI'] == 'Fonasa C-01' , 'PREVI'] = 3
    IEEH.loc[IEEH['PREVI'] == 'Fonasa D-01' , 'PREVI'] = 4
    IEEH.loc[IEEH['PREVI'] == 'Fonasa C-02' , 'PREVI'] = 5
    IEEH.loc[IEEH['PREVI'] == 'Fonasa D-02' , 'PREVI'] = 6
    IEEH.loc[IEEH['PREVI'] == 'Fonasa B-02' , 'PREVI'] = 11
    return (IEEH)

def normalize_provincia(IEEH):
    comunas = pd.read_excel('comunas.xlsx')
    provincias = pd.read_excel('provincias.xlsx')
    comunas = comunas.merge(provincias, left_on='Provincia', right_on='Provincia')
    comunas = comunas[['CUT (Código Único Territorial)','Cod']]
    comunas['CUT (Código Único Territorial)'] = comunas['CUT (Código Único Territorial)'].astype(int)
    comunas['CUT (Código Único Territorial)'] = comunas['CUT (Código Único Territorial)'].astype(str)
    IEEH['COMUNA'] = IEEH['COMUNA'].astype(str)
    IEEH = IEEH.merge(comunas, left_on='COMUNA', right_on='CUT (Código Único Territorial)')
    return (IEEH)

def normalize_fecha_egreso(IEEH,formato):
    IEEH['FECHA_EGR'] = IEEH['DIA_EGR'].astype(str)+'/'+IEEH['MES_EGR'].astype(str)+'/'+IEEH['ANO_EGR'].astype(str)+' '+IEEH['HORA_EGR'].astype(str)+':'+IEEH['MIN_EGR'].astype(str)
    IEEH['FECHA_EGR'] =  pd.to_datetime(IEEH['FECHA_EGR']).dt.strftime(formato)
    return (IEEH)

def normalize_destino_alta(IEEH):
    IEEH['DES_ALTA'] = IEEH['DES_ALTA'].astype(str)
    IEEH.loc[IEEH['DES_ALTA'] == 'nan', 'DES_ALTA'] = '0'
    IEEH.loc[(IEEH['DES_ALTA'] == '2.0'), 'DES_ALTA'] = '4'
    IEEH.loc[(IEEH['DES_ALTA'] == '3.0'), 'DES_ALTA'] = '5'
    IEEH.loc[(IEEH['DES_ALTA'] == '4.0'), 'DES_ALTA'] = '7'
    IEEH.loc[(IEEH['DES_ALTA'] == '5.0'), 'DES_ALTA'] = '8'
    IEEH.loc[(IEEH['DES_ALTA'] == '6.0'), 'DES_ALTA'] = '9'
    IEEH.loc[(IEEH['DES_ALTA'] == '7.0'), 'DES_ALTA'] = '10'
    IEEH.loc[(IEEH['DES_ALTA'] == '1.0'), 'DES_ALTA'] = '1'
    IEEH.loc[(IEEH['DES_ALTA'] == '0'), 'DES_ALTA'] = '2'
    return (IEEH)

def normalize_rut_med(IEEH):
    IEEH['RUT_MEDICO'] = IEEH['RUT_MEDICO'].fillna(1)
    IEEH['RUT_MEDICO'] = IEEH['RUT_MEDICO'].astype(int)
    IEEH['RUT_MEDICO'] = IEEH['RUT_MEDICO'].astype(str)+'-'+IEEH['DV_M'].astype(str)
    IEEH['RUT_MEDICO'] = IEEH['RUT_MEDICO'].replace('1-nan',np.NaN)
    return (IEEH)

def normalize_rut_pac(IEEH):
    IEEH['RUT'] = IEEH['RUT'].fillna(1)
    IEEH['RUT'] = IEEH['RUT'].astype(int)
    IEEH['RUT'] = IEEH['RUT'].astype(str)+'-'+IEEH['DV'].astype(str)
    IEEH['RUT'] = IEEH['RUT'].replace('1-nan',np.NaN)
    return (IEEH)

def normalize_procedencia(IEEH,codigo_ss):
    IEEH['prueba'] = IEEH['COD_HOSP_P'].map(lambda x: str(x)[:-3])
    IEEH.loc[IEEH['prueba'] == codigo_ss, 'PROCEDENCI'] = 6
    IEEH.loc[IEEH['prueba'] != codigo_ss, 'PROCEDENCI'] = 7
    IEEH.loc[IEEH['PROCEDENCI'] == 1, 'PROCEDENCI'] = 1
    IEEH.loc[IEEH['PROCEDENCI'] == 3, 'PROCEDENCI'] = 5
    IEEH.loc[IEEH['PROCEDENCI'] == 6, 'PROCEDENCI'] = 11
    return (IEEH)

def normalize_cod_hosp(IEEH):
    IEEH['COD_HOSP_P'] = IEEH['COD_HOSP_P'].map(lambda x: str(x)[:6])
    return (IEEH)

def normalize_fechas_traslado(IEEH, formato):
    traslados = [1,2,3,4,5,6,7,8,9]
    for i in traslados:
        IEEH['DIA_'+str(i)+'_TRAS'] = IEEH['DIA_'+str(i)+'_TRAS'].fillna(1)
        IEEH['DIA_'+str(i)+'_TRAS'] = IEEH['DIA_'+str(i)+'_TRAS'].astype(int)
        IEEH['MES_'+str(i)+'_TRAS'] = IEEH['MES_'+str(i)+'_TRAS'].fillna(1)
        IEEH['MES_'+str(i)+'_TRAS'] = IEEH['MES_'+str(i)+'_TRAS'].astype(int)
        IEEH['ANO_'+str(i)+'_TRAS'] = IEEH['ANO_'+str(i)+'_TRAS'].fillna(1)
        IEEH['ANO_'+str(i)+'_TRAS'] = IEEH['ANO_'+str(i)+'_TRAS'].astype(int)

        IEEH['FECHA_'+str(i)+'_TRAS'] = IEEH['DIA_'+str(i)+'_TRAS'].astype(str)+'/'+IEEH['MES_'+str(i)+'_TRAS'].astype(str)+'/'+IEEH['ANO_'+str(i)+'_TRAS'].astype(str)
        IEEH['FECHA_'+str(i)+'_TRAS'] =  pd.to_datetime(IEEH['FECHA_'+str(i)+'_TRAS']).dt.strftime(formato)
        IEEH.loc[(IEEH['FECHA_'+str(i)+'_TRAS'] == '01/01/2001 00:00'), 'FECHA_'+str(i)+'_TRAS'] = ''
    return(IEEH)

def normalize_ley_prev(IEEH):
    IEEH.loc[IEEH['LEY_PREV'] == 2, 'LEY_PREV'] = '00'
    IEEH.loc[IEEH['ACC_ATEN'] == 1, 'LEY_PREV'] = '01'
    IEEH.loc[IEEH['ACC_ATEN'] == 2, 'LEY_PREV'] = '02'
    IEEH.loc[IEEH['ACC_ATEN'] == 3, 'LEY_PREV'] = '03'
    IEEH.loc[IEEH['ACC_ATEN'] == 4, 'LEY_PREV'] = '04'
    IEEH.loc[IEEH['ACC_ATEN'] == 5, 'LEY_PREV'] = '05'
    return(IEEH)

def normalize_especialidad(IEEH):
    IEEH.loc[IEEH['ESPEC'] == 1, 'ESPEC'] = '01'
    IEEH.loc[IEEH['ESPEC'] == 2, 'ESPEC'] = '02'
    IEEH.loc[IEEH['ESPEC'] == 3, 'ESPEC'] = '03'
    IEEH.loc[IEEH['ESPEC'] == 4, 'ESPEC'] = '04'
    return(IEEH)

def normalize_tipo_ocp(IEEH):
    IEEH['TIPO_OCUPACION'] = IEEH['TIPO_OCUPACION'].fillna('99')
    IEEH['TIPO_OCUPACION'] = IEEH['TIPO_OCUPACION'].astype(str)
    IEEH['TIPO_OCUPACION'] = IEEH['TIPO_OCUPACION'].str.zfill(2)   
    return(IEEH)

def normalize_glos_ocp(IEEH):
    IEEH.loc[IEEH['GLO_OCUPACION'] == 1, 'GLO_OCUPACION'] = '01'
    IEEH.loc[IEEH['GLO_OCUPACION'] == 2, 'GLO_OCUPACION'] = '02'
    IEEH.loc[IEEH['GLO_OCUPACION'] == 3, 'GLO_OCUPACION'] = '03'
    IEEH.loc[IEEH['GLO_OCUPACION'] == 4, 'GLO_OCUPACION'] = '04'
    IEEH.loc[IEEH['GLO_OCUPACION'] == 5, 'GLO_OCUPACION'] = '05'
    IEEH.loc[IEEH['GLO_OCUPACION'] == 6, 'GLO_OCUPACION'] = '06'
    IEEH.loc[IEEH['GLO_OCUPACION'] == 7, 'GLO_OCUPACION'] = '07'
    IEEH.loc[IEEH['GLO_OCUPACION'] == 8, 'GLO_OCUPACION'] = '08'
    IEEH.loc[IEEH['GLO_OCUPACION'] == 9, 'GLO_OCUPACION'] = '09'
    return(IEEH)  

def normalize_etnia(IEEH):
    IEEH['ETNIA'] = IEEH['ETNIA'].astype(str)
    IEEH['ETNIA'] = IEEH['ETNIA'].str.zfill(2)    
    return(IEEH)

def normalize_uf(IEEH):
    lista = ['AREA_FUNC_I','AREAF_1_TRAS','AREAF_2_TRAS','AREAF_3_TRAS','AREAF_4_TRAS','AREAF_5_TRAS','AREAF_6_TRAS','AREAF_7_TRAS','AREAF_8_TRAS','AREAF_9_TRAS','AREAF_EGR']
    for elemento in lista:
        IEEH[elemento] = IEEH[elemento].map(lambda x: str(x)[:3])
    return(IEEH)
    
def estructura_grd(IEEH):
    IEEH = IEEH[['ESTAB','FICHA','NUM_ADM','FECHA_NAC','SEXO','FECHA_ING','TIPO_ING','PREVI','ETNIA','Cod','COMUNA','P_ORIGEN',
            'FECHA_EGR','DES_ALTA','AREA_FUNC_I','AREAF_EGR','TIPO_ID','ESPEC','SER_SALUD','COD_HOSP_P','RUT_MEDICO','RUT',
            'PROCEDENCI','TIPO_ACTIVIDAD','ESTADO','NOMBRES','APELL_PATE','APELL_MATE','FECHA_1_TRAS','AREAF_1_TRAS',
             'FECHA_2_TRAS','AREAF_2_TRAS','FECHA_3_TRAS','AREAF_3_TRAS','FECHA_4_TRAS','AREAF_4_TRAS','FECHA_5_TRAS',
             'AREAF_5_TRAS','FECHA_6_TRAS','AREAF_6_TRAS','FECHA_7_TRAS','AREAF_7_TRAS','FECHA_8_TRAS','AREAF_8_TRAS',
             'FECHA_9_TRAS','AREAF_9_TRAS','GLO_OCUPACION','TIPO_OCUPACION','LEY_PREV']]

    IEEH.columns = ['HOSPITAL','HISTORIA','EPISODIO','FECNAC','SEXO','FECING','TIPING','REGCON_01','ETNIA','DIST_PAC','MRES','PAIS',
                'FECALT','TIPALT','SERVING','SERVALT','TIPO_CIP','ESPECIALIDAD','SERVICIO_SALUD','PROCHOSPITAL',
                'MEDICOALT','CIP','PROC','TIPO_ACTIVIDAD','ESTADO','NOMBRE','APELLIDO1','APELLIDO2','TRAS_FEC_01',
                'TRAS_SRV_01','TRAS_FEC_02','TRAS_SRV_02','TRAS_FEC_03','TRAS_SRV_03','TRAS_FEC_04','TRAS_SRV_04',
                'TRAS_FEC_05','TRAS_SRV_05','TRAS_FEC_06','TRAS_SRV_06','TRAS_FEC_07','TRAS_SRV_07','TRAS_FEC_08','TRAS_SRV_08',
                'TRAS_FEC_09','TRAS_SRV_09','OCUPACION','CAT_OCP','PROGRAMA']

    GRD = pd.DataFrame(columns=('HOSPITAL','HISTORIA','EPISODIO','FECNAC','SEXO','FECING','TIPING','REGCON_01','ETNIA','DIST_PAC',
                                'MRES','PAIS','FECALT','TIPALT','SERVING','SERVALT','TIPO_CIP','ESPECIALIDAD','SERVICIO_SALUD',
                                'FEC_INT_1','FECPART','TGESTAC','RN_PESO_01','RN_SEXO_01','RN_PESO_02','RN_SEXO_02','RN_PESO_03',
                                'RN_SEXO_03','RN_PESO_04','RN_SEXO_04','TRASHOSPITAL','PROCHOSPITAL','MEDICOALT','CIP','PROC',
                                'TIPO_ACTIVIDAD','RN_EST_01','RN_EST_02','RN_EST_03','RN_EST_04','ESTADO','NOMBRE','APELLIDO1','APELLIDO2','PROGRAMA','RN_COND_ING_01',
                                'RN_COND_ING_02','RN_COND_ING_03','RN_COND_ING_04','CUMPLIMENTACION','MED_INT_1','ESPINT',
                                'TIP_PAB','TRAS_FEC_01','TRAS_SRV_01','TRAS_FEC_02','TRAS_SRV_02','TRAS_FEC_03','TRAS_SRV_03',
                                'TRAS_FEC_04','TRAS_SRV_04','TRAS_FEC_05','TRAS_SRV_05','TRAS_FEC_06','TRAS_SRV_06','TRAS_FEC_07',
                                'TRAS_SRV_07','TRAS_FEC_08','TRAS_SRV_08','TRAS_FEC_09','TRAS_SRV_09','TRAS_FEC_10','TRAS_SRV_10',
                                'FEC_URGENCIAS','OCUPACION','CAT_OCP'))

    GRD = GRD[['HOSPITAL','HISTORIA','EPISODIO','FECNAC','SEXO','CIP','FECING','TIPING','REGCON_01','ETNIA','DIST_PAC',
                                'MRES','PAIS','FECALT','TIPALT','SERVING','SERVALT','TIPO_CIP','ESPECIALIDAD','SERVICIO_SALUD',
                                'FEC_INT_1','FECPART','TGESTAC','RN_PESO_01','RN_SEXO_01','RN_PESO_02','RN_SEXO_02','RN_PESO_03',
                                'RN_SEXO_03','RN_PESO_04','RN_SEXO_04','TRASHOSPITAL','PROCHOSPITAL','PROC',
                                'TIPO_ACTIVIDAD','RN_EST_01','RN_EST_02','RN_EST_03','RN_EST_04','ESTADO','NOMBRE','APELLIDO1','APELLIDO2','PROGRAMA','RN_COND_ING_01',
                                'RN_COND_ING_02','RN_COND_ING_03','RN_COND_ING_04','CUMPLIMENTACION','MED_INT_1','ESPINT',
                                'TIP_PAB','TRAS_FEC_01','TRAS_SRV_01','TRAS_FEC_02','TRAS_SRV_02','TRAS_FEC_03','TRAS_SRV_03',
                                'TRAS_FEC_04','TRAS_SRV_04','TRAS_FEC_05','TRAS_SRV_05','TRAS_FEC_06','TRAS_SRV_06','TRAS_FEC_07',
                                'TRAS_SRV_07','TRAS_FEC_08','TRAS_SRV_08','TRAS_FEC_09','TRAS_SRV_09','TRAS_FEC_10','TRAS_SRV_10','MEDICOALT',
                                'FEC_URGENCIAS','OCUPACION','CAT_OCP']]
    
    GRD_f = GRD.append(IEEH)
    
    return(GRD_f)