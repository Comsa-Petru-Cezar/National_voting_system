from Application.DB import DBManager

class admin():

    def __init__(self, id, password):
        self.id = id
        self.password = password

    def login(self):
        db = DBManager()
        if db.select_from_admin_table(self):
            db.close()
            return True
        else:
            db.close()
            return False

    def in_db(self):
        db = DBManager()
        if db.select_from_admin_table(self):
            db.close()
            return True
        else:
            db.close()
            return False

    def add_to_db(self):
        db = DBManager()
        db.insert_in_admin_table(add_admin=self)
        db.close()