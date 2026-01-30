from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    name = args[0] if args else None
    if name is None or name.strip() == "":
        print("Hola mundo")
    else:
        print(f"Hola mundo, {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
