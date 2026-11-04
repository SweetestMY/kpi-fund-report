import glob

for f in glob.glob('*.md'):
    safe = f.encode('ascii', 'backslashreplace').decode('ascii')
    print("MD file:", safe)
