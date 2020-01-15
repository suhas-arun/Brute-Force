"""Script that finds the users on the current network without getmac"""
import subprocess


def get_devices():
    """Returns a set of the MAC addresses on the current network using arp"""
    result = str(subprocess.check_output(["arp", "-a"]))

    devices = set()
    for word in result.split():
        if ":" in word:
            devices.add(word)

    return devices


def main():
    """Main function"""
    print("Finding devices...")

    devices = get_devices()

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
