from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'helo world'

if __name__ == "__main__":
    app.run(debug=True)

''' it will create web page and print helo world 
for executing file type - python ./first_page.py
'''
