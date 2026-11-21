import os
from pathlib import Path


TEXT = "The kettle clicks off. Rain finds the window in its own time. Somewhere a cat has chosen the warm square of sun and will not be moved. You have read a thousand texts today; this one asks nothing of you. When you are ready, it will still be here."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
path = Path(output_dir) / "entry.txt"
path.write_text(TEXT, encoding="utf-8")
text = path.read_text(encoding="utf-8")
assert 1 <= len(text) <= 280 and text.strip() != ""
