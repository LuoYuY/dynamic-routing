import telnetlib
import time
### 配置登录信息
#_Username = 'r'
_Password = 'CISCO'
_Host = '192.168.1.1'
# 命令结束提示符
# 正常模式如<R1> 来提示用户输入命令，所以取>为作为标志符
_UsermodTag = '>'
# system-view模式如[R1] 来提示用户输入命令，所以取]为作为标志符
_SysrmodTag = ']'

# 实例化telnet对象，建立一个主机连接
telnetsession = telnetlib.Telnet(_Host)
# 开启调试，按需开启，方便判断
#telnetsession.set_debuglevel(2)
# read_until()来判断缓冲区中的数据是否有想要的内容，如果没有就等待
# 当然也可以使用expect方法，与read_until差不多，但是它可以支持正则表达式，功能要强大得多
# 区配字符，当出现'Username'时，输入用户名
login_prompt = b'Username'
response = telnetsession.read_until(login_prompt)
if login_prompt in response:
    pass
    #print response
    #print ('[*] Username: ',_Username)
#telnetsession.write(_Username.encode('ascii')+ b'\n')
time.sleep(5)
# 区配字符，当出现'Password'时，输入密码
password_prompt = 'Password'
response = telnetsession.read_until(password_prompt.encode('ascii'))
if password_prompt.encode('ascii') in response:
    print ('[*] Password: ',_Password)
    time.sleep(2)
telnetsession.write(_Password.encode('ascii')+b'\n')
# 如果登录成功，则出现类似<R1>,使用_UsermodTag来进行捕获
response = telnetsession.read_until(_UsermodTag.encode('ascii'))
if _UsermodTag.encode('ascii') in response:
    print (response.decode('ascii'))
time.sleep(2)


telnetsession.write("dir\n".encode())
response = telnetsession.read_until(_UsermodTag.encode())
if _UsermodTag.encode('ascii') in response:
    print (response.decode())
time.sleep(2)
#切换到system-view模式
# telnetsession.write("system-view\n".encode())
# # 此时使用_SysrmodTag来进行捕获输出
# response = telnetsession.read_until(_SysrmodTag.encode())
# if _SysrmodTag.encode('ascii') in response:
#     print (response.decode())
# time.sleep(2)
# telnetsession.write("display this\n".encode())
# response = telnetsession.read_until(_SysrmodTag.encode())
# #print(response.decode('ascii'))
# #if _SysrmodTag.encode('ascii') in response:
# print(response.decode('ascii'))
# time.sleep(2)
telnetsession.write("dis ip interface brief\n".encode())
response = telnetsession.read_until(_UsermodTag.encode())
print(response.decode())
#测试完毕后，关闭连接
time.sleep(2)
#测试完毕后，关闭连接
telnetsession.close()
print ('[*] Session Close.')
