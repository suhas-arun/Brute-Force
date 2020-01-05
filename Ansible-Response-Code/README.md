# Ansible Module that gets the HTTP response status code from a website. (For Google Code-In)

HTTP response status codes are used to indicate the status of a HTTP request. There are 5 classes of responses:

* 100-199: Informational responses
* 200-299: Successful responses
* 300-399: Redirects
* 400-499: Client errors
* 500-599: Server errors

This ansible module gets the HTTP response code from https://getfedora.org but this can be changed by editing the url in [main.yml](./main.yml). The response code is found using the `requests` library.

Below is a recording of the module running:

[![asciicast](https://asciinema.org/a/291964.svg)](https://asciinema.org/a/291964)