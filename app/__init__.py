from flask import  Flask, render_template
import requests
import json

app = Flask(__name__)

# posts =[
#     {'id':'hello', 'age': '12', 'name' : 'Angie'}
# ]

@app.route('/', methods=['GET'])
def home():
    req = requests.get('https://newsapi.org/v2/everything?q=Apple&from=2022-05-01&sortBy=popularity&apiKey=88d9674802b048a3b86ddde3d25291ce')
    data = json.loads(req.content)
    return render_template('news.html', data=data)
