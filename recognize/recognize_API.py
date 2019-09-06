import requests
import time
import hashlib
import base64
from recognize import read_xlsx
 
URL = "http://tupapi.xfyun.cn/v1/currency"
APPID = "5d668d4d"
API_KEY = "79da89e4f4c7f7c50c7ccf8d9873cc7d"
ImageName = "img.jpg"
ImageUrl = ""


# FilePath = r"/home/baicaitong/Pictures/xiangjiao.jpg"


def getHeader(image_name, image_url=None):
    curTime = str(int(time.time()))
    param = "{\"image_name\":\"" + image_name + "\",\"image_url\":\"" + image_url + "\"}"
    paramBase64 = base64.b64encode(param.encode('utf-8'))
    tmp = str(paramBase64, 'utf-8')

    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + tmp).encode('utf-8'))
    checkSum = m2.hexdigest()

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
    }
    return header


def getBody(filePath):
    binfile = open(filePath, 'rb')
    data = binfile.read()
    return data

def main(filepath):
    r = requests.post(URL,headers=getHeader(ImageName,ImageUrl),data=getBody(filepath))
    cc=r.json()
    #print(type(cc))
    label=cc["data"]['fileList'][0]['label']
    out=read_xlsx.label2class(label)
    #if out['classx']!=None:
    outee="这是"+out['object']
    #else:
        #outee="这是"+out['object']
    #print(outee)

    return outee

if __name__=='__main__':
  filpath="./1.jpg"

  main(filpath)