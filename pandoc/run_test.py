import yaml
import sys
from glob import glob
from algebra import *
from analysis import *
from stats import *
from probability import *
from pythontex import *
import sympy

for path in glob('./tests/*.yaml'):
    with open(path) as file:
        tests = yaml.load(file, Loader=yaml.FullLoader)

        for test in tests:
            result = eval(test['cmd'])
            if isinstance(result, tuple):
                result = list(result)
            if result == test['out']:
                print('Passed test:', test['name'])
            else:
                print('Failed test:', test['name'])
                print('Output:', result)
                print('Expected result:', test['out'])
                sys.exit(1)
