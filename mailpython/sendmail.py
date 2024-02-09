from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.utils import formatdate
from datetime import datetime
from email.mime.image import MIMEImage
import glob
import smtplib
import os

def mailSend(from_email, to_email):

  # smtpobj = smtplib.SMTP('arc-mec.co.jp', 587)
  # smtpobj.ehlo()
  # smtpobj.starttls()
  # smtpobj.ehlo()
  # smtpobj.login('sawa_hiroyuki@arc-mec.co.jp', 'tX7FnseE')
  
  smtpobj = smtplib.SMTP('smtp.gmail.com', 465)
  smtpobj.starttls()
  smtpobj.login('yrfrkw42@gmail.com', 'Ktyt286016')
  
  msg = MIMEMultipart()
  msg['Subject'] = 'submain'
  msg['From'] = from_email
  msg['To'] = ",".join(to_email)
  msg['Date'] = formatdate()
  print(msg)
  msg.attach(MIMEText('mailmain'))
  # ファイル読込
  now = datetime.now()
  nowstr = now.strftime("%Y%m%d")
  path = "./img/"
  filename = nowstr + ".png"
  reserch = os.path.exists(path+filename)

  if reserch == True:
    with open(path+filename, 'rb') as f:
      attach = MIMEApplication(f.read())
      attach.add_header('Content-Disposition', 'attachment', filename=filename)
      msg.attach(attach)

  imgfile = glob.glob(path+"*.png")

  for file in imgfile:
    if os.path.isfile:
      fname = os.path.basename(file)
      part = MIMEBase('application', 'octet-stream')
      part.set_payload(open(file, 'rb').read())
      encoders.encode_base64(part)
      part.add_header('Content-Disposition', 'attachment', filename=fname)
      msg.attach(part)

# smtpobj.sendmail('sawa_hiroyuki@arc-mec.co.jp', 'furukawa_yuri@arc-mec.co.jp', msg.as_string())
# smtpobj.close()

# def sendError(from_email, to_email):
  try:
    smtpobj.sendmail(from_email, to_email, msg.as_string())
  except smtplib.SMTPServerDisconnected as e:
    print('サーバーのエラー発生', e)
  except smtplib.SMTPSenderRefused as e:
    print('送信者アドレスが拒否されました。', e)
  except smtplib.SMTPRecipientsRefused as e:
    print('すべての受信者アドレスが拒否されました。', e)
  except smtplib.SMTPDataError as e:
    print('SMTP サーバーは、メッセージ データの受け入れを拒否しました。', e)
  except smtplib.SMTPConnectError as e:
    print('サーバーとの接続の確立中にエラーが発生しました。', e)
  except smtplib.SMTPHeloError as e:
    print('サーバーはメッセージを拒否しました。', e)
  except smtplib.SMTPNotSupportedError as e:
    print('試行されたコマンドまたはオプションは、サーバーでサポートされていません。', e)
  except smtplib.SMTPAuthenticationError as e:
    print('SMTP認証がうまくいきませんでした。', e)
  except smtplib.SMTPResponseException as e:
    print('コードエラー', e)
  except smtplib.SMTPException as e:
    print('エラー', e)
  else:
    print('メールを送信しました。')
  finally:
    smtpobj.close()

# sendError(msg['From'], msg['To'])
aiueo = ['furukawa_yuri@arc-mec.co.jp']
mailSend('yrfrkw42@gmail.com', aiueo)