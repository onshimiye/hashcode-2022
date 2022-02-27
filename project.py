class Project:
    def __init__(self, languages, name, days, score, bbefore, roles, rs):
        self.langs = languages
        self.name = name
        self.days = days
        self.score = score
        self.bbefore = bbefore
        self.roles = roles
        self.rs = rs

    def __str__(self) -> str:
        
        return self.name + ' ' + str(self.roles)