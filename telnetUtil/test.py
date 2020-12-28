import telnetlib
import time

Host = "192.168.1.1"

#config Interface
def configInt(router, password,intType,intId,ip,mask):
    print('start config int ')
    tn = telnetlib.Telnet(router, port=23, timeout=10)
    tn.set_debuglevel(0)
    tn.read_until(b'Password: ')
    tn.write(b'CISCO' + b'\n')
    tn.read_until(b'Router>')
    print('login success')
    tn.write(b'enable' + b'\n')
    tn.read_until(b'Password: ')
    tn.write(b'CISCO' + b'\n')
    tn.read_until(b'Router#')
    print("yes")
    # tn.write(password.encode('utf-8') + b'\n')
    # tn.read_until(b'Router#')
    tn.write(b'config terminal' + b'\n')
    print('config terminal')
    time.sleep(1)
    tn.write(b'int ' + intType.encode('utf-8')+intId.encode('utf-8') + b'\n')
    time.sleep(1)
    print('int ' + intType+intId)
    tn.write(b'ip address '+ip.encode('utf-8')+b' '+mask.encode('utf-8') + b'\n')
    print('ip address '+ip+' '+mask)
    time.sleep(1)
    tn.write(b'no shutdown' + b'\n')
    time.sleep(1)
    tn.write(b'exit'+ b'\n')
    time.sleep(1)
    tn.write(b'exit' + b'\n')
    print('finish')
    tn.close()

#config network
def configRIP(router, password,net):
    print('start config int ')
    tn = telnetlib.Telnet(router, port=23, timeout=10)
    tn.set_debuglevel(0)
    tn.read_until(b'Password: ')
    tn.write(b'CISCO' + b'\n')
    tn.read_until(b'Router>')
    print('login success')
    tn.write(b'enable' + b'\n')
    tn.read_until(b'Password: ')
    tn.write(b'CISCO' + b'\n')
    tn.read_until(b'Router#')
    print("yes")
    # tn.write(password.encode('utf-8') + b'\n')
    # tn.read_until(b'Router#')
    tn.write(b'config terminal' + b'\n')
    print('config terminal')
    time.sleep(1)
    tn.write(b'router rip' + b'\n')
    time.sleep(1)
    tn.write(b'network '+ net.encode('utf-8'))
    time.sleep(1)
    tn.write(b'exit'+ b'\n')
    time.sleep(1)
    tn.write(b'exit' + b'\n')
    print('finish subnet config')
    tn.close()

#test dynamic route

if __name__ == '__main__':
    # configInt("2.2.2.5", "CISCO","s0","/0/1","192.168.2.2","255.255.255.0")
    configRIP("2.2.2.3", "CISCO", "192.168.2.0")
    # 连接Telnet服务器
    # tn = telnetlib.Telnet(Host, port=23, timeout=10)
    # tn.set_debuglevel(0)
    # print('yes')
    # # 输入登录用户名
    # #tn.read_until(b'login: ')
    # print("no")
    # #tn.write(b"r" + b'\n')
    # print('yes')
    # # 输入登录密码
    # tn.read_until(b'Password: ')
    # tn.write(b"CISCO" + b'\n')
    # print('yes33')
    # tn.read_until(b'Router>')
    # tn.write(b"show int f0/0" + b'\n')
    # print("a")
    #
    # #tn.read_until(b'#')
    # #tn.write(b"ls -al" + b'\n')
    #
    # r = tn.read_until(b'Hardware').decode('ASCII')
    # print("b")
    # r1 = r.split(r"\r\n")
    # for i in r1:
    #     print(i)
    # tn.close()