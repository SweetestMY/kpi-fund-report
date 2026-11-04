import os, sys
sys.stdout.reconfigure(encoding='utf-8')

for item in sorted(os.listdir('.')):
    if os.path.isdir(item):
        size = sum(os.path.getsize(os.path.join(dp, f)) for dp, dn, fn in os.walk(item) for f in fn)
        print(f"DIR  {item:30s}: {size / (1024*1024):6.2f} MB")
    else:
        print(f"FILE {item:30s}: {os.path.getsize(item) / 1024:6.2f} KB")
