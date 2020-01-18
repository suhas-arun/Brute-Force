# Ansible Role that fixes the Heartbleed bug (For Google Code-In)

The role updates and restarts the following services:

* nginx
* apache2
* postgresql
* php5-fpm
* openvpn
* postfix
* monit
* unbound

It then runs the following command to check for vulnerable processes:

    lsof -n | grep ssl | grep DEL | wc -l

If the output is 0 then there are no vulnerable processes.

Below is a recording of the role running:

[![asciicast](https://asciinema.org/a/294416.svg)](https://asciinema.org/a/294416)