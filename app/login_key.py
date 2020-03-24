from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    status = False #本当は電流が流れているかから読み取る
    if request.method == 'POST':
        print("POSTされたIDは？" + str(request.form['id']))
        print("POSTされたPASSWORDは？" + str(request.form['pwd']))
        if str(request.form['id'])==idid and str(request.form['pwd'])==ps:
            if status==False:
                ###
                #ロック解除の処理をここに書く
                ###
                status = True #本当は電流が流れているかから読み取る
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
    idid = 'aaa'
    ps = 'bbb'
    app.run(host='0.0.0.0', debug= True)
