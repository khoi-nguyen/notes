from generator.generator import *

exercises = [f for f in dir() if f.startswith("generate_")]

for ex in exercises:
    for level in range(1, 10):
        for i in range(0, 5):
            globals()[ex](level)
