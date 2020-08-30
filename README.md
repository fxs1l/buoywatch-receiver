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

## Usage
The bash script ``run`` runs ``date_receiver.py``. Make``run`` executable and run.
```bash 
chmod +x run
./run
```
### Enable on boot
Move ``run`` to ``/etc/init.d/`` folder
