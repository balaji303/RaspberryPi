# RaspberryPi
The components used here are as follows
  1. Raspberry Pi 3-MODB-1GB Motherboard (RASPBERRYPI3-MODB-1GB)
  2. Raspberry Pi 5MP Camera Board
  3. Push Button Switch
  4. Generic Jumper Wires 

Some Important features regarding RaspberryPi are as follows

  1. gpiozero python doesn't support 1-WireProtocol
  2. No Analog inputs in Pi
  3. Only 3.3V is the highest input voltage
  4. WiringPi and bcm2835 are the library for C-Language in RaspberryPi
  5. Node-Red has good community support of all 
  6. Pull Up resistor are connected to GPIO-0 to GPIO-8
  7. Pull Down resistor are connected to GPIO-9 to GPIO-27
  8. Vout= (Vin*R2)/(R1+R2)