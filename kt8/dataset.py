import tensorflow as tf
import numpy as np

#data1 = tf.data.Dataset.from_tensor_slices([np.ones((1,10)), np.ones((1,10))])
data1 = tf.data.Dataset.from_tensor_slices([1,2,3,4,5,6,7,8])
#data1 = tf.data.TextLineDataset(["testi.py", "second.py"])
#data1 = tf.data.Dataset.list_files("c:/temp/*.*")

def filter_fn(x):
    y = False
    if(x<4):
        y = True
    return y

#data1 = data1.filter(lambda x:x<4)
data1 = data1.filter(filter_fn)
for element in data1.as_numpy_iterator():
    print(element)

#for element in data1:
#    print(element)

data1 = data1.map(lambda x: x+5)
for element in data1.as_numpy_iterator():
    print(element)
