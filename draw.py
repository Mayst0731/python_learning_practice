import pyfiglet
from termcolor import colored

msg = input('What msg do you want to try?')
color = input('What color do you like?')

shape = pyfiglet.figlet_format(msg)

colored_shape = colored(shape,color)

print(colored_shape)