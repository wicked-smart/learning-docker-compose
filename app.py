from flask import Flask
import time
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
	retries = 5
	while True:
		try:
			return cache.incr('hits')

		except redis.exceptions.ConnectionError as exc:
			if retries == 0:
				raise exec
			retries -= 1
			time.sleep(0.5)


@app.route('/')
def hello():
	count = get_hit_count()
	return "Hello, world from Dcoker! I have been seen {} times.".format(count) 



