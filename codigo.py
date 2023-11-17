import pandas as pd
from script import send_dataframe_to_kafka
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
datos_2015=pd.read_csv('2015.csv')
datos_2016=pd.read_csv('file:///C:/Users/Admin/Downloads/2016.csv')
datos_2017=pd.read_csv('file:///C:/Users/Admin/Downloads/2017.csv')
datos_2018=pd.read_csv('file:///C:/Users/Admin/Downloads/2018.csv')
datos_2019=pd.read_csv('file:///C:/Users/Admin/Downloads/2019.csv')

# Función de modificación para el año 2015
def modificacion_2015(datos_2015):
    nuevos_nombres = {
        'Happiness Score': 'Happiness Score',
        'Economy (GDP per Capita)': 'GDP',
        'Family': 'Family',
        'Health (Life Expectancy)': 'Life Expectancy',
        'Freedom': 'Freedom',
        'Trust (Government Corruption)': 'Corruption',
        'Generosity': 'Generosity',
    }
    columnas_a_eliminar = ['Region', 'Happiness Rank','Standard Error','Dystopia Residual']
    df_2015 = datos_2015.rename(columns=nuevos_nombres)
    df_2015 = df_2015.drop(columns=columnas_a_eliminar, errors='ignore')
    return df_2015

# Función de modificación para el año 2016
def modificacion_2016(datos_2016):
    nuevos_nombres ={
        'Happiness Score': 'Happiness Score',
        'Economy (GDP per Capita)': 'GDP',
        'Family': 'Family',
        'Health (Life Expectancy)': 'Life Expectancy',
        'Freedom': 'Freedom',
        'Trust (Government Corruption)': 'Corruption',
        'Generosity': 'Generosity',
    }
    columnas_a_eliminar = ['Region', 'Happiness Rank','Lower Confidence Interval','Upper Confidence Interval','Dystopia Residual']
    df_2016 = datos_2016.rename(columns=nuevos_nombres)
    df_2016 = df_2016.drop(columns=columnas_a_eliminar, errors='ignore')
    return df_2016

# Función de modificación para el año 2017
def modificacion_2017(datos_2017):
    nuevos_nombres ={
        'Country':'Country',
        'Happiness.Score': 'Happiness Score',
        'Economy..GDP.per.Capita.': 'GDP',
        'Family': 'Family',
        'Health..Life.Expectancy.': 'Life Expectancy',
        'Freedom': 'Freedom',
        'Trust..Government.Corruption.': 'Corruption',
        'Generosity': 'Generosity',
    }
    columnas_a_eliminar = ['Whisker.high','Happiness.Rank','Whisker.low','Dystopia.Residual']
    df_2017 = datos_2017.rename(columns=nuevos_nombres)
    df_2017 = df_2017.drop(columns=columnas_a_eliminar, errors='ignore')
    return df_2017

# Función de modificación para el año 2018
def modificacion_2018(datos_2018):
    nuevos_nombres ={
        'Country or region':'Country',
        'Score': 'Happiness Score',
        'GDP per capita': 'GDP',
        'Social support': 'Family',
        'Healthy life expectancy': 'Life Expectancy',
        'Freedom to make life choices': 'Freedom',
        'Perceptions of corruption': 'Corruption',
        'Generosity': 'Generosity',
    }
    columnas_a_eliminar = ['Overall rank']
    df_2018 = datos_2018.rename(columns=nuevos_nombres)
    df_2018 = df_2018.drop(columns=columnas_a_eliminar, errors='ignore')
    return df_2018
def modificacion_2019(datos_2019):
    nuevos_nombres ={
        'Country or region':'Country',
        'Score': 'Happiness Score',
        'GDP per capita': 'GDP',
        'Social support': 'Family',
        'Healthy life expectancy': 'Life Expectancy',
        'Freedom to make life choices': 'Freedom',
        'Perceptions of corruption': 'Corruption',
        'Generosity': 'Generosity',
    }
    columnas_a_eliminar = ['Overall rank']
    df_2019 = datos_2019.rename(columns=nuevos_nombres)
    df_2019 = df_2019.drop(columns=columnas_a_eliminar, errors='ignore')

    return df_2019

# Suponiendo que tienes DataFrames correspondientes a cada año (datos_2015, datos_2016, datos_2017, datos_2018)
# Aplicar las modificaciones a los DataFrames de cada año

datos_final_2015 = modificacion_2015(datos_2015)
datos_final_2016 = modificacion_2016(datos_2016)
datos_final_2017 = modificacion_2017(datos_2017)
datos_final_2018 = modificacion_2018(datos_2018)
datos_final_2019 = modificacion_2019(datos_2019)


dataframes = [datos_final_2015, datos_final_2016, datos_final_2017, datos_final_2018,datos_final_2019]

# Concatenar los DataFrames en uno solo
datos_completos = pd.concat(dataframes, ignore_index=True)

datos_completos = datos_completos.dropna()
y=datos_completos['Happiness Score']
X=datos_completos[['GDP','Family','Life Expectancy','Freedom','Corruption','Generosity']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


indices_X_test = X.index[X.isin(X_test.to_dict(orient='list')).all(axis=1)]

# Crear un nuevo DataFrame con las filas de X_test en datos completos
datos_completos_test = datos_completos.loc[indices_X_test]


send_dataframe_to_kafka(datos_completos_test,'kafka_prueba')

