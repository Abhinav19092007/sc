#!/usr/bin/env python3

from pathlib import Path


def main() -> int:
    requirements_path = Path(__file__).with_name("requirements.txt")

    if not requirements_path.exists():
        print("requirements.txt not found.")
        return 1

    print("Scanning dependencies in requirements.txt...")
    packages = []
    with requirements_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                packages.append(stripped)

    if not packages:
        print("No dependencies to scan.")
        return 0

    print("Detected packages:")
    for pkg in packages:
        print(f" - {pkg}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
