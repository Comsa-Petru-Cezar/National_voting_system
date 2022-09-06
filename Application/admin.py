from Application.DB import DBManager

class Admin():

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

    def is_in_db(self):
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

    @staticmethod
    def sql_injection(text):
        danger_list = [" AND ", " OR ", " SELECT ", " WHERE ", " UNION ", " DELETE ", " INSERT ", " ORDER ", " UPDATE ",
                       " JOIN ", ",", ")", "'"]

        for d in danger_list:
            if text.find(d) == -1:
                return False
        return True

    def self_check(self):
        try:
            nid = int(self.id)
        except:
            return False
        if len(self.password) < 5 or len(self.password) > 15:
            return False

        return Admin.sql_injection(self.password)

