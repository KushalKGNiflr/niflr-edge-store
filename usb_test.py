import usb.core
import usb.util

dev = usb.core.find(idVendor=0x2dd6, idProduct=0x21c1)

if dev is None:
    raise ValueError('USB device not found')
else:
    print("Device found")

dev.set_configuration()

try:
    data = dev.read(4, 64)
except usb.core.USBError as e:
    print ("Error reading response: {}".format(e.args))
