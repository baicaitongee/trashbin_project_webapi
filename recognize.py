# 需要进行建立模型
import keras
from keras.preprocessing.image import ImageDataGenerator
# 隐藏层
from keras.layers import Conv2D, Flatten, MaxPool2D, Dense,Dropout
from keras.models import Sequential
# 优化方法
from keras.optimizers import Adam

# 加载模型
from keras.models import load_model
model = load_model('my_model1.h5')





from PIL import Image
import numpy as np
image = Image.open("paper4.jpg") # 用PIL中的Image.open打开图像
img2=image.resize((64, 64),Image.ANTIALIAS)
image_arr = np.array(img2) # 转化成numpy数组
image_arr=image_arr/255
image_arr.shape
image_1=np.array([image_arr])

# test_x, test_y = validation_generator.__getitem__(1)
# labels = (train_generator.class_indices)
# labels = dict((v,k) for k,v in labels.items())
# preds = model.predict(test_x)
# preds
# plt.figure(figsize=(16, 16))
# for i in range(16):
#     plt.subplot(4, 4, i+1)
#     plt.title('pred:%s / truth:%s' % (labels[np.argmax(preds[i])], labels[np.argmax(test_y[i])]))
#     plt.imshow(test_x[i])

#预测一张怎么预测
#导入导出模型 深度学习h5 机器学习pkl



preds = model.predict(image_1)
print(preds)
