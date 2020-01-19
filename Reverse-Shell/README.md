# Remote Command Execution using Reverse Shell (For Google Code-In)

The attacker file ([attacker.py](./attacker.py)) binds to port 5000. The victim file ([victim.py](./victim.py)) connects to the same port (the attacker's IP is entered by the user). The attacker is prompted to enter a command, which is sent to the victim. The victim then sends back the output of the command to the attacker.

**Note: `attacker.py` must be run before `victim.py`.**


## Recording

Below is a recording of `attacker.py` running. I ran `victim.py` on another virtual machine at the same time.

[![asciicast](https://asciinema.org/a/294613.svg)](https://asciinema.org/a/294613)