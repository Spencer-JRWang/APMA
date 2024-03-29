import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.header import Header
from email.utils import formataddr
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_email(toEmailAddrs):
    # 设置服务器所需信息
    fromEmailAddr = 'spencer-jrwang@foxmail.com'  # 邮件发送方邮箱地址
    password = '********************'  # (注意不是邮箱密码，而是为授权码)
    #toEmailAddrs = ['3338561620@qq.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    
    # 设置email信息
    # ---------------------------发送带附件邮件-----------------------------
    # 邮件内容设置
    message =  MIMEMultipart()
    # 邮件主题
    message['Subject'] = 'Auto Protein Mutation Analyzer'
    # 发送方信息
    message['From'] = fromEmailAddr
    # 接受方信息
    message['To'] = toEmailAddrs[0]
    # 邮件正文内容
    html_content = """
<!DOCTYPE html>
<html>
<body>

<img src="cid:image1" style="width:50%; height:auto;">
<h1>Thank you for using APMA</h1>
<h2>Please check the file attached bellow.</h2>
<p>--------------------------------------</p>
<p>Developed by Spencer Wang</p>
</body>
</html>
"""
    # 将HTML内容作为MIMEText的一部分添加到邮件中
    message.attach(MIMEText(html_content, 'html'))

    # 读取图片并添加到邮件中
    with open('/home/wangjingran/APMA/Figure/LOGO.png', 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', '<image1>')
        message.attach(img)

    #message.attach(MIMEText('APMA analyzation is done.\n Please check the file attached bellow.\n--------------------------------------\nDeveloped by Spencer Wang', 'plain', 'utf-8'))
    
    # 构造附件
    att_img2 = MIMEText(open(r'/home/wangjingran/APMA/Email/APMA_outcome.zip', 'rb').read(), 'base64', 'utf-8')
    att_img2['Content-disposition'] = 'attachment;filename="APMA_outcome.zip"'
    message.attach(att_img2)
    # ---------------------------------------------------------------------
    
    # 登录并发送邮件
    try:
        server = smtplib.SMTP('smtp.qq.com')  # qq邮箱服务器地址，端口默认为25
        server.login(fromEmailAddr, password)
        server.sendmail(fromEmailAddr, toEmailAddrs, message.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print("error:", e)

def send_error_email(toEmailAddrs):
    # 设置服务器所需信息
    fromEmailAddr = 'spencer-jrwang@foxmail.com'  # 邮件发送方邮箱地址
    password = 'oqkrrekmykewcjcj'  # (注意不是邮箱密码，而是为授权码)
    #toEmailAddrs = ['3338561620@qq.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    
    # 设置email信息
    # ---------------------------发送带附件邮件-----------------------------
    # 邮件内容设置
    message =  MIMEMultipart()
    # 邮件主题
    message['Subject'] = 'Auto Protein Mutation Analyzer'
    # 发送方信息
    message['From'] = fromEmailAddr
    # 接受方信息
    message['To'] = toEmailAddrs[0]
    # 邮件正文内容
    html_content = """
<!DOCTYPE html>
<html>
<body>

<img src="cid:image1" style="width:50%; height:auto;">
<h2>Oops! Something went wrong, please check your files</h2>
<p>--------------------------------------</p>
</body>
</html>
"""
    # 将HTML内容作为MIMEText的一部分添加到邮件中
    message.attach(MIMEText(html_content, 'html'))

    # 读取图片并添加到邮件中
    with open('/home/wangjingran/APMA/Figure/LOGO.png', 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', '<image1>')
        message.attach(img)

    #message.attach(MIMEText('APMA analyzation is done.\n Please check the file attached bellow.\n--------------------------------------\nDeveloped by Spencer Wang', 'plain', 'utf-8'))
    # ---------------------------------------------------------------------
    
    # 登录并发送邮件
    try:
        server = smtplib.SMTP('smtp.qq.com')  # qq邮箱服务器地址，端口默认为25
        server.login(fromEmailAddr, password)
        server.sendmail(fromEmailAddr, toEmailAddrs, message.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print("error:", e)
