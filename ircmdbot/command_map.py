from ircmdbot.utils import whitespace_split


class CommandMapBuilder:
    def __init__(self):
        self.internal_command_map = {}

    def add_command(self, caller, alias, command):
        key = CommandMap.build_key(caller, alias)
        self.internal_command_map[key] = command

    def build(self):
        ret = CommandMap(self.internal_command_map)
        self.internal_command_map = {}
        return ret


class CommandMap:
    @staticmethod
    def build_key(caller, alias):
        return caller + '#' + alias

    def __init__(self, internal_command_map):
        self.internal_command_map = internal_command_map

    def get_command(self, caller, alias):
        key = CommandMap.build_key(caller, alias)
        return self.internal_command_map.get(key)


class CommandMapFactory:
    @staticmethod
    def from_file(file_name):
        builder = CommandMapBuilder()
        for l in (file(file_name)):
            l = l.strip()
            if len(l) == 0:
                continue
            parts = whitespace_split(l, 3)
            if len(parts) != 3:
                print "WARN: invalid command line '%s'" % l
                continue
            (caller, alias, command) = parts
            builder.add_command(caller, alias, command)
        return builder.build()
