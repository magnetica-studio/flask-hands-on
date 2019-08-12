
from flask import Flask
app = Flask(__name__)

print('Successfully imported modules')

#%%
@app.route('/')
def hello_world():
    print('returning Hello World')
    return 'Hello, World!'
