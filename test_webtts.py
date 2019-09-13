#-*- coding: utf-8 -*-
#完成由文字到语音的转换以及播放，实现给一个词就读出来的功能
import requests
import time
import hashlib
import base64

import pyaudio
import wave


#  合成webapi接口地址
URL = "http://api.xfyun.cn/v1/service/v1/tts"
#  音频编码(raw合成的音频格式pcm、wav,lame合成的音频格式MP3)
AUE = "raw"
#  应用APPID（必须为webapi类型应用，并开通语音合成服务，参考帖子如何创建一个webapi应用：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=36481
APPID = "5d668d4d"
#  接口密钥（webapi类型应用开通合成服务后，控制台--我的应用---语音合成---相应服务的apikey）
API_KEY = "d5650158056598b9fe70c4f936c09c03"



def play_audio(path):
    CHUNK = 1024
    # 从目录中读取语音
    wf = wave.open(path, 'rb')
    # read data
    data = wf.readframes(CHUNK)
    # 创建播放器
    p = pyaudio.PyAudio()
    # 获得语音文件的各个参数
    FORMAT = p.get_format_from_width(wf.getsampwidth())
    CHANNELS = wf.getnchannels()
    RATE = wf.getframerate()
    #print('FORMAT: {} \nCHANNELS: {} \nRATE: {}'.format(FORMAT, CHANNELS, RATE))
    # 打开音频流， output=True表示音频输出
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    frames_per_buffer=CHUNK,
                    output=True)
    # play stream (3) 按照1024的块读取音频数据到音频流，并播放
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

# 组装http请求头
def getHeader():
    curTime = str(int(time.time()))
    # ttp=ssml
    param = "{\"aue\":\"" + AUE + "\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\"xiaoyan\",\"engine_type\":\"intp65\"}"
    #print("param:{}".format(param))

    paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
    #print("x_param:{}".format(paramBase64))

    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))

    checkSum = m2.hexdigest()
    #print('checkSum:{}'.format(checkSum))

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'X-Real-Ip': '127.0.0.1',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    #print(header)
    return header


def getBody(text):
    data = {'text': text}
    return data


def writeFile(file, content):
    with open(file, 'wb') as f:
        f.write(content)
    f.close()

def main(text):
    #  待合成文本内容
    r = requests.post(URL, headers=getHeader(), data=getBody(text))

    contentType = r.headers['Content-Type']
    if contentType == "audio/mpeg":
        sid = r.headers['sid']
        if AUE == "raw":
            print(r.content)
    #   合成音频格式为pcm、wav并保存在audio目录下
            path="audio/" + sid + ".wav"
            writeFile(path, r.content)
            play_audio(path)


        else:
            print(r.content)
    #   合成音频格式为mp3并保存在audio目录下
            writeFile("audio/" + "xiaoyan" + ".mp3", r.content)
        print("success, sid = " + sid)
    else:
    #   错误码链接：https://www.xfyun.cn/document/error-code （code返回错误码时必看）
        print(r.text)

if __name__=='__main__':
    main('传奇')