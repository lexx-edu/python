import configparser


def read_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf8')
    return config