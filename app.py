from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenido al bot de Consultech!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Aquí procesarás los datos que lleguen al webhook
    print(data)
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
