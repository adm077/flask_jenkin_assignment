from flask import Flask
app = Flask(_name_)

@app.route('/', method=['GET'])
def helloworld():
    return 'Hellow World'

if _name_ == "_main_":
    app.run(port=3000, debug=True)
