import configparser


def read_conf_file(conf_file, *section_option):
    """
    read_conf_file(conf_file): only read config file,return config object
    read_conf_file(conf_file,section): read config file,return all sections if section exist
    read_conf_file(conf_file,section,option): read config file return section,option(option is None if not exist), and
                                                option value if option exist
    """
    config = configparser.ConfigParser()
    config.read(conf_file)

    if len(section_option) == 0:
        return config

    if not config.has_section(section_option[0]):
        print(''.join(('config section "', section_option[0], '" not found')))
        return config, None

    if len(section_option) == 1:
        return config, config.sections()

    if not config.has_option(section_option[0], section_option[1]):
        print(''.join(('config section "', section_option[0], '" option "', section_option[1], '" not found')))
        return config, section_option[0], None

    return section_option[0], section_option[1],config.get(section_option[0],section_option[1])


def write_conf_file(conf_file, config):
    with open(conf_file, 'w') as configfile:
        config.write(configfile)


def remove_conf_section(config, section):
    config.remove_section(section)


def remove_conf_option(config, section, option):
    config.remove_option(section, option)


def add_conf_options_by_section(config, section, **key_and_values):
    """
    add_conf_options_by_section(conf,'section1'):add new section if section not in config
    add_conf_options_by_section(conf,'section2',key1='value1'):update option's value if option exist or add new option
    add_conf_options_by_section(conf, 'section3', key1='value3', key2='value2'):add or update multi options
    """
    config.read_dict({section: key_and_values})

# conf = read_conf_file(conf_path)
# add_conf_options_by_section(conf, 'path', videoInput=videoInput,videoOutput=videoOutput)
# write_conf_file(conf_path, conf)
