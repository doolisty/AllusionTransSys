from flask_bootstrap import Bootstrap
from flask import Flask, request, render_template, g
import config
import os

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        content = request.form.get("content")
        return render_template("response.html", content=content)


@app.route('/response/', methods=['GET', 'POST'])
def response():
    # --------------------------------------------------------------------------
    # add back-end code here
    #
    # including: link database, return corresponding records
    # store result in a list 'Result', regulated in
    #
    # Result =
    # [
    #   {
    #       u'所在段': int,
    #       u'所在行': int,
    #       u'原文': string ('first 3 words' + '...'),
    #       u'典故': string (name of allusion, meanwhile key of a record in db),
    #       u'含义': string (interpretation of allusion, meanwhile content of a record in db)
    #   },
    #   ......
    # ]
    # ---------------------------------------------------------------------------
    result = [
        {
            u'所在段': 2,
            u'所在行': 2,
            u'原文': "original text",
            u'典故': "allusion",
            u'含义': "meaning"
         }
    ]  # store result in this dict, here is for debugging
    g.result = result
    if request.method == 'GET':
        return render_template("response.html", result=result)
    else:
        content = request.form.get("content")
        return render_template("response.html", result=result, content=content)


@app.route('/savefile/', methods=['GET', 'POST'])
def savefile():
    if request.method == 'GET':
        return render_template("savefile.html")
    if request.method == 'POST':
        filepath = request.form.get("filepath")
        save_result = ""
        for i in g.result:
            for key, value in i.items():
                save_result += key + str(value) + "\n"
        if not os.path.exists(os.path.split(filepath)[0]):
            os.makedirs(os.path.split(filepath)[0])
        try:
            with open(filepath, 'wb') as f:
                f.write(save_result.encode('utf8'))
            print('保存成功')  # 改为消息闪现
        except Exception as e:
            print('保存失败', e)


if __name__ == '__main__':
    app.run(debug=True)
