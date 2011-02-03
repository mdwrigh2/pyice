import subprocess
import os

for fn in os.listdir('tests'):
    if fn.endswith('.9') and not fn.startswith('.'):
        for line in open('tests/'+fn, 'r'):
            if line.startswith('#:compile'):
                retprocess = subprocess.call(['./ice9', 'tests/'+fn])
