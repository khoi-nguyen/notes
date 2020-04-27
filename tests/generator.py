from generator.generator import *
import sys

exercises = [f for f in dir() if f.startswith("generate_")]

for ex in exercises:
    for level in range(1, 10):
        for i in range(0, 5):
            try:
                globals()[ex](level)
            except:
                print("Exercise:", ex)
                print("Level   :", level)
                sys.exit(1)
