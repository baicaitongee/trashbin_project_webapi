# -*-coding:utf-8 -*-  
__author__ = "YZC"
import threading
import cv2
import time
import shutil
from keras.models import load_model
from PIL import Image
import numpy as np

from sqlite_test import update_data

from recognize import recognize_API
from TTS import test_webtts
#from AMSpi import dc_example


def cam():
    # 保存截图
    save_path = './img/'

    # 坑：model载入必须在函数内，否则可能不进行运行
    #model = load_model('my_model1.h5')

    # 类别
    #labels = {'cardboard': 0, 'glass': 1, 'metal': 2, 'paper': 3, 'plastic': 4, 'trash': 5}

    # 定义摄像头对象，其参数0表示第一个摄像头
    camera = cv2.VideoCapture(0)

    # 判断视频是否打开
    if (camera.isOpened()):
        print('Open')
    else:
        print('摄像头未打开')

    # 测试用,查看视频size
    size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('size:' + repr(size))

    # 帧率
    fps = 5
    # 总是取前一帧做为背景（不用考虑环境影响）
    pre_frame = None
    #拍照数
    num_pict = 0


    # 预加载
    ret, frame = camera.read()
    time.sleep(1)# 等待两秒




    while (1):
        start = time.time()
        # 读取视频流
        ret, frame = camera.read()
        # 转灰度图
        gray_lwpCV = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if not ret:
            break
        end = time.time()

        # 显示图像
        # cv2.imshow("capture", frame)

        # 运动检测部分
        seconds = end - start
        if seconds < 1.0 / fps:
            time.sleep(1.0 / fps - seconds)
        gray_lwpCV = cv2.resize(gray_lwpCV, (500, 500))
        # 用高斯滤波进行模糊处理
        gray_lwpCV = cv2.GaussianBlur(gray_lwpCV, (21, 21), 0)
        # putText 图片中加入文字
        cv2.putText(frame,
                    "now time: {}".format(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))),
                    (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # 如果没有背景图像就将当前帧当作背景图片
        if pre_frame is None:
            pre_frame = gray_lwpCV
        else:
            # absdiff把两幅图的差的绝对值输出到另一幅图上面来
            img_delta = cv2.absdiff(pre_frame, gray_lwpCV)
            # threshold阈值函数(原图像应该是灰度图,对像素值进行分类的阈值,当像素值高于（有时是小于）阈值时应该被赋予的新的像素值,阈值方法)
            thresh = cv2.threshold(img_delta, 25, 255, cv2.THRESH_BINARY)[1]
            # 膨胀图像
            thresh = cv2.dilate(thresh, None, iterations=2)
            # findContours检测物体轮廓(寻找轮廓的图像,轮廓的检索模式,轮廓的近似办法)
            contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # contours 有很多不同形状的轮廓，用c进行遍历，小于某个值时进行下一轮，大于某个值说明图像更改较大，有物体进入
            for c in contours:
                # 设置敏感度
                # contourArea计算轮廓面积
                if cv2.contourArea(c) < 10000:
                    continue
                else:

                    # 等待图像稳定时间
                    time.sleep(1)
                    num_pict += 1
                    print("出现目标物，请求核实第"+str(num_pict)+"张   "+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))

                    ret, frame = camera.read()

                    mingcheng = save_path+str(num_pict)+str(time.strftime(" %m-%d %H_%M_%S", time.localtime(time.time())))+".png"
                    cv2.imwrite(mingcheng, frame)
                    outee=recognize_API.main(mingcheng)
                    print(outee)
                    test_webtts.main(outee)


                    #dc_example.main()

                    update_data(1,1,1,1)
                    print("已更新数据库")

                    # 等待两个机关启动时间
                    time.sleep(2)
                    print('相机再启动时间'+str(time.strftime(" %m-%d %H_%M_%S", time.localtime(time.time()))))
                    break
            ret, frame = camera.read()
            # 转灰度图
            gray_lwpCV = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            gray_lwpCV = cv2.resize(gray_lwpCV, (500, 500))
            # 用高斯滤波进行模糊处理
            gray_lwpCV = cv2.GaussianBlur(gray_lwpCV, (21, 21), 0)


            pre_frame = gray_lwpCV

            # print(num_pict)

            # 显示图像
            cv2.imshow("capture", frame)
            # cv2.imshow("Thresh", thresh)
            # 进行阀值化来显示图片中像素强度值有显著变化的区域的画面
            cv2.imshow("Frame Delta", img_delta)
            # 不同按键不同功能
            key = cv2.waitKey(1) & 0xFF
            # 按'q'健退出循环
            if key == ord('q'):
                break

             # 按'w'健退出循环
            if key == ord('w'):
                shutil.rmtree('./img/', True)  # 删除里面所有文件
                break



    # release()释放摄像头
    camera.release()
    # destroyAllWindows()关闭所有图像窗口
    cv2.destroyAllWindows()



def main():
    """创建启动线程"""
    t_cam = threading.Thread(target=cam)  # 函数名不能带括号
    t_cam.start()


if __name__ == '__main__':
    main()