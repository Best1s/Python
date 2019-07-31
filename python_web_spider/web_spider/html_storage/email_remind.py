from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
  name,addr = parseaddr(s)
  return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = 'xxxxx@163.com'
password = 'password'
to_addr = 'xxxxxx@qq.com'
smtp_server = 'smtp.163.com'

# 构造 MIMEText对象需要三个参数 正文 ，MIME的subtype  ‘palin’代表纯文本 ，编码格式
msg = MIMEText('内容 测试','plain','utf-8')
msg['From'] = _format_addr('xxxx <%s>' % from_addr)
msg['To'] = _format_addr('xxx<%s>' % to_addr)
msg['Subject'] = Header('xxxxxx','utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server,quit()