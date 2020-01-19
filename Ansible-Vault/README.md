# Working with Ansible Vault (For Google Code-In)

Ansible vault is an Ansible feature that allows sensitive data (e.g. passwords and keys) to be kept in encrypted files. This is useful for distributing files as sensitive data will not be visible to others.

## Encrypyting files
In this example I used [add-user.yml](./add-user.yml) which is a simple Ansible playbook that adds a user to the system under the name `new-user`. 

The playbook can be encrypted using Ansible Vault as follows:

    ansible-vault encrypt add-user.yml

This prompts the user for a password to encrypt the file with, which is just `password` in this case. The encrypted playbook is saved directly in [add-user.yml](./add-user.yml) so I copied it to [encrypted.yml](./encrypted.yml):

    cat add-user.yml > encrypted.yml

## Viewing encrypted files
Viewing the encrypted playbook with `cat` will not show the actual playbook but the encrypted version (as in [encrypted.yml](./encrypted.yml)). In order to view the encrypted playbook you need to use Ansible Vault as such:

    ansible-vault view add-user.yml

This prompts the user for the password and shows the actual playbook.

## Running the encrypted playbook

If you try to run an encrypted playbook with

    ansible-playbook add-user.yml -K

you will get an error, as the password is not provided.

In order to run an encrypted playbook with Ansible vault, you need to use the following command, which will prompt the user for the password.

    ansible-playbook add-user.yml -K --ask-vault-pass

## Decrypting playbooks

The playbook can be decrypted with

    ansible-vault decrypt add-user.yml


# Recording

[![asciicast](https://asciinema.org/a/294559.svg)](https://asciinema.org/a/294559)
