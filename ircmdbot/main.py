import sys

from executor import Excecutor
from bot import IrcmdBot
from config import ConfigFactory, ConfigException
from command_map import CommandMapFactory


def help_exit():
    print "Usage: ircmdbot <config_file> <command_file>"
    sys.exit(1)


def main():
    if len(sys.argv) != 3:
        help_exit()

    config_file_name = sys.argv[1]
    command_file_name = sys.argv[2]

    config = read_config(config_file_name)
    command_map = CommandMapFactory.from_file(command_file_name)
    executor = Excecutor(command_map)
    bot = IrcmdBot(config, executor)
    bot.start()


def read_config(config_file_name):
    try:
        config = ConfigFactory.from_yaml_file(config_file_name)
    except ConfigException, e:
        print e.message
        sys.exit(2)
    return config


if __name__ == "__main__":
    main()
