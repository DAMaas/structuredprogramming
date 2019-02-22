from configparser import ConfigParser


def getConfig(filename="Code/Config.ini", section="DEFAULT"):
    config = {}

    parser = ConfigParser()
    parser.read(filename)

    if parser.has_section(section):
        parameters = parser.items(section)
        for parameter in parameters:
            config[parameter[0]] = parameter[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return config
