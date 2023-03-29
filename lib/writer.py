from pydantic import BaseModel

from lib.types import Bookmark


class Writer(BaseModel):
    indent: int = 0

    def write(self, entry: Bookmark) -> None:
        if entry.uri is None:
            self.print('- ' + entry.name)
        else:
            self.print(f'- [{entry.name}]({entry.uri})')

        child_writer = Writer(indent=self.indent + 1)
        if entry.children is not None:
            for child in entry.children:
                child_writer.write(child)

    def print(self, msg: str) -> None:
        print(('  ' * self.indent) + msg)
