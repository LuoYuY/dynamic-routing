import telnetlib
import time
import re


_UsermodTag = '>'
class telnetUtil:
    # 接口配置
    def configInt(router, password, intType, intId, ip, mask):
        print('--start config interface--')
        # login
        tn = telnetlib.Telnet(router, port=23, timeout=10)
        tn.set_debuglevel(0)
        tn.read_until(b'Password: ')
        tn.write(password.encode('utf-8') + b'\n')
        tn.read_until(b'Router>')
        print('login success')

        # configure
        tn.write(b'enable' + b'\n')
        tn.read_until(b'Password: ')
        tn.write(b'CISCO' + b'\n')
        tn.read_until(b'Router#')
        tn.write(b'config terminal' + b'\n')
        print('config terminal')
        time.sleep(0.2)
        tn.write(b'int ' + intType.encode('utf-8') + intId.encode('utf-8') + b'\n')
        time.sleep(0.2)
        print('int ' + intType + intId)
        tn.write(b'ip address ' + ip.encode('utf-8') + b' ' + mask.encode('utf-8') + b'\n')
        print('ip address ' + ip + ' ' + mask)
        time.sleep(0.2)
        tn.write(b'no shutdown' + b'\n')
        time.sleep(0.2)
        tn.write(b'exit' + b'\n')
        time.sleep(0.2)
        tn.write(b'exit' + b'\n')
        print('---finish config interface--')
        tn.close()

    # RIP配置
    def configRIP(router, password, netList):
        # login
        print('--start config network--')
        tn = telnetlib.Telnet(router, port=23, timeout=10)
        tn.set_debuglevel(0)
        tn.read_until(b'Password: ')
        tn.write(b'CISCO' + b'\n')
        tn.read_until(b'Router>')
        print('login success')

        print(router)
        # configure
        tn.write(b'enable' + b'\n')
        tn.read_until(b'Password: ')
        tn.write(password.encode('utf-8') + b'\n')
        tn.read_until(b'Router#')
        print("yes")
        tn.write(b'config terminal' + b'\n')
        print('config terminal')
        # time.sleep(1)
        tn.write(b'router rip' + b'\n')
        print('router rip')
        time.sleep(0.5)
        for net in netList:
            tn.write(b'network ' + net.encode('utf-8') + b'\n')
            print('network ' + net)
            time.sleep(0.3)
        # time.sleep(1)
        tn.write(b'exit' + b'\n')
        # time.sleep(1)
        tn.write(b'exit' + b'\n')
        print('---finish subnet config---')
        tn.close()

    # 获取路由表
    def showIpRoute(router, password):
        print('--- start: get route --- ')
        # login
        tn = telnetlib.Telnet(router, port=23, timeout=10)
        tn.set_debuglevel(0)
        tn.read_until(b'Password: ')
        tn.write(password.encode('utf-8') + b'\n')
        tn.read_until(b'Router>')
        print('login success')

        # show ip route
        tn.write(b'show ip route' + b'\n')
        response = tn.read_until(_UsermodTag.encode())
        print(response.decode())
        tn.close()
        print('--- finish: get route --- ')
        return response.decode()

    #get result: show interface s0/0/0
    def showInterface(router, password, intType, intId):
        print('--- start: get route --- ')
        # login
        tn = telnetlib.Telnet(router, port=23, timeout=10)
        tn.set_debuglevel(0)
        tn.read_until(b'Password: ')
        tn.write(password.encode('utf-8') + b'\n')
        tn.read_until(b'Router>')
        print('login success')

        # show ip route
        tn.write(b'show int '+ intType.encode('utf-8') + intId.encode('utf-8') + b'\n')
        response = tn.read_until(b'MTU')
        print(response.decode())
        tn.close()
        print('--- finish: get route --- ')
        return response.decode()

    # 启动进程交换
    def close(router, password) :
        print('--- start: close --- ')
        # login
        tn = telnetlib.Telnet(router, port=23, timeout=10)
        tn.set_debuglevel(0)
        tn.read_until(b'Password: ')
        tn.write(password.encode('utf-8') + b'\n')
        tn.read_until(b'Router>')
        print('login success')

        tn.write(b'enable' + b'\n')
        tn.read_until(b'Password: ')
        tn.write(password.encode('utf-8') + b'\n')
        tn.read_until(b'Router#')
        tn.write(b'config terminal' + b'\n')
        print('config terminal')
        time.sleep(0.2)

        tn.write(b'int f0/1' + b'\n')
        time.sleep(0.2)
        tn.write(b'no ip route-cache' + b'\n')
        tn.write(b'exit' + b'\n')

        tn.write(b'int s0/0/0'+b'\n')
        time.sleep(0.2)
        tn.write(b'no ip route-cache'+ b'\n')
        tn.write(b'exit' + b'\n')

        tn.write(b'int s0/0/1' + b'\n')
        time.sleep(0.2)
        tn.write(b'no ip route-cache' + b'\n')
        tn.write(b'exit' + b'\n')
        tn.write(b'exit' + b'\n')
        tn.close()

    # debug 返回debug信息
    def debug(router, password, destNet, destIp):
        print('start config int ')
        tn = telnetlib.Telnet(router, port=23, timeout=10)
        tn.set_debuglevel(0)
        tn.read_until(b'Password: ')
        tn.write(password.encode('utf-8') + b'\n')
        tn.read_until(b'Router>')
        print('login success')
        tn.write(b'enable' + b'\n')
        tn.read_until(b'Password: ')
        tn.write(password.encode('utf-8') + b'\n')
        tn.read_until(b'Router#')
        print("yes")
        tn.write(b'terminal monitor' + b'\n')
        print('----open terminal monitor----')
        # fliter
        tn.write(b'config terminal' + b'\n')
        tn.write(b'access-list 101 permit icmp any '+ destNet.encode('utf-8') + b' 0.255.255.255' + b'\n')

        tn.write(b'exit' + b'\n')
        tn.write(b'debug ip packet 101' + b'\n')
        tn.write(b'ping ' + destIp.encode('utf-8') + b'\n')
        time.sleep(2)

        tn.write(b'undebug all'+ b'\n')
        response = tn.read_until(b'All possible')

        # save result to 'result.txt'
        result = response.decode()
        fh = open('result.txt', 'w', encoding='utf-8')
        fh.write(result)
        fh.close()

        tn.close()

    # 判断接口启用情况
    def isUp(result) :
        #pattern=re.compile(r'^[A-Za-z0-9]+[u,p]{2}[A-Za-z0-9]*')
        pattern=re.compile(r'up')
        if pattern.search(result.split('\n')[1]) :
            print(len(pattern.search(result).span()))
            res = len(pattern.search(result).span())
            if res < 2 :
                return False
            return True
        else :
            print('None')
            return False

    # 子网掩码转换
    def exchange_maskint(mask_int):
        bin_arr = ['0' for i in range(32)]
        for i in range(mask_int):
            bin_arr[i] = '1'
        tmpmask = [''.join(bin_arr[i * 8:i * 8 + 8]) for i in range(4)]
        tmpmask = [str(int(tmpstr, 2)) for tmpstr in tmpmask]
        return '.'.join(tmpmask)

    # 获取接口的ip和mask
    def getIntIpMask(result) :
        pattern=re.compile(r'up')
        line = result.split('\n')[3]
        ip_mask = line.split(' ')[5]
        print("ip_mask: "+ip_mask)
        ip = ip_mask.split('/')[0]
        mask_num = ip_mask.split('/')[1]
        print('mask_num:'+mask_num)
        mask = exchange_maskint(int(mask_num))
        return ip,mask

