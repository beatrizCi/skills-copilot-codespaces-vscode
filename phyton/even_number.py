from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

@app.route('/filter_even_numbers', methods=['POST'])
def filter_even_numbers():
    data = request.get_json()
    numbers = data.get('numbers', [])
    even_numbers = [num for num in numbers if num % 2 == 0]
    return jsonify(even_numbers)

if __name__ == '__main__':
    app.run()

    

#I need a function to convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
