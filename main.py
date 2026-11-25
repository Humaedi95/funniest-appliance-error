#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Entry for the make.fun bounty u-xvader-the-funniest-honest-appliance-error-adec4450.
A washing machine, reporting its own failure in its own flat voice.
"""

import os

ENTRY = "ERROR E07: Unbalanced load. One hoodie, one sock. I have spun for 40 minutes trying to make that fair. Please fix it yourself — I have given up."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