# test dynamic route/
if __name__ == '__main__':
    pass


    # result =  showInterface(router, password, intType, intId)
    result = "show int s0/0/0\r\nSerial0/0/0 is down, line protocol is down \r\n  Hardware is GT96K Serial\r\n  Internet address is 192.168.2.2/24\r\n  MTU"
    print(getIntIpMask(result))
    # configInt("192.168.3.2", "CISCO", "f0", "/0", "10.0.0.1", "255.255.255.0")
    # configInt("192.168.3.2", "CISCO", "s0", "/0/0", "192.168.1.2", "255.255.255.0")
    # configInt("192.168.3.1", "CISCO", "s0", "/0/0", "192.168.2.1", "255.255.255.0")
    # configInt("192.168.3.1", "CISCO", "s0", "/0/1", "192.168.1.1", "255.255.255.0")
    # configInt("192.168.3.3", "CISCO", "f0", "/0", "10.0.0.2", "255.255.255.0")
    # configInt("192.168.3.3", "CISCO", "s0", "/0/0", "192.168.2.2", "255.255.255.0")
    # # # #
    # rta = [ "192.168.1.0", "10.0.0.0"]
    # rtb = [ "192.168.1.0", "192.168.2.0", "192.168.3.0"]
    # rtc = [ "192.168.2.0", "10.0.0.0" ]
    # configRIP("192.168.3.2", "CISCO", rta)
    # configRIP("192.168.3.1", "CISCO", rtb)
    # configRIP("192.168.3.3", "CISCO", rtc)
    # time.sleep(0.3)
    # # # #
    # showIpRoute("192.168.3.1","CISCO")
    # close("192.168.3.1","CISCO")
    # result = showInterface("192.168.3.1","CISCO",'s0', '/0/0')
    # isUp(result)
    # getIntIpMask(result)
    # debug("192.168.3.1","CISCO","10.0.0.0","10.0.0.1")
