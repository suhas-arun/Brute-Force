"""Python script to publish messages"""

from fedora_messaging import api, config

message = input("Enter message: ")
config.conf.setup_logging()
api.publish(api.Message(topic="hello", body={"Message": message}))
