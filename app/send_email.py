import smtplib
from email.message import EmailMessage

def send_email(adress, tp, id_=''):
    msg = EmailMessage()
    
    if tp == 'confirm':
        msg.set_content('Your ID is\n\n' + id_)
        msg['Subject'] = 'ID通知'
    elif tp== 'note':
        msg.set_content('閉めルンですによりロックが解除されました。\n操作に覚えがない場合は至急確認を行ってください。 ')
        msg['Subject'] = '（要確認）ロックが解除されました'

    msg['From'] = 'shimerundesu@gmail.com'
    msg['To'] = adress

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('shimerundesu@gmail.com', 'a_team_a') #送信元アカウントとそのパスワード

    s.send_message(msg)
    s.quit()


if __name__ == "__main__":
    #テスト用
    send_email('メールアドレス', tp='confirm', id_='test')