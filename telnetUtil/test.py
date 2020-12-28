import telnetlib
import time

_UsermodTag = '>'

# 接口配置
# router 路由器ip, password 密码, intType 接口类型, intId 接口号, ip 配置ip, mask 掩码
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
    time.sleep(1)
    tn.write(b'int ' + intType.encode('utf-8') + intId.encode('utf-8') + b'\n')
    time.sleep(1)
    print('int ' + intType + intId)
    tn.write(b'ip address ' + ip.encode('utf-8') + b' ' + mask.encode('utf-8') + b'\n')
    print('ip address ' + ip + ' ' + mask)
    time.sleep(1)
    tn.write(b'no shutdown' + b'\n')
    time.sleep(1)
    tn.write(b'exit' + b'\n')
    time.sleep(1)
    tn.write(b'exit' + b'\n')
    print('---finish config interface--')
    tn.close()


# RIP配置
# router  路由器ip,password 密码, net 子网ip
def configRIP(router, password, net):
    # login
    print('--start config network--')
    tn = telnetlib.Telnet(router, port=23, timeout=10)
    tn.set_debuglevel(0)
    tn.read_until(b'Password: ')
    tn.write(b'CISCO' + b'\n')
    tn.read_until(b'Router>')
    print('login success')

    # configure
    tn.write(b'enable' + b'\n')
    tn.read_until(b'Password: ')
    tn.write(password.encode('utf-8') + b'\n')
    tn.read_until(b'Router#')
    print("yes")
    tn.write(b'config terminal' + b'\n')
    print('config terminal')
    time.sleep(1)
    tn.write(b'router rip' + b'\n')
    time.sleep(1)
    tn.write(b'network ' + net.encode('utf-8'))
    time.sleep(1)
    tn.write(b'exit' + b'\n')
    time.sleep(1)
    tn.write(b'exit' + b'\n')
    print('---finish subnet config---')
    tn.close()


# 获取路由表
# router  路由器ip,password 密码
# 返回：string 路由器路由表信息
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


# debug
def debug(router, password):
    print('start config int ')
    tn = telnetlib.Telnet(router, port=23, timeout=10)
    tn.set_debuglevel(0)
    tn.read_until(b'Password: ')
    tn.write(b'CISCO' + b'\n')
    tn.read_until(b'Router>')
    print('login success')
    tn.write(b'enable' + b'\n')
    tn.read_until(b'Password: ')
    tn.write(password.encode('utf-8') + b'\n')
    tn.read_until(b'Router#')
    print("yes")
    # tn.write(b'config terminal' + b'\n')
    print('config terminal')
    time.sleep(1)
    tn.write(b'debug ip packet' + b'\n')
    time.sleep(1)
    tn.write(b'undebug all')
    response = tn.read_until(_UsermodTag.encode())
    print(response.decode())
    tn.close()


# test dynamic route
if __name__ == '__main__':
    showIpRoute("2.2.2.3")
    # configInt("2.2.2.5", "CISCO","f0","/0","10.0.0.2","255.255.255.0")
    # configRIP("2.2.2.3", "CISCO", "192.168.2.0")
    # debug("2.2.2.3")
