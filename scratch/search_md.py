import glob

for fname in glob.glob('*.md'):
    with open(fname, 'r', encoding='utf-8') as f:
        txt = f.read()
    matches = [l for l in txt.split('\n') if '5.2' in l or 'ทรัพยากรบุคคล' in l]
    safe_fn = fname.encode('ascii', 'backslashreplace').decode('ascii')
    print(f"=== {safe_fn} matches: {len(matches)} ===")
    for m in matches[:10]:
        print("  ", m.encode('ascii', 'backslashreplace').decode('ascii'))
