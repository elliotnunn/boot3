#!/usr/bin/env python3

CI, CO = b'RESUME', b'YIELD'

from sys import argv, stdout

a, b = argv[1:]

with open(a, 'rb') as a, open(b, 'rb') as b:
	which = False
	ibins = [a, b]
	try:
		while True:
			l = next(ibins[which])
			stdout.buffer.write(l)

			if CO in l:
				which = not which
				for cil in ibins[which]:
					if CI in cil:
						stdout.buffer.write(cil)
						break

	except StopIteration:
		pass
