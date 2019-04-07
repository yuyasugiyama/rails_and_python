import numpy as np
import sys
from keras.models import Model
from keras.layers import Input,Dense, Dropout, Activation
from keras.layers import BatchNormalization
from keras.optimizers import SGD
from keras import backend as K
from keras.applications.vgg16 import VGG16
import json
import cv2

K.set_image_dim_ordering('th')

def extract_features(path): #入力画像から特徴量を抽出
   base_model=VGG16(weights='imagenet')#学習済みVGG16を用いる
   model = Model(inputs=base_model.input,outputs=base_model.get_layer('fc1').output)
   img = cv2.imread(path)
   img = cv2.resize(img,(224,224))
   img = img.transpose((2,0,1))
   img = img.astype('float32')
   img /= 255
   x_input = img
   x_input = np.expand_dims(x_input, axis=0)#複数枚入力を基本とするため、次元合わせ
   x_pred = model.predict(x_input,verbose=0)
   return x_pred

def label_predict(path):
  img_input = extract_features(path)

  #ネットワーク
  main_input = Input(shape= img_input.shape[1:],name='main_input')
  x = Dense(4096)(main_input)
  x = BatchNormalization()(x)
  x = Activation('relu')(x)
  x = Dropout(0.5)(x)
  x = Dense(4096)(x)
  x = BatchNormalization()(x)
  x = Activation('relu')(x)
  x = Dropout(0.5)(x)
  main_output = Dense(116,activation='sigmoid',name='main_output')(x)
  auxiliary_output = Dense(116,activation='sigmoid',name='aux_output')(x)
  model = Model(inputs=main_input,outputs=[main_output,auxiliary_output])
  sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
  model.compile(loss={'main_output':'binary_crossentropy','aux_output':'mean_squared_error'},loss_weights={'main_output':1.0,'aux_output':1.0}, optimizer=sgd, metrics={'main_output':'accuracy','aux_output':'accuracy'})
  model.load_weights("/mnt/exthd1/home/y-sugiyama/rails/weights.ver2_0.0876433778019_top.hdf5")#適切なパスに変更
  output = model.predict(img_input)#ラベル予測
  return output

if __name__ == '__main__':
  args = sys.argv
  output = label_predict(args[1])
  f = open('/mnt/exthd1/home/y-sugiyama/rails/taglist2.json','r')#適切なパスに変更
  labellist = json.load(f)
  f.close()
  threshold = np.full(116,0.5)#ラベル決定のための閾値
  tags = np.array([[1 if output[0][i,j]>=threshold[j] else 0 for j in range(output[0].shape[1])] for i in range(output[0].shape[0])])

  #出力
  for i in range(len(labellist)):
    if tags[0][i] > 0:
      print(labellist[i],round(output[1][0,i],3))

