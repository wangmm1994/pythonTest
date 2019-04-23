import os
import shutil

class IdeaJavaExport(object):
    def __init__(self):
        self.local_file = 'D:/educloud_app/src/'
        self.to_file = 'C:/Users/wangj/Desktop/ideaJava/src/'

    def getSrc(self,filesrc):
        with open(filesrc, "r") as f:  # 设置文件对象
            for line in f.readlines():
                line = line.strip('\n')
                pos = line.rfind("/")
                path = line[:pos + 1]
                # file = line[pos+1:]
                self.mkdir(path,line)

    def mkdir(self,path,line):
        path = self.to_file + path
        srcFile = self.local_file + line
        print('源文件:',srcFile,' 目标路径:',path)
        # 去除首位空格
        path = path.strip()
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            os.makedirs(path)
            print('目标目录创建成功！！')
            shutil.copy(srcFile, path)
            print('-------------------复制',srcFile,'到',path,'成功！！！')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            shutil.copy(srcFile, path)
            print('目标目录已经存在','-------------------复制', srcFile, '到', path, '成功！！！')
            return False
user = IdeaJavaExport()
user.getSrc('D:/home/5.txt')