import redis
from flask import Flask

app = Flask(__name__)

# conecta no Redis
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    cache.incr('visits')
    return f"Numero de visitas: {cache.get('visits').decode('utf-8')}"

app.run(host='0.0.0.0', port=5000)
