import argparse
import csv
import json
import sys
from pathlib import Path

def parse_csv(file_path):
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def parse_json(file_path):
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(
        description="File Parser CLI Tool"
    )

    parser.add_argument(
        "input",
        help="Path to input file"
    )

    parser.add_argument(
        "--format",
        choices=["csv", "json"],
        required=True,
        help="Input file format"
    )

    parser.add_argument(
        "--output",
        help="Output file (default: stdout)"
    )

    args = parser.parse_args()

    input_path = Path(args.input)

    if not input_path.exists():
        print("Error: input file not found", file=sys.stderr)
        sys.exit(1)

    if args.format == "csv":
        data = parse_csv(input_path)
    elif args.format == "json":
        data = parse_json(input_path)

    output_data = json.dumps(data, indent=2)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_data)
    else:
        print(output_data)

if __name__ == "__main__":
    main()
