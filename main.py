import webbrowser
import subprocess, os, platform
from crossref_commons import retrieval


class Paper:
    @classmethod
    def from_doi(cls, doi, local_path=None):
        metadata = retrieval.get_publication_as_json(doi)
        name = metadata['title'][0]
        first_author = metadata['author'][0]['family'] + " " + metadata['author'][0]['given']
        url = metadata['URL']
        return cls(name, first_author, url, local_path=local_path)

    def __init__(self,
                 name: str,
                 first_author: str,
                 url: str,
                 local_path: str = "") -> None:
        self.name = name
        self.first_author = first_author
        self.url = url
        self.local_path = local_path

    def open_web(self):
        webbrowser.open(self.url, new=2)

    def open_local(self):
        # https://stackoverflow.com/questions/434597/open-document-with-default-os-application-in-python-both-in-windows-and-mac-os
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', self.local_path))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(self.local_path)
        else:  # linux variants
            subprocess.call(('xdg-open', self.local_path))

    def __str__(self):
        return self.name + "\n" + self.first_author


class PaperNote(Paper):
    @classmethod
    def from_paper(cls, parent_paper, id=0, keywords={}, connections={}):
        return cls(parent_paper.name, parent_paper.first_author,
                   parent_paper.url, parent_paper.local_path, id, keywords, connections)

    def __init__(self,
                 name: str = None,
                 first_author: str = None,
                 url: str = None,
                 local_path: str = None,
                 id: int = 0,
                 keywords: set = {},
                 connections: set = {}) -> None:
        super().__init__(name, first_author, url, local_path)
        self.id = id
        self._keywords = keywords
        self._connections = connections

    def add_keyword(self, keyword):
        self._keywords.add(keyword)

    def remove_keyword(self, keyword):
        self._keywords.remove(keyword)

    def add_connection(self, connection):
        self._connections.add(connection)

    def remove_connection(self, connection):
        self._connections.remove(connection)

    @property
    def connections(self):
        return self._connections

    @property
    def keywords(self):
        return self._keywords


class PaperGraph:
    def __init__(self):
        pass


doi = "10.1134/S154747712106008X"
paper = Paper.from_doi(doi)
paperNote = PaperNote.from_paper(paper, 1)
print(paperNote)
print(paperNote.id)
print(paperNote.connections)
