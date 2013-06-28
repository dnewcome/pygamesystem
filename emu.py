import sys, array, string

# registers
PC = 0
AC = 0
X = 0
Y = 0
SR = 0
SP = 0x0100

# flag masks
N = 0b01000000
V = 0b00100000
G = 0b00010000
B = 0b00001000
D = 0b00000100
I = 0b00000010
C = 0b00000001

# ram = array.array('B', '123')
mem = [0 for x in range(100)]

def printRegs():
	print 'AC: ' + str(AC)
	print 'SR: ' + str(SR)
	print 'PC: ' + str(PC)

f = open('code.obj', 'r')

opcodes = []
for line in f:
    for item in string.split(line.rstrip(), ' '):
        opcodes.append( item )

print opcodes 

while( PC < 50 ):
	if opcodes[PC] == '0xA009':
		print 'Instruction: LDA ' + opcodes[PC+1]
		AC = int( opcodes[PC+1], 16 )
		PC += 2
		printRegs()

	elif opcodes[PC] == '0xA00A':
		print 'Instruction: LSR A'
		if AC & 0b00000001:
			# set carry bit
			SR |= C
		else:
			# clear carry bit
			SR &= ~C
			
		AC = AC >> 1
		PC += 1
		printRegs()

	# placeholder
	# todo: put proper opcode in
	elif opcodes[PC] == '0xA00B':
		print 'Instruction: MOV xxxxx'
		print line
		mem[int( opcodes[PC+1], 16 )] = int( opcodes[PC+2], 16 );
		PC += 3
		printRegs()
		print mem

	else:	
		print 'invalid opcode'

