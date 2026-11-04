import os, sys
sys.stdout.reconfigure(encoding='utf-8')

for name in os.listdir('d:/1-project-gun'):
    full = os.path.join('d:/1-project-gun', name)
    if os.path.isdir(full):
        print(name)
