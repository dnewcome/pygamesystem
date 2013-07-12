# load A with initial value
LDA 0x0008

# set framebuffer bit
MOVA 0x002C 

## read joystick ##
# compare mem location 99 with D
CMP 0x0063 0x0010

# jump if eq
BRZ 0x0010 

# compare mem location 99 with A
CMP 0x0063 0x0004

# jump if eq
BRZ 0x0015 

# jump to beginning
JMP 0x0004

# increment A
INA

# set framebuffer bit
MOVA 0x002C

# jump to beginning
JMP 0x0004

# decrement A
DEA

# set framebuffer bit
MOVA 0x002C

# jump to beginning
JMP 0x0004
