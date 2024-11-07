from flask import Flask, request, json

app = Flask(__name__)

def is_prime(n):
    alkuluku = True

    for jakaja in range(2, n):
        if n % jakaja == 0:
            return False
    return True

@app.route('/primenumber')
def check_prime():
    number = request.args.get('n', type=int)
    if number is None:
        return json.dumps({"error": "Please enter a number"})

    result = {
        "Number": number,
        "isPrime" : is_prime(number)
    }
    return json.dumps(result)

if __name__ == '__main__':
    app.run(use_reloader=True, host="127.0.0.1", port=5000)