import re

class IdeaTableToJava(object):

    def getSrc(self,filesrc):
        with open(filesrc, "r", encoding='UTF-8') as f:  # 设置文件对象
            for line in f.readlines():
                line = line.strip('\n')
                fild_name = line.split("-")[0]  # 字段名称
                fild_type = line.split("-")[1]  # 字段类型
                java_desc = line.split("-")[2]  # 字段描述
                java_type = self.get_java_type(fild_type)  # 获取java变量类型
                java_name = self.get_java_name(fild_name)  # 获取java变量名称
                file = 'private ' + java_type + ' ' + java_name + ';//' + java_desc
                print(file)


    def get_java_type(self,fild_type):
        if re.match(r'(varchar)|(date)', fild_type):
            return 'String'
        elif re.match(r'number\(\d\)', fild_type):
            return 'int'
        elif re.match(r'number\(\d{2}\)', fild_type):
            return 'long'

    def get_java_name(self,fild_name):
        # 这里re.sub()函数第二个替换参数用到了一个匿名回调函数，回调函数的参数x为一个匹配对象，返回值为一个处理后的字符串
        sub = re.sub(r'(_\w)', lambda x: x.group(1)[1].upper(), fild_name)
        return sub
user = IdeaTableToJava()
user.getSrc('D:/home/6.txt')


