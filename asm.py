import sys, string

opcodes = []

f = open('code2.asm', 'r')

def decode( op ): 
	if( op == 'LDA' ):
		return 0xA009
	elif( op == 'LSR' ):
		return 0xA00A
	elif( op == 'JMP' ):
		return 0xA00C
	elif( op == 'INA' ):
		return 0xA00D
	elif( op == 'DEA' ):
		return 0xB00D
	elif( op == 'MOVA' ):
		return 0xA00E
	elif( op == 'MOV' ):
		return 0xA00B
	elif( op == 'CMP' ):
		return 0xB001
	elif( op == 'BRZ' ):
		return 0xB002
	elif( op == 'HLT' ):
		return 0xB003
	else:
		return int(op, 16)

for line in f:
	if( not line.startswith('#') ):
		for item in string.split(line.rstrip(), ' '):
			opcodes.append( decode(item) )

print opcodes;

