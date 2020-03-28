#Flask
from flask import Flask, request, render_template, flash, url_for, redirect
#Arudino関連
import serial,time
#データベース
from db import *
#Eメール
from send_email import *


def open_key(): #鍵を開ける
    ser = serial.Serial('COM6',9600)
    ser.write(b'1')

def get_status(): #鍵が開いているかの状態を取得
    ser = serial.Serial('COM6',9600)
    key_status = ser.read()

    def b_to_bool(ser): #バイナリをTrue or Falseに変換
        if ser == b'0':
            return False
        else:
            return True
    
    return b_to_bool(key_status)



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #TOPページ
def form():
    #status = True
    status = get_status() #鍵の状態を読み取り

    if request.method == 'POST': #IDとパスワードの入力を受けた時
        user = session.query(User).get(request.form["id"].strip()) #データベースからIDが一致するものを検索
        if user and hash(str(request.form['pwd']))==user.password:
            if status==True:
                open_key() #鍵を開ける。
                #print("open")
                status = get_status()

                #status = False
                if status == True: #万が一装置が正常に動かなかった場合
                    return render_template('message.html', message='装置にエラーが発生しました。至急確認してください。')
                else:
                    send_email('bunshucho@gmail.com', 'note') #ロックが解除された旨をメールで通知
                    return render_template('opened.html')
            else:
                return render_template('already_opened.html')
        else:
            return render_template('not_opened.html', status="ロックされていません！！")

    else:
        status = get_status()
        if status==True:
            return render_template('mainpage.html', status="OK")
        else:
            return render_template('mainpage.html', status="ロックされていません！！")


@app.route('/confirm', methods=['GET', 'POST']) #IDを忘れた方のためのページ
def confirm():
    if request.method == 'POST':
        users = session.query(User).filter(User.email == request.form['adress']).all() #Eメールアドレスを元にユーザーを検索
        if users:
            for user in users:
                send_email(user.email, 'confirm', id_=user.name)
            return render_template('message.html', message='メールを送信しました。') #メールでIDを通知
        else:
            return render_template('message.html', message='入力されたメールアドレスは登録されていません。')
    
    else:
        return render_template('confirmation.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug= True)