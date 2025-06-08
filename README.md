# RGB-CONTROLLER
 This project provides a web-based RGB controller interface that allows users to adjust Red, Green, and Blue values using sliders or numeric input. The values are sent to a Flask backend, which communicates with a serial (UART) device such as an Arduino.

## Features

- RGB sliders and manual numeric input (range: 0–4095)
- Real-time color preview box
- Serial port detection and dropdown selection
- Reset and Enter buttons
- Keyboard Enter key support
- Fake serial port option for testing without hardware

## Project Structure
<pre>
```text
RGB_controller/
├── backend/
│   └── app.py
├── frontend/
│   └── front.html
├── requirements.txt
└── README.md
```
</pre>

## How It Works

1. User selects RGB values using sliders or inputs.
2. User selects an available serial port.
3. On clicking "Enter" or pressing the Enter key:
   - The RGB values are sent to the Flask backend.
   - The backend sends the values to the selected serial (UART) port.
4. The connected device receives and processes the RGB values.

## Troubleshooting

- **Error: `ModuleNotFoundError: No module named 'serial'`**
  - Run `pip install pyserial`

- **No serial ports showing up**
  - Make sure a device is connected.
  - On Windows: check Device Manager.
  - On macOS/Linux: try `ls /dev/tty.*` or `ls /dev/ttyUSB*`

- **Frontend doesn't connect to backend**
  - Ensure Flask server is running on `localhost:5000`
  - CORS must be enabled (already handled in `app.py`)
