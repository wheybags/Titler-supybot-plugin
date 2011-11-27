###
# Copyright (c) 2011, lolno
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
import re
import mechanize

class Titler(callbacks.Plugin):
    noIgnore = True
    pass
    
    def __call__(self, irc, msg):
	if len(msg.args) >= 2:
		match = re.search("https*://[^ ]*", msg.args[1])
	else:
		return
	if match:
		url = msg.args[1][match.start():match.end()]
		br = mechanize.Browser()
		try:
			br.open(url)
			title = br.title()
		except:
			return

		if title:
			irc.queueMsg(ircmsgs.privmsg(msg.args[0],"Title: %s" % title))

Class = Titler


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
