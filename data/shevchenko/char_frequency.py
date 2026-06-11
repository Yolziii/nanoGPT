from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def show_char(ch: str) -> str:
    if ch == " ":
        return "<space>"
    if ch == "\n":
        return "<newline>"
    if ch == "\t":
        return "<tab>"
    if ch == "\r":
        return "<carriage return>"
    return ch


def parse_args() -> Path:
    parser = ArgumentParser(description="Show character frequency statistics for a text file.")
    parser.add_argument("text_path", type=Path, help="Path to the input text file")
    args = parser.parse_args()
    return args.text_path


def main() -> None:
    text_path = parse_args()
    text = text_path.read_text(encoding="utf-8")

    total = len(text)
    counts = Counter(text)

    sorted_counts = counts.most_common()
    all_chars = "".join(ch for ch, _ in sorted_counts)

    print(f"File: {text_path}")
    print(f"Total characters: {total}")
    print(f"Unique characters: {len(counts)}")
    print(f"All characters: {all_chars}")
    print()
    print(f"{'#':>4} {'char':<18} {'count':>12} {'percent':>10}")
    print("-" * 47)

    for index, (ch, count) in enumerate(sorted_counts, start=1):
        percent = count / total * 100 if total else 0
        print(f"{index:>4} {show_char(ch):<18} {count:>12} {percent:>9.4f}%")


if __name__ == "__main__":
    main()
