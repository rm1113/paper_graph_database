class KeywordNode:
    def __init__(self,
                 name: str,
                 description: str = None) -> None:
        self._name = name
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def rename(self, new_name):
        self._name = new_name

    def change_description(self, new_description):
        self._description = new_description

    def __str__(self):
        return f"Keyword: {self._name}"

    def serialize(self):
        data = {
            'name': self.name,
            'description': self.description
        }
        return data


if __name__ == '__main__':
    k = KeywordNode('key')
    print(k)
    print(k.name, k.description)
    print(k.serialize())
    k.rename('new_key')
    k.change_description("new description")
    print(k)
    print(k.name, k.description)
    print(k.serialize())
