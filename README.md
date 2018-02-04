# DI
import numpy as np
import pandas as pd

WD= pd.read_csv("012330-99999-2017.csv")


print(WD.shape)
list(WD)

colsToDrop = [ 'Year','Month','Day','Weather_Station_USAF ', 'SYNOP Type','Obs Type','Call Letter Identifier','Weather_Station_USAF ']
x_train= WD.drop(colsToDrop, axis=1)
y_train = WD['Air Temp (Cel)']
#y_train = WD.iloc[:,18]
#y_train = pd.DataFrame(y_train)
#print(x_train.shape[1])
#print(y_train.shape[0])
list(x_train)
list(x_train.shape)

x_train_lag = pd.concat([x_train.shift(24), x_train.shift(48), x_train.shift(72), x_train.shift(94),  x_train.shift(116),  x_train.shift(140),  x_train.shift(164)], axis=1)
list(x_train_lag)

x_train_lag.columns = ["Total_Record_length_lag_1","Date_lag_1","time.H_lag_1","Obs Type_lag_1","Latitude_lag_1",
                       "Longitude_lag_1","SYNOP Type_lag_1","Elevation(m)_lag_1","Wind (Angular Degrees)_lag_1",
                       "Wind (QC)_lag_1","Wind TC_lag_1","Wind Speed (m/s)_lag_1","Wind Speed (QC)_lag_1","Air Temp (Cel)_lag_1",
                       "Air Temp (QC)_lag_1","Dew Point (Cel)_lag_1","Dew Point (QC)_lag_1","Precip Time (H)_lag_1",
                       "Precip Depth (mm)_lag_1","Precip (CC)_lag_1","Precip (QC)_lag_1","Total_Record_length_lag_2",
                       "Date_lag_2","time.H_lag_2","Obs Type_lag_2","Latitude_lag_2","Longitude_lag_2","SYNOP Type_lag_2",
                       "Elevation(m)_lag_2","Wind (Angular Degrees)_lag_2","Wind (QC)_lag_2","Wind TC_lag_2",
                       "Wind Speed (m/s)_lag_2","Wind Speed (QC)_lag_2","Air Temp (Cel)_lag_2","Air Temp (QC)_lag_2","Dew Point (Cel)_lag_2",
                       "Dew Point (QC)_lag_2","Precip Time (H)_lag_2","Precip Depth (mm)_lag_2","Precip (CC)_lag_2",
                       "Precip (QC)_lag_2","Total_Record_length_lag_3","Date_lag_3","time.H_lag_3","Obs Type_lag_3",
                       "Latitude_lag_3","Longitude_lag_3","SYNOP Type_lag_3","Elevation(m)_lag_3",
                       "Wind (Angular Degrees)_lag_3","Wind (QC)_lag_3","Wind TC_lag_3","Wind Speed (m/s)_lag_3",
                       "Wind Speed (QC)_lag_3","Air Temp (Cel)_lag_3","Air Temp (QC)_lag_3","Dew Point (Cel)_lag_3","Dew Point (QC)_lag_3",
                       "Precip Time (H)_lag_3","Precip Depth (mm)_lag_3","Precip (CC)_lag_3","Precip (QC)_lag_3",
                       "Total_Record_length_lag_4","Date_lag_4","time.H_lag_4","Obs Type_lag_4","Latitude_lag_4",
                       "Longitude_lag_4","SYNOP Type_lag_4","Elevation(m)_lag_4","Wind (Angular Degrees)_lag_4",
                       "Wind (QC)_lag_4","Wind TC_lag_4","Wind Speed (m/s)_lag_4","Wind Speed (QC)_lag_4","Air Temp (Cel)_lag_4","Air Temp (QC)_lag_4",
                       "Dew Point (Cel)_lag_4","Dew Point (QC)_lag_4","Precip Time (H)_lag_4","Precip Depth (mm)_lag_4",
                       "Precip (CC)_lag_4","Precip (QC)_lag_4","Total_Record_length_lag_5","Date_lag_5","time.H_lag_5",
                       "Obs Type_lag_5","Latitude_lag_5","Longitude_lag_5","SYNOP Type_lag_5","Elevation(m)_lag_5",
                       "Wind (Angular Degrees)_lag_5","Wind (QC)_lag_5","Wind TC_lag_5","Wind Speed (m/s)_lag_5",
                       "Wind Speed (QC)_lag_5","Air Temp (Cel)_lag_5","Air Temp (QC)_lag_5","Dew Point (Cel)_lag_5","Dew Point (QC)_lag_5",
                       "Precip Time (H)_lag_5","Precip Depth (mm)_lag_5","Precip (CC)_lag_5","Precip (QC)_lag_5",
                       "Total_Record_length_lag_6","Date_lag_6","time.H_lag_6","Obs Type_lag_6","Latitude_lag_6",
                       "Longitude_lag_6","SYNOP Type_lag_6","Elevation(m)_lag_6","Wind (Angular Degrees)_lag_6",
                       "Wind (QC)_lag_6","Wind TC_lag_6","Wind Speed (m/s)_lag_6","Wind Speed (QC)_lag_6","Air Temp (Cel)_lag_6",
                       "Air Temp (QC)_lag_6","Dew Point (Cel)_lag_6","Dew Point (QC)_lag_6","Precip Time (H)_lag_6",
                       "Precip Depth (mm)_lag_6","Precip (CC)_lag_6","Precip (QC)_lag_6","Total_Record_length_lag_7",
                       "Date_lag_7","time.H_lag_7","Obs Type_lag_7","Latitude_lag_7","Longitude_lag_7","SYNOP Type_lag_7",
                       "Elevation(m)_lag_7","Wind (Angular Degrees)_lag_7","Wind (QC)_lag_7","Wind TC_lag_7",
                       "Wind Speed (m/s)_lag_7","Wind Speed (QC)_lag_7","Air Temp (Cel)_lag_7","Air Temp (QC)_lag_7","Dew Point (Cel)_lag_7",
                       "Dew Point (QC)_lag_7","Precip Time (H)_lag_7","Precip Depth (mm)_lag_7","Precip (CC)_lag_7",
                       "Precip (QC)_lag_7"]

