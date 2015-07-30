# ircmdbot

This is simple IRC bot allowing users to execute predefined set
of shell commands on machine on which bot is running.

# Installation

```
pip install ircmdbot
```

# Running bot

You can simply execute `ircmdbot` command passing two configuration file paths as arguments:

```
# ircmdbot <config_file.yaml> <commmands_file>
```

## config_file.yaml

It is general configuration file.

Example contents:
```
server: port80a.se.quakenet.org
port: 6667
nickname: ircmdtdbd
secret: godsavethequeen
```

Configuration params are:
 - *server* - hostname of IRC server to connect to
 - *port* - TCP port to be used to connect to IRC server
 - *nickname* - nickname to be used by bot
 - *secret* - secret token to be used for authorization when sending commands to bot


## commands_file

Lists commands which can be run through the bot.
Each command is keyed with alias and nickname.

Format of configuration line in `commands_file` is:

```
<user> <alias> <command>
```

Example contents:

```
frank dosth           /home/frank/bin/dosth
frank dosth_different /home/frank/bin/dosth_different
steve dosth           /home/steve/bin/dosth
```

# Interacting with bot

Users interact with bot using private messages.
Each command is single line in following format.
```
<secret> <command_alias>
```

`<secret>` must be equal to `secret` from `config_file.yaml`.</br>
`<command_alias>` is one of aliases defined for user talking to bot in `commands_file`.

Special `<command_alias>` `die` is supported and kills bot process.


