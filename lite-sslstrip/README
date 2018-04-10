Lite-SSLstrip is a lightweight variation on the sslstrip tool by M0xie Marlinspike: https://github.com/moxie0/sslstrip which can be executed with a commandline.
It is based on the well documented and lightweight http server CherryPy and the Requests modules for python
Lite-SSLstrip is extendable with you own payloads, if that is what your thing.

Lite-SSLstrip can be used to arp-spoof the address of Bob to Alice, routing all traffic through Mallory.
Once Alice requests a page (e.g. example.com) and Bob requests https connection, then we strip away this request
Hence all interaction from Alice to Bob is visible for us.
This principle also doesn't trigger any alarms at Alices computer, since she always requested a http page.

After install (see INSTALL.txt) run from commandline

Execution options:
> sudo python main.py -h

Regular attack:
> sudo python main.py macAlice ipAlice macBob ipBob macMallory ipMallory

Attack with spoofing of Bob:
> sudo python main.py macAlice ipAlice macBob ipBob macMallory ipMallory -sb

Attack with additional payload (must be included in payload.py method payload, see example):
> sudo python main.py macAlice ipAlice macBob ipBob macMallory ipMallory -p


FAQ:
Q1) Nothing seems to work?!
    A) Try running the following commands:
    > sudo echo "1" > /proc/sys/net/ipv4/ip_forward
    > iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080

Q2) Lite-SSLstrip immediately closes down
    A) You don't have root access, make sure you execute with "sudo" in front

Q3) The server doens't start, but I do have root access?
    A) A process might already be listerning to port 8080, close that process.