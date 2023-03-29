from typing import Optional
from urllib.parse import urlparse

from pydantic import BaseModel, Field


class Bookmark(BaseModel):
    guid: str
    title: str
    index: int
    date_added: int = Field(alias="dateAdded")
    last_modified: int = Field(alias="lastModified")
    id: int
    type_code: int = Field(alias="typeCode")
    type_name: str = Field(alias="type")
    root: Optional[str] = None
    children: Optional[list['Bookmark']] = None
    uri: Optional[str] = None

    @property
    def name(self) -> str:
        if self.title == '' and self.uri is not None:
            # Extract hostname from URI
            hostname = urlparse(self.uri).hostname
            assert hostname is not None
            return hostname
        return self.title

    @property
    def is_empty(self) -> bool:
        return self.uri is None and self.children is None

    def cleanup(self) -> None:
        if self.children is None:
            return
        for child in self.children:
            child.cleanup()
        self.children = [child for child in self.children if not child.is_empty]
