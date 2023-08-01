# BLUETOOTH HACKING(ATTACK)

No, even your Bluetooth connection isn't safe from hackers! Here's how cybercriminals can target your Bluetooth-enabled devices.

![Untitled](BLUETOOTH%20HACKING(ATTACK)%20d1665292785b40b2b3a21591a1095853/Untitled.png)

You probably have Bluetooth enabled on numerous devices, including your smartphone, laptop, PC, and maybe even your vehicle. Through this connection, you can listen to music, get directions, and more.

But it's not exactly a secure technology. Bluetooth can get hacked. But the first line of defence is knowing how this can happen. So what vulnerabilities does Bluetooth have? How do hackers target Bluetooth-enabled devices?

## 1. Bluesnarf Attack

Bluesnarf attacks are one of the most prevalent types of Bluetooth 
attack. The OBject EXchange (OBEX) protocol is used for importing 
business cards and other items. With an OBEX GET request, the attacker 
has access to all files on the victim's device if the victim's Bluetooth
 driver software is wrongly installed. This service does not usually 
need authentication, so anybody can use it.

## 2. Bluesnarf++ Attack

This attack is similar to the Bluesnarf attack. The main difference 
is the method the attacker uses to gain access to the file system. If a [File Transfer Protocol (FTP)](https://www.makeuseof.com/what-is-ftp-server/)
 server is running on OBEX, it is possible to connect to this service 
without pairing with the device, thanks to the OBEX Push service. They 
gain access to, and can view and modify files without authentication and
 matching.

## 3. BluePrinting Attack

Through a BluePrinting attack, it is possible to capture information 
such as the brand and model of the device by using the data provided by 
Bluetooth technology.

The first three digits of the Bluetooth [MAC address](https://www.makeuseof.com/mac-address-vs-ip-address-difference/)
 provide information about the device and its manufacturer. Apart from 
that, there are supported applications, open ports, and more that you 
can learn from the device. With this information, you can access the 
device's brand, model, and even the version of the Bluetooth software 
you're running. In this way, you can learn more detailed information 
about the operating system and the attack vector can be narrowed.

## 4. HelloMoto Attack

![Untitled](BLUETOOTH%20HACKING(ATTACK)%20d1665292785b40b2b3a21591a1095853/Untitled%201.png)

This attack exploits the vulnerability in some of Motorola's devices
 with improper management of "trusted devices". The attacker starts 
sending a vCard (a virtual business card with contact information) using
 the OBEX Push service. The attacker interrupts this, creating a failed 
post; however, this does not remove the attacker from the trusted list. 
Now, the attacker can connect to the headset profile without the need 
for authentication.

## 5. BlueBump Social Engineering Attack

This attack [requires some social engineering](https://www.makeuseof.com/tag/social-engineering-makeuseof-explains/).
 The main idea is to provide a secure connection with the victim. This 
is possible with a virtual job card or a file transfer. If, after a 
transfer, the victim has added you to the trusted device list, the 
attacker will then ask the victim to delete the connection key without 
breaking the connection. Having cleared this, and being unaware that the
 attacker is still connected, the victim continues with their usual 
business.

The attacker, on the other hand, requests to re-key using their 
current connection. As a result, the attacker's device re-enters the 
victim's trusted list without authentication, and the attacker can gain 
access to the device until the victim disables this key.

## 6. BlueDump Attack

Here, the attacker has to know the addresses with which the Bluetooth
 device is paired, i.e. the Bluetooth Device Address (BD_ADDR), a unique
 identifier assigned to each device by manufacturers. The attacker 
replaces their address with the address of a device the victim is 
connected to and connects to the victim. Since the attacker does not 
have a connection key, the victim's device will return no connection key
 ("HCI_Link_Key_Request_Negative_Reply") when it wants to connect. In 
some cases, this will cause the victim's device to clear the connection 
key and enter pairing mode again.

The attacker can enter pairing mode and read the key change, so they 
have both removed the trusted device from the list and have the right to
 connect. They are also involved in the key exchange and can perform a [Man-in-the-Middle (MITM) attack](https://www.makeuseof.com/what-is-a-man-in-the-middle-attack/).

## 7. BlueChop Attack

![Untitled](BLUETOOTH%20HACKING(ATTACK)%20d1665292785b40b2b3a21591a1095853/Untitled%202.png)

## 8. Authentication Abuse

Authentication applies to all devices that use a service on Bluetooth
 devices; but anything that connects to the main device to use a service
 can also use all other services that provide unauthorized access. In 
this attack, the attacker tries to connect to the unauthorized services 
running on the provider and uses these for their own purposes.

## 9. BlueSmack DoS Attack

BlueSmack is a Denial-of-Service (DoS) attack, possible to create 
using the Linux BlueZ Bluetooth layer. Essentially, a cybercriminal 
sends over a data packet that overwhelms the target device.

This is achieved through the Logic Link Control And Adaptation 
Protocol (L2CAP) layer, the purpose of which is to check the connection 
and measure the round trip time. Thanks to BlueZ's l2ping tool, an 
attacker can change the size of the packets (600 bytes size is ideal 
with the -s parameter), and cause the device to be rendered useless.

## 10. BlueBorne

Using the vulnerabilities in the Bluetooth stack, Blueborne can 
connect to devices without owners' knowledge and run commands with 
maximum authority inside the device. As a result, it is possible to 
perform all operations on the device; for example, operations such as 
listening, changing data, reading, and tracking.

This issue is caused by the Bluetooth chip being able to connect to 
the main chip without security checking and having maximum 
authorization.

## 11. Car Whisperer Attack

![Untitled](BLUETOOTH%20HACKING(ATTACK)%20d1665292785b40b2b3a21591a1095853/Untitled%203.png)

In this attack, attackers use PIN codes that come by default on 
Bluetooth radios in cars. Devices connect to vehicles by emulating a 
phone. After connecting, they can play sounds from the music systems in 
the vehicles and listen to the microphone. It's rare but can certainly 
happen, and at a surprising distance.

## Why Does Bluetooth Have So Many Vulnerabilities?

Bluetooth technology continues to evolve day by day. There is a very 
broad protocol level. This means that there is ample terrain to develop 
attack vectors and find new vulnerabilities. The easier understanding of
 other protocols (compared to Bluetooth) and the more complex nature of 
Bluetooth means it's still a target.

So how can you protect yourself? Be careful with what devices you 
pair with, and certainly what you allow on your list of trusted 
connections. You should also turn off your Bluetooth whenever you're not
 using it. It really doesn't need to be turned on 24/7.