#include <Stepper.h>

#include <Servo.h>

Servo myServo;
// Define stepper motor steps per revolution
const int stepsPerRevolution = 300; // Adjust based on your stepper motor

// Create Stepper instance (4 pins version: pins 8, 9, 10, 11)
Stepper myStepper(stepsPerRevolution, 11, 9, 10, 8);
Stepper myStepper_rev(stepsPerRevolution,  8,10,9,11);

// Variables
bool motorDirection = false; // False = clockwise, True = counterclockwise
const int motorRunTime = 11000; // Motor run time in milliseconds

void setup() {
  Serial.begin(9600);
  myServo.attach(3);
  pinMode  (6,INPUT);
  pinMode (7,INPUT); 
  myStepper.setSpeed(120);
  myStepper_rev.setSpeed(120);        // Set motor speed (RPM)
       // Initialize serial communication (HC-05 default baud rate)

}

void loop() {
  // Check if data is available
  if (Serial.available() > 0) {
    char input = Serial.read(); // Read the incoming character
    if (input == '1') { // Command to toggle motor direction
      // Toggle motor direction
      motorDirection = !motorDirection;
      Serial.println(motorDirection ? "Direction: Going UP" : "Direction: Going DOWN");
      
      // Run motor in the desired direction
      unsigned long startTime = millis();
      while (millis() - startTime < motorRunTime) {
        if (motorDirection) {
            myStepper_rev.step(0);
            myStepper.step(stepsPerRevolution); // Rotate one step clockwise
        } else {
            myStepper.step(0);
            myStepper_rev.step(stepsPerRevolution);// Rotate one step counterclockwise
        }
      }
    }
  }
}