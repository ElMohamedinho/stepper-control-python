import tkinter as tk
import serial
import time
import serial.tools.list_ports

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())  # List all available ports
    for port, desc, hwid in ports:
        # Check if the port description contains common Arduino keywords
        if 'Arduino' in desc or 'CH340' in desc or 'FTDI' in desc:  
            print(f"Found Arduino on port: {port}")
            return port
    print("No Arduino found.")
    return None

# Call the function and detect the Arduino port
arduino_port = find_arduino_port()

if arduino_port:
    print(f"Arduino is connected to: {arduino_port}")
else:
    print("Arduino not found.")

# Configure the serial port (adjust to your Arduino's port)
arduino = serial.Serial(port=arduino_port, baudrate=9600, timeout=1)  # Replace 'COM3' with your port

def send_command():
    """Send command to Arduino."""
    try:
        arduino.write(b'1')  # Send '1' to toggle motor
        time.sleep(0.1)  # Wait for the Arduino to process
        feedback = arduino.readline().decode('utf-8').strip()
        print(feedback)  # Display feedback from Arduino
        status_label.config(text=f"Arduino says: {feedback}")
    except Exception as e:
        print(f"Error: {e}")
        status_label.config(text="Error communicating with Arduino!")

# Create a simple GUI

root = tk.Tk()
root.title("Stepper Motor Control")
root.configure(bg="#121212")
# Add a button
button = tk.Button(root, text="Toggle Motor", command=send_command, font=("Arial", 40,"bold"), bg="#4CAF50", fg="#121212")
button.pack(pady=20)

# Add a status label
status_label = tk.Label(root, text="Press the button to toggle motor direction.", font=("Arial", 12,"bold"),bg="#121212",fg="#E0E0E0")
status_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
