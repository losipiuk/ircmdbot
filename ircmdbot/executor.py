from subprocess import Popen
import os


class Excecutor:
    def __init__(self, command_map):
        self.command_map = command_map

    def run(self, caller, alias):
        command = self.command_map.get_command(caller, alias)
        if not command:
            return "unknown command %s/%s" % (caller, alias)
        self.execute(command)
        return "executed command %s/%s" % (caller, alias)

    def execute(self, command):
        print "Running %s" % command
        devnull = open(os.devnull, 'wb')
        Popen(command, shell=True, stdout=devnull, stderr=devnull)
