from flask import Flask

app = Flask(__name__)
print('Successfully imported modules')


# %%
@app.route('/')
def hello_world():
    print('Returning Hello World')
    return '<h1>Hello, World!</h1>'
