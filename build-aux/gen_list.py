# script to generate a markdown list of snippets to include in README.md

import json
from pathlib import Path

input_file = Path("snippets/rust.json")

with input_file.open("r") as in_file:
    content = json.load(in_file)
snippet_list = sorted(
    [(v["prefix"], v.get("description", k)) for k, v in content.items()]
)
col1 = "  Snippet"
col2 = "  Description"
print("\n## Snippets\n")
print(f"|{col1:25}|{col2:40}|")
print(f"|{25 * '-'}|{40 * '-'}|")
for prefix, description in snippet_list:
    print(f"|{prefix:25}|{description:40}|")
