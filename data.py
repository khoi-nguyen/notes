#!/usr/bin/env python

from datetime import datetime
from pathlib import Path
import subprocess
import json

data = []

for path in Path('10').rglob('*.md'):
    modified = path.stat().st_mtime
    path = str(path)
    cmd = 'pandoc -s {} -t markdown --template=pandoc/meta.json'.format(path)
    json_string = subprocess.check_output(cmd.split(' '))
    data.append({
        'path': path,
        'year': path.split('/')[0],
        'meta': json.loads(json_string),
        'pdf': path.replace('.md', '.pdf'),
        'handout': path.replace('.md', '.handout.pdf'),
        'modified': datetime.fromtimestamp(modified).strftime('%d %b %Y %H:%m'),
    })

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=True)
