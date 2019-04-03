import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd

datos2008=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2008.txt', sep=";", names=['fecha', 'hora','valor', 'algo'])

datos2009=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2009.txt', sep=";", names=['fecha', 'hora','valor', 'algo'])

datos2010=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2010.txt', sep=";", names=['fecha', 'hora','valor', 'algo'])

datos2008['nueva']=datos2008["fecha"].astype(str).str[:-8] + " " + datos2008["hora"].astype(str).str[-8:]

datos2009['nueva']=datos2009["fecha"].astype(str).str[:-8] + " " + datos2009["hora"].astype(str).str[-8:]

datos2010['nueva']=datos2010["fecha"].astype(str).str[:-8] + " " + datos2010["hora"].astype(str).str[-8:]


datos2008n=datos2008.drop(['fecha', 'hora', 'algo'], axis=1)
print(datos2008n)

datos2009n=datos2009.drop(['fecha', 'hora', 'algo'], axis=1)
print(datos2009n)

datos2010n=datos2010.drop(['fecha', 'hora', 'algo'], axis=1)
print(datos2010n)


data=pd.concat([datos2008n, datos2009n, datos2010n])

print(data)

data['nueva']=pd.to_datetime(data['nueva'])
data.set_index(['nueva'],inplace=True)

data.plot(figsize=(20,7))
plt.show()
