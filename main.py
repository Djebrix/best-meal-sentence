"""Best Meal You Ever Had — entry program.

Writes a single sentence (at most 200 characters) about the best meal
the entrant ever had to /output/entry.txt.
"""

import os

SENTENCE = (
    "At a plastic table in Jakarta past midnight, my grandmother's rendang, "
    "beef gone dark and soft after hours in coconut milk, made the motorbikes "
    "and the shouting hawkers fade to nothing."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1, "must be exactly one sentence"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
