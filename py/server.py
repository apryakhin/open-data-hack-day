import os
import sentiment
from flask import Flask, request, jsonify


__app_root__ = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('/put', methods=['GET', 'POST'])
def task():
    query = request.values.get('q')
    return jsonify(sentiment.process(query))


def start_server():
    app.run(host='0.0.0.0', port=8084, debug=False)

if __name__ == '__main__':
    # pool = Pool(__num_workers__)
    # for i in xrange(0, __num_workers__):
    #     pool.apply_async(start_worker, args=((i), ))
    start_server()
    # pool.close()
    # pool.join()
