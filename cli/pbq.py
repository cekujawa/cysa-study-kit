#!/usr/bin/env python3
import sys, pathlib

scenario = sys.argv[1] if len(sys.argv) > 1 else "linux-bruteforce"
path = pathlib.Path(f"pbq/scenarios/{scenario}/prompt.md")

if path.exists():
    print(path.read_text())
else:
    print(f"Scenario {scenario} not found.")
