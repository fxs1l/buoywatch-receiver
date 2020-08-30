import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
 
 
# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None
 
while True:
    os.system("sudo rfcomm listen hci0&")
    packet = None
    # check for packet rx
    packet = rfm9x.receive()
    if packet is None:
        os.system("echo 'The Municipal Waters are safe. No illegal fishing detected' >/dev/rfcomm0")
    else:
        # Display the packet text and rssi
        prev_packet = packet
        packet_text = str(prev_packet, "utf-8")
        os.system("echo {} >/dev/rfcomm0").format(packet_text)

        time.sleep(1)
 
    display.show()
    time.sleep(0.1)