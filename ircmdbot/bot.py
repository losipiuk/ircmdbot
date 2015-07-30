import irc.bot
from utils import whitespace_split


class Command:
    def __init__(self, secret, action):
        self.secret = secret
        self.action = action

    @staticmethod
    def parse(cmd_string):
        parts = whitespace_split(cmd_string, 2)
        if len(parts) != 2:
            return None
        return Command(*parts)


class IrcmdBot(irc.bot.SingleServerIRCBot):
    def __init__(self, config, executor):
        irc.bot.SingleServerIRCBot.__init__(self,
                                            [(config.server, config.port)],
                                            config.nickname,
                                            config.nickname)
        self.config = config
        self.executor = executor

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        return

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        return

    def on_dccmsg(self, c, e):
        return

    def on_dccchat(self, c, e):
        return

    def do_command(self, e, cmd_string):
        nick = e.source.nick
        c = self.connection

        cmd = Command.parse(cmd_string)
        if not cmd:
            c.notice(nick, "what?")
            return

        if cmd.secret != self.config.secret:
            c.notice(nick, "no way!")
            return

        if cmd.action == "die":
            c.notice(nick, "bang!")
            self.die()
        else:
            c.notice(nick, self.executor.run(nick, cmd.action))
