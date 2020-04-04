import yaml
import sys
from algebra import *
from analysis import *
from stats import *
from probability import *
import sympy

paths = ['general', 'algebra']

for path in paths:
    with open(f'tests/{path}.yaml') as file:
        tests = yaml.load(file, Loader=yaml.FullLoader)

        for test in tests:
            result = eval(test['cmd'])
            if isinstance(result, tuple):
                result = list(result)
            if result != test['out']:
                print('Failed test:', test['name'])
                print('Output:', result)
                print('Expected result:', test['out'])
                sys.exit(1)
