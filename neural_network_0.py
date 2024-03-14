import numpy as np
import matplotlib.pyplot as plt 
from tensorflow.keras.utils import to_categorical

from keras import models
from keras import layers

print('Reading files cn_p_data.dat and cn_a_data.dat')
data_p = np.loadtxt('cn_p_data.dat') 
data_l = np.loadtxt('cn_a_data.dat') 

train_size = int(len(data_p)*(4/5))

train_data  = data_p[:train_size]
train_label = data_l[:train_size]

test_data  = data_p[train_size:]
test_label = data_l[train_size:]

print('Compiling ANN')

model = models.Sequential()
model.add(layers.Dense(64,activation='relu', input_shape=data_p[0].shape))
model.add(layers.Dense(1))

model.compile(optimizer='rmsprop',
              loss='mse',
              metrics=['mae'])

print('Start training stage')
model.fit(train_data, train_label,epochs=1000, batch_size=256)

score = model.evaluate(test_data, test_label, verbose=0)
print ('The ANN presents a MAE=%f' % score[1])

print('Saving ANN in model.keras files')
model.save('model.keras')
print('Done')
