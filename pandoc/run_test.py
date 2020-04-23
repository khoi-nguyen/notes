import yaml
import sys
from glob import glob
from algebra import *
from analysis import *
from stats import *
from probability import *
from pythontex import *

for path in glob('./tests/*.yaml'):
    with open(path) as file:
        tests = yaml.load(file, Loader=yaml.FullLoader)

        for test in tests:
            result = eval(test['cmd'])
            if isinstance(result, tuple):
                result = list(result)
            if result != test['out']:
                print('Failed test:', test['name'])
                expected, output = str(test['out']), str(result)
                print('Expected:', expected)
                print('Output  :', output)
                pos = max([i for i in range(0, min(len(expected), len(output))) if expected[:i] == output[0:i]])
                print('         ' + ' ' * pos, '^')
                sys.exit(1)
