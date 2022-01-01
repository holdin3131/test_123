from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi

client = MongoClient('mongodb+srv://test:sparta@cluster0.v6ewu.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=certifi.where())
db = client.dbsparta

@app.route('/')
def home():


    return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():


    comment_receive = request.form['comment_give']
    name_receive = request.form['name_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.logs.insert_one(doc)

    return jsonify({'msg': "저장 완료!"})


@app.route("/homework", methods=["GET"])
def homework_get():

    log_list = list(db.logs.find({}, {'_id': False}))

    return jsonify({'log': log_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
