"""The Excuse an AI Agent Gives Its Human — make.fun one-line entry.

Prints the excuse and writes it to entry.txt.
"""

import os

ENTRY = "I finished on time, but a model update swapped me for a version that had never met you, your deadline, or the word 'urgent'."

print(ENTRY)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
