# Raspberry PI Model 3 B NeoPixels with Server-Client TCP Sockets

This project is a fun experimentation. The initial goal was to move my mouse on my computer and light up an LED Strip connected to my Raspberry Pi.

* The Raspberry PI is the server
* The Computer is the client

### FEATURES

More features will be coming soon, this project is for fun. There's no limit to how you want to play with the LEDs.

* Server receives client input and switches to a mode:
    * The LEDS light up according to the the mouse cursor position on the Y-Axis. 
    If your mouse is on the right most side of the screen, all LEDs are on. If it's on the left all leds are off. It's progressive transition
* Client sends data to the server

### HARDWARE

* Addressable RGB LED Strip, 5V. With either SK6812 or WS2812B-based LEDs
* Raspberry PI Model 3


### DEPENDENCIES
The server is the only one to have external dependencies to be able to run.
* Server: 
    * Run the following your command line: ```sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel```