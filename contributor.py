class Contributor:
    def __init__(self, languages, name):
        self.lang = languages
        self.name = name


    def improve(self, language):
        self.lang[language] += 1

    def __str__(self) -> str:
        return self.name

    # def __cmp__(self, other):
    #     return cmp((self.last, self.first), (other.last, other.first))

    # def __eq__(self, other):
    #     return ((self.languages, self.first) == (other.last, other.first))