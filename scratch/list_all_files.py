# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

for root, dirs, files in os.walk('..'):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), '..')
        if not rel.startswith('.git') and not 'node_modules' in rel:
            print(rel)
