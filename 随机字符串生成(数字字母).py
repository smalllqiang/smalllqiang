import random
ff = open("ff.txt",mode = "w",encoding="utf-8")
ls = ""
i = 0
while i <= 63:
	a = random.randint(0,61)
	if a <= 9:
		b = a + 48
	elif a > 9 and a <= 35:
		b = a + 55
	else :
		b = a + 61
	c = chr(b)
	ls = ls + c
	i = i + 1
ff.write(ls)
ff.close()

'''
chr(48)
0
chr(57)
9
chr(65)
A
chr(90)
Z
chr(97)
a
chr(122)
z
'''












print("成功生成ff.txt")
input("<press>")