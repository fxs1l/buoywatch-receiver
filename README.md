# Buoywatch Central Receiving Device
![buoywatch_logo.png](https://github.com/fxs1l/Buoywatch/blob/master/images/buoywatch_logo.png "BuoyWatch Logo")
This repository contains the source codes for the central receiving node of the [BuoyWatch Project](https://github.com/fxs1l/BuoyWatch). 

## Installation 
Clone the repository to the Raspberry Pi.
```bash
git clone https://github.com/fxs1l/buoywatch-receiver.git
```
> Note: Only tested on the Raspberry Pi 3 Model B.

## Requirements

In order to enable bluetooth communication in your device, run this on terminal:

```bash
sudo apt-get install bluemanbluez Bluetooth
```
This is needed to enable bluetooth in your Raspberry Pi

For you to pair your mobile phone to your Raspberry Pi
```bash
bluetoothctl
power on
devices
scan on
agent on
pair <mac address>
trust <mac address>
connect <mac address>
```

Configuration for bluetooth:
```bash
hciconfig
```

Create Bluetooth profile as follows:
```bash
sdptool add sp
```


In data_receiver.py, it automatically sends data bluetooth serial to the terminal once connected. 
```bash
echo “type character/message here” >/dev/rfcomm0
```

## Schematic Diagram
![receiver schematic.png](https://github.com/fxs1l/buoywatch-receiver/blob/master/receiver-schematic.jpeg "BuoyWatch Receiver")

The Receiver node of BuoyWatch is composed of Raspberry Pi and LoRa Module. This is to wirelessly communicate with the deployed buoy and to send data to and from the different nodes. 

## Usage
The bash script ``run`` runs ``date_receiver.py``. Make``run`` executable and run.
```bash 
chmod +x run
./run
```
### Enable on boot
Move ``run`` to ``/etc/init.d/`` folder
