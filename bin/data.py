#!/usr/bin/env python

from datetime import datetime
from pathlib import Path
import subprocess
import json

data = []

for path in sorted(Path('resources').rglob('*.md')):
    if str(path).endswith('worksheet.md'):
        data[-1]['worksheet'] = str(path).replace('.md', '.pdf')
        data[-1]['answers'] = str(path).replace('.md', '.answers.pdf')
        continue
    modified = path.stat().st_mtime
    path = str(path)
    cmd = 'pandoc -s {} -t markdown --template=pandoc/templates/meta.json'.format(path)
    json_string = subprocess.check_output(cmd.split(' '))
    meta = json.loads(json_string)
    if meta.get('publish'):
        data.append({
            'path': path,
            'year': path.split('/')[1],
            'meta': meta,
            'pdf': path.replace('.md', '.pdf'),
            'handout': path.replace('.md', '.handout.pdf'),
            'modified': datetime.fromtimestamp(modified).strftime('%d %b %Y %H:%m'),
        })

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=True)
