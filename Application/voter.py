from Application.DB import DBManager

class voter():

    def __init__(self, cnp):
        self.cnp = cnp

    def in_db(self):
        db = DBManager()
        if db.select_from_voter_table(self):
            return True
            db.close()
        else:
            return False
            db.close()

    def add_to_db(self):
        db = DBManager()
        db.insert_in_voter_table(self)
        db.close()

    def remove_from_db(self):
        db = DBManager()
        db.remove_from_voter_table(self)
        db.close()

    def __repr__(self):
        return "'{}'".format(self.cnp)