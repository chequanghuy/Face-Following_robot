import os
from keras.players import *
from keras.models import *
from keras import optimizers
import numpy as np 
x_data=[[],
[],
[],
]
y_data=[[]]
x_data=np.asarray(x_data)
y_data=np.asarray(y_data)
model=Sequential()
model.add(Dense(units=1,input_dim=2))
model.compile(loss='mse',optimizer='rmsprop')
model.summary()
model.fit(x_data,y_data,epochs=100)

