#!/usr/bin/env python3
"""Worst Fix Ever — writes the funniest commit message to /output/entry.txt.

The fix: the error message is now a compliment. The bug is still there,
but it feels supported.
"""
import os

TEXT = "fix: turned the error message into a compliment. The bug is still there but now it feels supported."

# A commit message in the classic voice: the prefix says "fix", the
# body confesses the fix fixed nothing — and calls it progress anyway.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
