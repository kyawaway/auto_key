from flask import Flask, request, render_template, flash, url_for, redirect
import serial,time
import os

def open_key(): #鍵を開ける
    ser = serial.Serial('COM6',9600)
    ser.write(b"1")

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

@app.route('/', methods=['GET', 'POST'])
def form():
<<<<<<< HEAD
    status = False #本当は電流が流れているかから読み取る。Trueなら鍵が閉まっていて、Falseなら空いている。
=======
    #status = False
    status = get_status() #鍵の状態を読み取り
>>>>>>> tehhuu
    if request.method == 'POST':
        print("POSTされたIDは？" + str(request.form['id']))
        print("POSTされたPASSWORDは？" + str(request.form['pwd']))
        if str(request.form['id'])==idid and str(request.form['pwd'])==ps:
            if status==False:
                open_key() #鍵を開ける。
                status = get_status()
                #status = True
                if status != True:
                    return render_template('error.html')
                else:
                    return render_template('opened.html')
            else:
                return render_template('already_opened.html')
        else:
            return render_template('not_opened.html', status="ロックされていません！！")

    else:
        if status==True:
            return render_template('index.html', status="OK")
        else:
            return render_template('index.html', status="ロックされていません！！")

if __name__ == "__main__":
<<<<<<< HEAD
    idid = 'aaa' #適宜設定
    ps = 'bbb' #適宜設定
    app.run(host='0.0.0.0', debug= True)
=======
    app.secret_key = os.urandom(12)
    idid = 'a' #適宜設定
    ps = 'b' #適宜設定
    app.run(host='0.0.0.0', debug= True)
>>>>>>> tehhuu
