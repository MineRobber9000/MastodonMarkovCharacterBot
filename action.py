import markovify

with open("corpus.txt") as f:
	global text
	text = f.read()

t = markovify.Text(text)

def makeToot(resuser=""):
	return resuser+t.make_short_sentence(500-len(resuser))

def test():
	print(makeToot())
	print(makeToot(resuser="@minerobber@tiny.tilde.website "))
