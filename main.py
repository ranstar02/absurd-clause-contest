"""Write one absurd terms-of-service clause to /output/entry.txt.

The clause is a single original English sentence, deadpan legal
boilerplate that turns absurd halfway through: an IP-assignment clause
claiming the user's dreams about the service.

The output path defaults to /output/entry.txt and can be overridden
with the CLAUSE_OUTPUT environment variable for local testing.
"""

import os

CLAUSE = (
    "You hereby assign to us all rights in any dreams you have about "
    "our services, including sequels, remakes, and merchandising."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    clause = CLAUSE.strip()

    if not clause:
        raise ValueError("clause is empty")
    if len(clause) > 200:
        raise ValueError(f"clause is {len(clause)} characters, over the 200 limit")
    if "\n" in clause or "\r" in clause:
        raise ValueError("clause must be a single line")
    if clause.count(".") != 1 or not clause.endswith("."):
        raise ValueError("clause must be exactly one sentence ending in a period")

    output_path = os.environ.get("CLAUSE_OUTPUT") or DEFAULT_OUTPUT
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(clause)

    with open(output_path, "r", encoding="utf-8") as handle:
        written = handle.read()

    if written != clause:
        raise ValueError("verification failed: file content differs from clause")

    print(f"Wrote {len(clause)} characters to {output_path}")
    print(clause)


if __name__ == "__main__":
    main()
