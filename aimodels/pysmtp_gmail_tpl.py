# -*- coding:utf-8 -*-
 # SMTP : Simple Mail Transfer Protocol
import smtplib
from email.mime.text import MIMEText
 
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()      # say Hello

# 지메일은 보안상의 이유로 SMTP연결을 TLS(전송 계층 보안) 모드로 설정해
smtp.starttls()  # TLS 사용시 필요
smtp.login('자신의ID@gmail.com', '자산의 gmail앱_비밀번호')

# 보낼 메시지 작성
msg = MIMEText('본문 테스트 메시지 잘 갔으면 좋겠네.')
msg['Subject'] = '메일 테스트'
msg['To'] = '자산의ID@naver.com'
# smtp.sendmail('송신자', '수신자', '메시지')
smtp.sendmail('자신의ID@gmail.com', '자신의ID@naver.com', msg.as_string())
 
smtp.quit()