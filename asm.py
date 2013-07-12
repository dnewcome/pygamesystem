import sys, string

opcodes = []

f = open('code2.asm', 'r')

def decode( op ): 
	if( op == 'LDA' ):
		return '0xA009', 2
	elif( op == 'LSR' ):
		return '0xA00A', 1
	elif( op == 'MOV' ):
		return '0xA00B', 3
	elif( op == 'JMP' ):
		return '0xA00C', 1
	elif( op == 'INA' ):
		return '0xA00D', 1
	elif( op == 'DEA' ):
		return '0xB00D', 1
	elif( op == 'MOVA' ):
		return '0xA00E', 2
	elif( op == 'CMP' ):
		return '0xB001', 3
	elif( op == 'BRZ' ):
		return '0xB002', 2
	elif( op == 'HLT' ):
		return '0xB003', 1
	else:
		return op, 1

for line in f:
	if( not line.startswith('#') and not line.startswith( '\n' ) ):
		for item in string.split(line.rstrip(), ' '):
			opcodes.append( decode(item)[0] )

print opcodes;

