"""Network analyser tool from PCAP file using wireshark"""
import os
import subprocess
import sys


def show_options():
    """Prints possible commands"""
    print(
        "\n[1] Top 10 Visited Sites\n[2] User-Agents List\n[3] Connection Details\n[4] String Grep Mode\n[5] IP list\n[6] Ports list\n[7] Exit\n"
    )


def get_pcap_file():
    """Returns name of pcap file"""
    pcap = input("Enter name of pcap file: ")
    while not os.path.isfile(f"./{pcap}") or pcap.split(".")[1] != "pcap":
        pcap = input("Please enter a pcap file in the current directory: ")

    return pcap


def get_command():
    """Returns command number"""
    command = input("Enter command number: ")
    while not command.isdigit():
        command = input("Enter command number: ")
    while int(command) < 1 or int(command) > 7:
        command = input("Enter command number: ")

    return int(command)


def execute_command(pcap, command):
    """Executes command depending on input"""
    commands = [
        show_sites,
        show_user_agents,
        show_conn_details,
        grep_mode,
        show_ips,
        show_ports,
    ]

    if command == 7:
        sys.exit(0)

    commands[command - 1](pcap)


def show_sites(pcap):
    """Show top 10 most visited sites"""

    result = subprocess.run(
        ["tshark", "-r", pcap, "-Y", "http.request", "-T", "fields", "-e", "http.host"],
        capture_output=True,
        check=False
    )

    sites = result.stdout.decode("utf-8").rstrip().split("\n")
    top_10 = []
    print()
    for site in sorted(sites, key=sites.count)[::-1]:
        if len(top_10) == 10:
            break
        if site not in top_10:
            print(site)
            top_10.append(site)


def show_user_agents(pcap):
    """Show user agents"""

    result = subprocess.run(
        [
            "tshark",
            "-r",
            pcap,
            "-Y",
            "http.request",
            "-T",
            "fields",
            "-e",
            "http.user_agent",
        ],
        capture_output=True,
        check=False
    )

    user_agents = result.stdout.decode("utf-8").rstrip().split("\n")
    agents = set()
    for user_agent in user_agents:
        agents.add(user_agent)

    print("\n".join(agents))


def show_conn_details(pcap):
    """Show connection details"""
    result = subprocess.run(
        [
            "tshark",
            "-r",
            pcap,
            "-T",
            "fields",
            "-e",
            "_ws.col.Protocol",
            "-e",
            "ip.src",
            "-e",
            "udp.srcport",
            "-e",
            "tcp.srcport",
            "-e",
            "ip.dst",
            "-e",
            "udp.dstport",
            "-e",
            "tcp.dstport",
        ],
        capture_output=True,
        check=False
    )

    details = result.stdout.decode("utf-8").rstrip().split("\n")
    for connection in details:
        try:
            protocol, src_ip, src_port, dst_ip, dst_port = connection.split()
        except ValueError:
            continue

        print(
            f"Protocol: {protocol}   Source: {src_ip} - PORT: {src_port}   -->   Destination: {dst_ip} - PORT: {dst_port}"
        )


def grep_mode(pcap_file_name):
    """Search PCAP file"""
    string = input("Enter search string: ").encode()
    with open(pcap_file_name, "rb") as pcap_file:
        pcap = pcap_file.readlines()
        for line in pcap:
            if string in line:
                print(line[:-1])


def show_ips(pcap):
    """Show list of IP addresses"""
    subprocess.call(["tshark", "-r", pcap, "-T", "fields", "-e", "ip.dst"],)


def show_ports(pcap):
    """Show list of ports"""

    result = subprocess.run(
        [
            "tshark",
            "-r",
            pcap,
            "-T",
            "fields",
            "-e",
            "udp.srcport",
            "-e",
            "udp.dstport",
            "-e",
            "tcp.srcport",
            "-e",
            "tcp.dstport",
        ],
        capture_output=True,
        check=False
    )

    ports = result.stdout.decode("utf-8").split("\n")
    print()
    for port in ports:
        port = port.lstrip("\t\t").strip()
        if port:
            src, dst = port.split("\t")
            print(src, dst)


def main():
    """Main function"""
    pcap = get_pcap_file()
    while True:
        show_options()
        command = get_command()
        execute_command(pcap, command)


if __name__ == "__main__":
    main()