train_x_lag = pd.concat([x_train_lag, y_train], axis = 1)
print(train_x_lag)

import pyflux as pf
from datetime import datetime
import matplotlib.pyplot as plt
%matplotlib inline

index = WD.index
plt.figure(figsize=(15,5))
plt.plot(index,WD['Air Temp (Cel)'])
plt.ylabel('Air Temp (Cel)')
plt.title('Air Temp (Degrees Celcius)');

plt.figure(figsize=(15,5))
plt.plot(index,WD['Wind Speed (m/s)'])
plt.ylabel('Wind Speed (m/s)')
plt.title('Wind Speed (m/s)');

plt.figure(figsize=(15,5))
plt.plot(index,WD['Wind (Angular Degrees)'])
plt.ylabel('Wind (Angular Degrees)')
plt.title('Wind (Angular Degrees)');

import h2o
h2o.init()

train_x = h2o.H2OFrame(train_x_lag)

from h2o.estimators.deeplearning import H2OAutoEncoderEstimator, H2ODeepLearningEstimator

y = 'Air Temp (Cel)'
x = list(train_x.columns)
x.remove(y)

dl_1 = H2ODeepLearningEstimator(epochs=1)
dl_1.train(x, y, train_x)

dl_250 = H2ODeepLearningEstimator(checkpoint=dl_1, epochs=250)
dl_250.train(x, y, train_x)

dl_500 = H2ODeepLearningEstimator(checkpoint=dl_250, epochs=500)
dl_500.train(x, y, train_x)

dl_750 = H2ODeepLearningEstimator(checkpoint=dl_500, epochs=750)
dl_750.train(x, y, train_x)

dl_model = H2ODeepLearningEstimator(epochs=1000)
dl_model.train(x, y, train_x)


VI_500 = dl_500._model_json['output']['variable_importances'].as_data_frame()
VI_500 = VI_500.iloc[0:27,]

print(VI_500)

plt.figure(figsize=(15,10))
x = VI_500['variable']
relative_importance = VI_500['relative_importance']

x_pos = [i for i, _ in enumerate(x)]

plt.barh(x_pos, relative_importance, color='purple')
plt.ylabel("Variable")
plt.title("Deep Learning Variable Importance Chart")

plt.yticks(x_pos, x)

plt.show()
