import sys, array, string
import asm

TRACE = False

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

# zero - not sure if this is part of 
# 6500 arch
Z = 0b10000000

# ram = array.array('B', '123')
mem = [0 for x in range(100)]

def printRegs():
	if(TRACE):
		print 'AC: ' + str(AC)
		print 'SR: ' + str(SR)
		print 'PC: ' + str(PC)

f = open('code2.obj', 'r')

def dec_eight( val ):
	val -= 1
	if( val < 0 ): 
		return 255
	else:
		return val

def inc_eight( val ):
	val += 1
	if( val > 255 ): 
		return 0 
	else:
		return val

def trace( msg ):
	if( TRACE ):
		print msg


opcodes = asm.opcodes 
'''
opcodes = []
for line in f:
	if( not line.startswith('#') ):
		for item in string.split(line.rstrip(), ' '):
			opcodes.append( item )

print opcodes 
'''

			
def tick():
	global PC
	global AC
	global SR

	if opcodes[PC] == '0xA009':
		trace( 'Instruction: LDA ' + opcodes[PC+1] )
		AC = int( opcodes[PC+1], 16 )
		PC += 2
		printRegs()
		trace( mem )

	elif opcodes[PC] == '0xA00A':
		trace( 'Instruction: LSR A' )
		if AC & 0b00000001:
			# set carry bit
			SR |= C
		else:
			# clear carry bit
			SR &= ~C
			
		AC = AC >> 1
		PC += 1
		printRegs()
		trace( mem )

	# placeholder
	# todo: put proper opcode in
	elif opcodes[PC] == '0xA00B':
		trace('Instruction: MOV xxxxx')
		mem[int( opcodes[PC+1], 16 )] = int( opcodes[PC+2], 16 );
		PC += 3
		printRegs()
		trace( mem )

	# placeholder
	# todo: put proper opcode in
	elif opcodes[PC] == '0xA00C':
		trace('Instruction: JMP xxxxx')
		PC = int(opcodes[PC+1], 16)
		printRegs()
		trace(mem)

	# placeholder
	# todo: put proper opcode in
	elif opcodes[PC] == '0xA00D':
		trace('Instruction: INA xxxxx')
		AC = inc_eight( AC )
   		PC += 1
		printRegs()
		trace(mem)

	# placeholder
	# todo: put proper opcode in
	# decrement A
	elif opcodes[PC] == '0xB00D':
		trace('Instruction: DEA xxxxx')
		AC = dec_eight( AC )
		PC += 1
		printRegs()
		trace(mem)

	# placeholder
	# todo: put proper opcode in
	elif opcodes[PC] == '0xA00E':
		trace('Instruction: MOVA xxxxx')
		mem[int( opcodes[PC+1], 16 )] = AC;
		PC += 2
		printRegs()
		trace(mem)

	# placeholder
	# todo: put proper opcode in
	# compare memory location with immediate
	elif opcodes[PC] == '0xB001':
		trace('Instruction: CMP xxxxx')
		if( mem[int( opcodes[PC+1], 16 )] == int( opcodes[PC+2], 16 ) ):
			# set zero bit
			SR |= Z
		else:
			# clear zero bit
			SR &= ~Z
				
		PC += 3
		printRegs()
		trace(mem)

	# placeholder
	# todo: put proper opcode in
	# branch if zero
	elif opcodes[PC] == '0xB002':
		trace('Instruction: BRZ xxxxx')
		if( SR & Z == Z ):
			PC = int( opcodes[PC+1], 16 )
		else:
			# clear zero bit
			PC += 2
				
		printRegs()
		trace(mem)

	# placeholder
	# todo: put proper opcode in
	# branch if zero
	elif opcodes[PC] == '0xB003':
		trace('Instruction: HLT xxxxx')
		printRegs()
		trace(mem)
		sys.exit()

	else:	
		print 'invalid opcode: ' + opcodes[PC] + ' PC: ' + str(PC)
		sys.exit()

