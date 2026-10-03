"""PEM Inspect — Show subject, issuer, and expiry for a PEM certificate without extra tools."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='pem_inspect',
        description='Show subject, issuer, and expiry for a PEM certificate without extra tools.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('PEM Inspect')
    print('What is in this .pem file.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
