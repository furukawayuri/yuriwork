from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
import os
import glob
from email.mime.base import MIMEBase
from email import encoders

# Gmail設定
my_account = 'yrfrkw42@gmail.com'
my_password = 'psfm oibs hout agee'

def send_gmail(msg):
  """
  引数msgをGmailで送信
  """
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context())
  # ログ出力
  server.set_debuglevel(0)
  # ログインしてメール送信
  server.login(my_account, my_password)
  server.send_message(msg)

def make_mime(mail_to, subject, body):
  """
  引数をMIME形式に変換
  """
  msg = MIMEMultipart()
  msg['Subject'] = subject #件名
  msg['To'] = ",".join(mail_to) #宛先
  msg['From'] = my_account #送信元
  msg.attach(MIMEText(body)) #メッセージ本文
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

  return msg

def send_my_message():
  """
  メイン処理
  """
  # MIME形式に変換
  msg = make_mime(
  mail_to=['yrfrkw42@gmail.com','furukawa_yuri@arc-mec.co.jp'], #送信したい宛先を指定
  subject='テスト件名',
  body='テストです。テストです。テストです。')
  
  try:
    send_gmail(msg)
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
    send_gmail.close()


if __name__ == '__main__':
    send_my_message()
