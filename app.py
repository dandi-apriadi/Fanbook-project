from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://dandi:Malware21@cluster0.gfzf0gt.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name' :name_receive,
        'comment' :comment_receive
    }
    db.Fanbook.insert_one(doc)
    return jsonify({'msg':'Comment Succes!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    message_list = list(db.Fanbook.find({},{'_id':False}))
    return jsonify({'Message':message_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)