gram = {
	"E":["S+S","S*S","id"]
}
starting_terminal = "E"
inp = "id+id*id+id*id"
"""
# example 2
gram = {
	"S":["S+S","S*S","id"]
}
starting_terminal = "S"
inp = "i+i*i"
"""
stack = "$"
print(f'{"Stack": <15}'+"|"+f'{"Input Buffer": <15}'+"|"+f'Parsing Action')
print(f'{"-":-<50}')

while True:
	action = True
	i = 0
	while i<len(gram[starting_terminal]):
		if gram[starting_terminal][i] in stack:
			stack = stack.replace(gram[starting_terminal][i],starting_terminal)
			print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Reduce S->{gram[starting_terminal][i]}')
			i=-1
			action = False
		i+=1
	if len(inp)>1:
		stack+=inp[0]
		inp=inp[1:]
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Shift')
		action = False

	if inp == "$" and stack == ("$"+starting_terminal):
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Accepted')
		break

	if action:
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Rejected')
		break

# Output

# Stack          |Input Buffer   |Parsing Action
# --------------------------------------------------
# $i             |d+id*id+id*id  |Shift
# $id            |+id*id+id*id   |Shift
# $E             |+id*id+id*id   |Reduce S->id
# $E+            |id*id+id*id    |Shift
# $E+i           |d*id+id*id     |Shift
# $E+id          |*id+id*id      |Shift
# $E+E           |*id+id*id      |Reduce S->id
# $E+E*          |id+id*id       |Shift
# $E+E*i         |d+id*id        |Shift
# $E+E*id        |+id*id         |Shift
# $E+E*E         |+id*id         |Reduce S->id
# $E+E*E+        |id*id          |Shift
# $E+E*E+i       |d*id           |Shift
# $E+E*E+id      |*id            |Shift
# $E+E*E+E       |*id            |Reduce S->id
# $E+E*E+E*      |id             |Shift
# $E+E*E+E*i     |d              |Shift
# $E+E*E+E*i     |d              |Rejected