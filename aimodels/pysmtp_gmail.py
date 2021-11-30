# -*- coding:utf-8 -*-
 # SMTP : Simple Mail Transfer Protocol
import smtplib                       # 파이썬에서 메일을 보낼 수 있는 라이브러리
from email.mime.text import MIMEText # 아래의 텍스트를 본문에 넣을 수 있는 메서드
 
smtp = smtplib.SMTP('smtp.gmail.com', 587) # 기본적으로 587번 포트 사용
smtp.ehlo()      # say Hello : 서버가 살아있는지 응답을 받기 위함

# 지메일은 보안상의 이유로 SMTP연결을 TLS(전송 계층 보안) 모드로 설정해
smtp.starttls()  # TLS 사용시 필요 : 보안을 중시하면 send 대신 starttls 사용(구글은 starttls만 사용 가능)
#smtp.login('자신의ID@gmail.com', '자신의 gmail앱_비밀번호')
smtp.login('starsbk7@gmail.com', 'gxmxupzjwbiyahlg')

###################### 로그인, mail을 보내기 위한 setting ####################
###################### 실제 mail을 보내는 action(by 'sendmail' 메서드)

# 보낼 메시지 작성
msg = MIMEText('본문 테스트 메시지 잘 갔으면 좋겠네.')
msg['Subject'] = '메일 테스트'           # mail title
msg['To'] = 'tmdqlsrla11@naver.com'     # 수신자
# smtp.sendmail('송신자', '수신자', '메시지')
smtp.sendmail('starsbk7@gmail.com', 'tmdqlsrla11@naver.com', msg.as_string())
 
smtp.quit()