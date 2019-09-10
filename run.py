import audio_text
import test_webtts
import recongnize,threading
import os


CUR_PATH = r'./audio'
PIC_PATH = r'./img'

def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


while(1):
    phase=audio_text.audio_text()
    if phase=='小北小北':
        while(1):
            test_webtts.main("您好,我是、智能垃圾分类系统,小北,请问,有什么可以帮您？")
            t1=audio_text.audio_text()
            if t1=='垃圾分类':
                test_webtts.main('好的，正在为您，开启智能识别！')
                t_cam = threading.Thread(target=recongnize.cam())  # 函数名不能带括号
                t_cam.start()
            if t1=='结束分类':
                test_webtts.main("好的，期待再次，为您服务！")
                break

        del_file(CUR_PATH)
        del_file(PIC_PATH)
        break
