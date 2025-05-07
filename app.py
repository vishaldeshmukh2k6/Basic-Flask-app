from flask import Flask, jsonify

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/armsg/<int:n>')
def armsg(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10

    if (sum == copy_n):
        # print(f"{copy_n} This is Armostrong Number ")
        result = {
            "Number": copy_n,
            "Armstrong" : True
        }
    else:
        result = {
            "Number": copy_n,
            "Armstrong" : False
        }
        # print(f"{copy_n} This not armstrong number ")
    return jsonify(result)

if __name__== "__main__":
    app.run(debug=True, port=5003)