"""Ansible module that gets the HTTP response status code from a website"""

from ansible.module_utils.basic import AnsibleModule
import requests

module = AnsibleModule(argument_spec={"url": {"required": True, "type": "str"}})

response = requests.get(module.params["url"])

module.exit_json(changed=True, meta={"Status Code": response.status_code})
