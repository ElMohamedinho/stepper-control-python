🔁 Stepper Motor Control via Python GUI & Arduino (UART)
This project enables real-time control of a stepper motor through a Python desktop application that communicates with an Arduino board over UART (Serial).


🖥️ Python GUI Features:
Built using Tkinter

Auto-detects the Arduino COM port

Sends a toggle command to change motor direction

Displays live feedback from Arduino

Clean dark-themed interface

🔧 Arduino Features:
Controls a 4-wire stepper motor using the Stepper library

Supports direction toggling (UP/DOWN)

Motor runs for a fixed duration (11s) when triggered

Sends feedback over Serial (e.g., Direction: Going UP)

Uses two Stepper instances to manage direction change


🧩 Components Used:
Arduino (Uno/Nano/ESP32)

Stepper Motor 

Stepper Driver 

USB Cable

PC with Python 3.x


🔌 Communication Protocol:
UART Serial @ 9600 baud

Python sends a command: '1'

Arduino reads via Serial.read() and reacts accordingly


📂 Project Structure:

/stepper-uart-controller/

├── arduino
│   └── stepper_control.ino

├── python-app
│   └── control UART.py

├── README.md


🚀 Getting Started:
On the Arduino Side:
Upload stepper_control.ino to your Arduino using the Arduino IDE.

Connect the stepper motor to pins 8-11.

Adjust stepsPerRevolution and motorRunTime if needed.

On the Python Side:
Install Python 3.x and pyserial:
      pip install pyserial
Run the Python app:
      python gui_controller.py
Press the GUI button to toggle motor direction.

📌 Notes:
Make sure your Arduino is detected properly via USB. The app will auto-scan for "Arduino", "CH340", or "FTDI" ports.

You can customize motor speed or direction logic in the Arduino code.

Supports expansion to include sensors, servos, and other control logic.

