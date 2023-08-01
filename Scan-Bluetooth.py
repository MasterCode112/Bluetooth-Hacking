import bluetooth
from Banner_MasterCode import print_banner

# Search for nearby Bluetooth devices

print_banner()

devices = bluetooth.discover_devices()

# Print table of devices found
print("Bluetooth Devices:\n")
print("{:<20} {:<17}".format("Device Name", "MAC Address"))
print("----------------------------------------")
for addr in devices:
    name = bluetooth.lookup_name(addr)
    if name is not None and addr is not None:
        print("{:<20} {:<17}".format(name, addr))
