import yaml


class Config:
    def __init__(self, server, port, nickname, secret):
        self.server = server
        self.port = port
        self.nickname = nickname
        self.secret = secret


class ConfigException(Exception):
    pass


class ConfigFactory:
    @staticmethod
    def from_yaml_file(file_name):
        with open(file_name) as file:
            config_yaml = yaml.load(file.read())

        print(config_yaml)

        def get_key(key):
            value = config_yaml.get(key)
            if not value:
                raise ConfigException("missing configuration key %s" % key)
            return value

        server = get_key('server')
        port = get_key('port')
        nickname = get_key('nickname')
        secret = get_key('secret')
        return Config(server, port, nickname, secret)
