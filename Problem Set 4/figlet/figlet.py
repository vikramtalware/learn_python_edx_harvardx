from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
argv = ['-f', '--font']

if len(sys.argv) == 3 and sys.argv[1] in argv and sys.argv[2] in figlet.getFonts():
     s = str(input("Input: "))
     figlet.setFont(font = sys.argv[2])
     print("Output:\n", figlet.renderText(s))
elif len(sys.argv) == 1:
     s = str(input("Input: "))
     figlet.setFont(font = random.choice(figlet.getFonts()))
     print("Output:\n", figlet.renderText(s))
else:
     sys.exit("Invalid usage")
