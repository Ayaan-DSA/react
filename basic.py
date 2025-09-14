from flask import Flask, request , make_response

app = Flask(__name__)

@app.route("/hello")
def hello():
 response = make_response()
 response.status_code = 202
 response.headers['content-type'] = 'application/ocetet-stream'
 return response



@app.route('/add/<int:num1>/<int:num2>' )
def add(num1,num2):
    return f'{num1}+{num2} = {num1 + num2}'

@app.route('/handle')
def handle():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
            greeting = request.args['greeting']
            name = request.args.get('name')
            return f'{greeting} , {name}'
    else:
         return ' Parameters are missing'   
if __name__ == "__main__":
    app.run(debug=True)
