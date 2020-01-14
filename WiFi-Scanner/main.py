"""Script that finds the users on the current network"""
import socket
import subprocess
from getmac import get_mac_address


def get_ip():
    """Gets the user's local IP"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    ip_address = sock.getsockname()[0]
    ip_address = ".".join(ip_address.split(".")[:3]) + "."
    sock.close()

    return ip_address


def get_devices(ip_address):
    """Returns the MAC addresses connected to the network"""
    devices = set()
    for i in range(256):
        current_ip = ip_address + str(i)
        command = ["ping", "-c", "1", "-w", "1", current_ip]
        result = subprocess.run(
            command,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode == 0:
            mac = get_mac_address(ip=current_ip)
            if mac:
                devices.add(mac)

    return devices


def main():
    """Main function"""
    ip_address = get_ip()

    print("Finding devices...")

    devices = get_devices(ip_address)

    print(f"There are {len(devices)} devices on the current network.")

    if devices:
        view_mac = input(
            "Would you like to view the MAC addresses on the current network (y/n)? "
        ).lower()

        if view_mac == "y":
            for device in devices:
                print(device)


if __name__ == "__main__":
    main()
