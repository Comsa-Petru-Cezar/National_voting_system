from Application.DB import DBManager

class Voter():

    def __init__(self, cnp):
        self.cnp = cnp

    def is_in_db(self):
        db = DBManager()
        if db.select_from_voter_table(self):
            return True
            db.close()
        else:
            return False
            db.close()

    def add_to_db(self):
        db = DBManager()
        if self.self_check():
            db.insert_in_voter_table(self)
        db.close()

    def remove_from_db(self):
        db = DBManager()
        db.remove_from_voter_table(self)
        db.close()

    def __repr__(self):
        return "'{}'".format(self.cnp)

    def self_check(self):
        if len(self.cnp) != 13:
            return False
        try:
            s = int(self.cnp[0])
            a = int(self.cnp[1:3])
            l = int(self.cnp[3:5])
            z = int(self.cnp[5:7])
            j = int(self.cnp[7:9])
            n = int(self.cnp[9:12])
            c = int(self.cnp[12])
        except:
            return False

        if s < 1 or s > 8:
            return False

        if l < 1 or l > 12:
            return False

        if z > 31:
            return False

        if j < 1 or j > 52:
            return False

        if n == 0:
            return False

        ccc = "279146358279"
        csum = 0

        for i in range(0, 12):
            csum = csum + int(self.cnp[i]) * int(ccc[i])

        cc = csum % 11
        if cc == 10:
            cc = 1
        if cc != c:
            return False

        return True
