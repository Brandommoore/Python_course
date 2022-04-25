# First conditionals

alum_mark=input()

def eval(mark):
	val="approved"
	if mark<5:
		val="fail"
	return val

print(eval(int(alum_mark)))