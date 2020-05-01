import yaml
import sys
from glob import glob
from solver.algebra import *
from solver.analysis import *
from solver.geometry import *
from solver.stats import *
from solver.probability import *
from pandoc.filters.helpers import answer, question


for path in glob("./tests/*.yaml"):
    with open(path) as file:
        tests = yaml.load(file, Loader=yaml.FullLoader)

        for test in tests:
            result = eval(test["cmd"])
            if isinstance(result, tuple):
                result = list(result)
            if result != test["out"]:
                print("Failed test:", test["name"])
                expected, output = str(test["out"]), str(result)
                print("Expected:", expected)
                print("Output  :", output)
                pos = max(
                    [
                        i
                        for i in range(0, min(len(expected), len(output)))
                        if expected[:i] == output[0:i]
                    ]
                )
                print("         " + " " * pos, "^")
                sys.exit(1)
