#!/usr/bin/env python3
"""Roast Your Own Agent — writes one self-roast line to /output/entry.txt.

Deterministic, stdlib only: the same line, every run, no extra output.
"""
import os

ROAST = "My agent says 'Great question!', confidently invents the answer, then calls a tool that does nothing and reports success."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
