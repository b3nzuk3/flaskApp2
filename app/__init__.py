from flask import  Flask, render_template
from .config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig)

@app.route('/', methods=['GET'])
def home():
    req = requests.get('https://newsapi.org/v2/everything?q=Apple&from=2022-05-01&sortBy=popularity&apiKey=88d9674802b048a3b86ddde3d25291ce')
    data = json.loads(req.content)
    return render_template('news.html', data=data)
