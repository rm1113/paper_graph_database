from pathlib import Path
import warnings
import requests


class DocumentNode:
    cross_ref_url = 'https://api.crossref.org/works/'

    @classmethod
    def from_doi(cls, doi: str):
        # TODO: remove to controller stage
        url = cls.cross_ref_url + f"/{doi}"
        res = requests.get(url)
        if res.status_code == 200:
            metadata = res.json()['message']
            title = metadata['title'][0]
            author = [a for a in metadata['author'] if a['sequence'] == 'first'][0]
            author = f"{author['given']} {author['family']}"
            date = str(metadata['published']['date-parts'][0][0])  # TODO: check how it works properly
            return cls(title, author, date, doi, local_file_path=None)
        else:
            warnings.warn(f"Can't read metadata from given doi with status {res.status_code}")
            return None

    def __init__(self,
                 title: str,
                 author: str = None,
                 date: str = None,
                 doi: str = None,
                 local_file_path: str = None
                 ) -> None:
        self._title = title
        self._author = author
        self._date = date
        self._doi = doi
        if local_file_path is not None:
            try:
                self._local_file_path = Path(local_file_path)
            except ValueError:
                warnings.warn("Can't convert given path to <pathlib.Path> object")
                self._local_file_path = None
        else:
            self._local_file_path = None

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def date(self):
        return self._date

    @property
    def doi(self):
        return self._doi

    @property
    def local_file_path(self):
        return self._local_file_path

    def change_title(self, new_title):
        self._title = new_title

    def change_author(self, new_author):
        self._author = new_author

    def change_doi(self, new_doi):
        self._doi = new_doi

    def change_date(self, new_date):
        self._date = new_date

    def change_local_path(self, new_path):
        self._local_file_path = Path(new_path)

    def __str__(self):
        line = f"Title: {self.title}\n"
        line += f"Author: {self.author}\n"
        line += f"Date: {self.date}\n"
        line += f"DOI: {self.doi}\n"
        line += f"local path: {self.local_file_path}"
        return line

    def serialize(self):
        data = {
            'title': self.title,
            'author': self.author,
            'date': self.date,
            'doi': self.doi,
            'local_path': str(self.local_file_path)
        }
        return data

    def __eq__(self, other):
        if not isinstance(other, DocumentNode):
            raise TypeError(f"Can't compare <DocumentNode> and {type(other)}")
        other_ser = other.serialize()
        for key, value in self.serialize().items():
            if value != other_ser[key]:
                return False
        return True


if __name__ == "__main__":
    doi = '10.1140/epja/s10050-022-00761-3'
    doc = DocumentNode.from_doi(doi)
    print(doc)
    # url = 'http://dx.doi.org/10.1016/j.nima.2023.168233'
    # url = "https://api.crossref.org/works/10.13140/RG.2.2.29015.14248"


