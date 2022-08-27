from Application.DB import DBManager

class election():
    def __init__(self, name, db=None):
        self.name = name

        if db:
            self.extract_from_db(db)
        else:
            self.track = {}

    def extract_from_db(self,db):
        pass