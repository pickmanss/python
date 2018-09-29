import re, os, zipfile
from unrar import rarfile

'''
rar = rarfile.RarFile('f:\\test\\old\\test1.rar') #打开压缩包 (图1)
#解析压缩包列表,循环
for file in rar.namelist(): 
    if file.endswith('.txt'):#判断文件类型
        if '解壓密碼' in re.findall('解壓密碼', file):#判断文件名
            pass
        else:
            rar.extract(file, 'f:\\test\\txt')#解压文件
            print(os.listdir('f:\\test\\txt'))#打印txt文件夹中文件名列表

'''

def rar_extract(rar, txt_addr): #解压文件函数
    print(rar)
    print(rar.namelist())
    #解析压缩包列表,循环
    for file in rar.namelist():
        if file.endswith('.txt'):   #判断文件类型
            if '解壓密碼' in re.findall('解壓密碼',file):   #判断文件名
                pass
            else:
                rar.extract(file, txt_addr)     #解压文件
                print(os.listdir(txt_addr))     #打印txt文件夹中的文件名列表
        else:
            pass

def IF_rar(addr, txt_addr):     #识别rar格式压缩包
    print(txt_addr)
    rarfiles = os.listdir(addr)
    print('IF_rar:', rarfiles)
    for rarfile in rarfiles:
        if rarfile.endswith('.zip'):   #判断ZIP文件
        #if rarfile.endswith('.rar'):   #判断RAR文件
            raraddr = os.path.join(addr, rarfile)  #压缩包地址
            rar = zipfile.ZipFile(raraddr)   #解析压缩包(图4)
            #rar = rarfile.RarFile(raraddr)  #解析压缩包(图3)
            #rar = rarfile.RarFile('f:\\test\\old\\test1.rar')   #解析压缩包 (图2)
            rar_extract(rar, txt_addr)  #解压文件函数
        else:
            pass

def main():
    #输入压缩包地址
    addr = input('pls input the PATH of rarfiles:',)
    #输入解压后TXT文件存放地址
    txt_addr = input('pls input the PATH of txtfiles:',)
    #识别rar或zip格式压缩包
    IF_rar(addr, txt_addr)
    
main()

