# 需要进行建立模型
import keras
from keras.preprocessing.image import ImageDataGenerator
# 隐藏层
from keras.layers import Conv2D, Flatten, MaxPool2D, Dense,Dropout
from keras.models import Sequential
# 优化方法
from keras.optimizers import Adam

train_dir = 'images'
num_epochs = 1
batch_size = 100

# rescale 像素比例缩放  validation_split 验证集数据比例
data_gen = ImageDataGenerator(rescale=1. / 255, validation_split=0.1)

# train_dir  文件夹
# target_size=(64, 64)  对象缩放比例
# batch_size=batch_size 一次读入多少图片，一共读多少数据，决定与data_gen中的validation_split验证集切割
# class_mode  固定字段，会根据给定路径下的文件夹做分类
# subset   training validation  训练集  和验证集 
train_generator = data_gen.flow_from_directory(train_dir,
                                               target_size=(64, 64),
                                               batch_size=batch_size,
                                               class_mode='categorical', subset='training')
validation_generator = data_gen.flow_from_directory(train_dir,
                                               target_size=(64, 64),
                                               batch_size=batch_size,
                                               class_mode='categorical', subset='validation')




#获得原始数据
# train_generator.__getitem__(1)
#获得分类对应
labels =train_generator.class_indices
print(labels)


# *******************************************************************
model=Sequential()
#输入层
model.add(Conv2D(64,3,3,input_shape=(64, 64,3),activation='relu'))
#隐藏层  计算
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(output_dim=32,activation='relu'))
# +1~-1  宽度比较大
model.add(Dense(output_dim=7,activation='sigmoid'))
model.summary()


#损失函数
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
# 试试看 3轮 准确率 88.75%
# model.fit(X_train , y_train, batch_size= 15, epochs = 3)
# *******************************************************************
# steps_per_epoch  一次训练多少张
# validation_steps  一次验证多少张
# epochs  训练几轮
#validation_data 验证数据是什么


model.fit_generator(train_generator, 
                    steps_per_epoch= 5, #100
                    validation_steps=1, #50
                    epochs= 3, 
                    validation_data=validation_generator)

#acc是准确度  loss是错误
model.save('my_model1.h5')
