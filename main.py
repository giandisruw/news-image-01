"""news-image-01 v2 entry: copy the bundled image to the output path.

The image is "THE WORLD TODAY" — Friday 13 November 2026 in 24
stories: a lead on the Microsoft 365 outage, a numbered world map whose
pins match the stories below, and 23 numbered stories in a grid, with
claim labels on attributed, unconfirmed items. It was drawn once with
PIL (see build/render.py) and stored in this repository as entry.png.
This program does nothing but copy those exact bytes to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png when that variable
is set), so the two grader runs always write identical bytes.

Standard library only, no network, no randomness.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output_dir / "entry.png")


if __name__ == "__main__":
    main()
