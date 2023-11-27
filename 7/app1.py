import os
from flask import Flask, request

app = Flask(__name__)
APP_PORT = 5000
RESPONSE_FORMAT = '<body style="background:{color};color:white"><b style="font-family:comic-sans;font-size:60px">{text}</b></div>'

@app.route('/')
def hello_world():
    log_file_path = f'./logs/{request.remote_addr}.log'
    if os.path.exists(log_file_path):
        with open(log_file_path) as buff:
            name = buff.read()
            return RESPONSE_FORMAT.format(color='green', text=f'Welcome back, {name.capitalize()}! I recognized you.')
    return RESPONSE_FORMAT.format(color='red', text='Enter your name under http://thisapp:{}/{{name}} so I can get to know you!'.format(APP_PORT))

@app.route('/<name>')
def logger(name):
    if name.startswith('favicon'):
        return ''

    logs_directory = os.path.join(os.getcwd(), 'logs')
    if not os.path.exists(logs_directory):
        os.mkdir(logs_directory)

    log_file_path = os.path.join(logs_directory, f'{request.remote_addr}.log')
    with open(log_file_path, 'w') as buff:
        buff.write(name)

    return RESPONSE_FORMAT.format(color='blue', text=f'Hello, {name.capitalize()}! Now I know you.')

if __name__ == '__main__':
    app.run('0.0.0.0', APP_PORT)