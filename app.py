from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template("static/index.html")

@app.route('/wordcloud.html')
def wordcloud():  # put application's code here
    return render_template("static/wordcloud.html")

@app.route('/timeline.html')
def timeline():  # put application's code here
    return render_template("static/timeline.html")

@app.route('/topic.html')
def topic():  # put application's code here
    return render_template("static/topic.html")

@app.route('/hottopic.html')
def hottopic():  # put application's code here
    return render_template("static/hottopic.html")

@app.route('/network.html')
def network():  # put application's code here
    return render_template("static/network.html")

@app.route('/emotion.html')
def emotion():  # put application's code here
    return render_template("static/emotion.html")

@app.route('/hotemotion.html')
def hotemotion():  # put application's code here
    return render_template("static/hotemotion.html")

@app.route('/toplist.html')
def toplist():  # put application's code here
    return render_template("static/toplist.html")

if __name__ == '__main__':
    app.run()
