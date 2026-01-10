#!/usr/bin/env python3
import subprocess
import os

bash_script = """
for ch in challenges/*/; do
    echo "Installing ${ch%/}"
    ctf challenge install "${ch%/}"
done
"""

subprocess.run(bash_script, shell=True, executable='/bin/bash')
