from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from pymongo import MongoClient
from mysql.connector import connect
import requests
import subprocess

app=Flask(__name__)
app.config['SECRET_KEY']="SECRET_KEY"
jwt=JWTManager(app)


mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["sms_config"]
config_collection = mongo_db["country_operator"]

mysql_conn = connect(
    host="localhost", user="root", password="password", database="sms_metrics"
)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Invalid token!'}), 403
        return f(*args, **kwargs)
    return decorated

@app.route('/session/<action>/<program_name>',methods=['POST'])
@token_required

def manage_session(action,program_name):
    if action not in ['start','stop','restart']:
        return jsonify({"message":"invalid action"}),400
    command=f"screen -S {program_name} -x {action}" 
    try:
        subprocess.run(command,shell=True,check=True)
        return jsonify({'message':f'{action} session:{program_name}'})
    except subprocess.CalledProcessError:
        return jsonify({'message':f'Failed to {action} session: {program_name}'})
    
if __name__=="__main__":
    app.run(debug=True)
    
@app.route('/metrics',methods=['GET'])
def get_metrics():
    data={
        'total_sms_sent':1000,
        'success_rate':95,
        'failure_rate':5
    }
    return jsonify(data),200


@app.route('/country_operator',methods=['POST'])
def add_country_operator():
    data=request.json
    config_collection.insert_one(data)
    return jsonify({'message':'Country-operator pair added'}),201


@app.route('/login',methods=['POST'])
def login():
    auth=request.json
    if auth and auth['username']=='admin' and auth['password']=='admin':
        token=jwt.encode({
            'user':auth['username'],
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
        })
        return jsonify({'token':token})
    return jsonify({'message':'Invalid credentials'}),403


def send_telegram_alert(message: str):
    token = "your_telegram_bot_token"
    chat_id = "your_chat_id"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": message})

@app.route("/alert", methods=["POST"])
def trigger_alert():
    data = request.get_json()
    send_telegram_alert(data["message"])
    return jsonify({"message": "Alert sent"}), 200


