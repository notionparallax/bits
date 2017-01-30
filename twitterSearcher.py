#example response: {"valid":false,"reason":"taken","msg":"Username has already been taken","desc":"That username has been taken. Please choose another."}

permissableChars = list("abcdefghijklmnopqrstuvwxyz_1234567890")

import json
import urllib2
import itertools

possibleUsernames  = []
noGood = {}#start the dance


for i in range(5,7):
	options  = itertools.combinations(permissableChars, i)

	for o in options:
		uname = "".join(o)
		if uname not in noGood:
			url = "https://twitter.com/users/username_available?username="+uname
			response = urllib2.urlopen(url)
			data = response.read()
			values = json.loads(data)
			print uname, values
			if values["valid"] == "true":
				print "\n\n\n WE GOT ONE!"
				print uname, values
				possibleUsernames.push(uname)
			else:
				noGood[uname]=values

print possibleUsernames
print noGood