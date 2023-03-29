from pathlib import Path
import json

import click

from lib.types import Bookmark
from lib.writer import Writer


TypePath = click.types.Path(path_type=Path)


@click.command()
@click.argument('bookmark-json', type=TypePath, required=True)
def main(bookmark_json: Path) -> None:
    writer = Writer()
    with bookmark_json.open() as f:
        data = json.load(f)
        bkmk = Bookmark(**data)
        bkmk.cleanup()
        writer.write(bkmk)


if __name__ == '__main__':
    main()
