from flask import Flask, request, jsonify
from flask_cors import CORS
import serial
import serial.tools.list_ports

app = Flask(__name__)
CORS(app)

@app.route('/ports', methods=['GET'])
def list_ports():
    ports = [port.device for port in serial.tools.list_ports.comports()]
    
    ports.append("Port 1")  

    return jsonify({"ports": ports})

@app.route('/updated', methods=['POST'])
def update_color():
    data = request.get_json()
    r = data.get('r')
    g = data.get('g')
    b = data.get('b')
    port = data.get('port')

    print(f"\nReceived RGB: R={r}, G={g}, B={b}, Port={port}\n")

    if port:
        try:
            with serial.Serial(port, 9600, timeout=1) as ser:
                message = f"{r},{g},{b}\n"
                ser.write(message.encode())
                print(f"Sent to serial: {message.strip()}")
        except Exception as e:
            print(f"Serial communication error: {e}")
            return jsonify({"status": "error", "message": str(e)}), 500

    return jsonify({"status": "success", "message": "RGB received"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)