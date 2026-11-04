import io, sys, os, subprocess
sys.stdout.reconfigure(encoding='utf-8')

# Search for any .git directory in D:\ or parent folders
print("Checking for .git folders:")
for root, dirs, files in os.walk('d:/'):
    if '.git' in dirs:
        print("Found git repo at:", os.path.join(root, '.git'))
        # don't go deep into this branch
        dirs.remove('.git')
    # only check top 3 levels
    if root.count(os.sep) - 'd:/'.count(os.sep) >= 2:
        dirs.clear()
