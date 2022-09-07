from Application.DB import DBManager
from Application.candidate import Candidate
from datetime import datetime


class Election():
    def __init__(self, election_from_db=None, name=None, begin=None, end=None,):
        if election_from_db:
            self.name = election_from_db[0]
            self.begin = election_from_db[1]
            self.end = election_from_db[2]
        else:
            self.name = name
            self.begin = begin
            self.end = end


    @classmethod
    def get_elections(cls, current_voter=None):
        db = DBManager()
        elections_list = []
        voted_list = []
        if current_voter:
            voted_list = db.get_election_from_voters_table(current_voter)

        for e in db.select_from_election_tables_table():
            if current_voter:
                today = datetime.today().date()
                if not (e[0],) in voted_list and datetime.strptime(e[1], "%d/%m/%Y").date() <= today and datetime.strptime(e[2], "%d/%m/%Y").date() >= today:
                    elections_list.append(Election(election_from_db=e))
            else:
                elections_list.append(Election(election_from_db=e))
        db.close()
        return elections_list

    def is_in_db(self):
        db = DBManager()
        if db.select_from_election_tables_table(self):
            return True
            db.close()
        else:
            return False
            db.close()

    def add_to_db(self):
        db = DBManager()
        db.insert_in_election_tables_table(self)
        db.create_election_table(self)
        db.close()

    def get_candidates(self):
        db = DBManager()
        candidates_list = []
        for c in db.select_from_election_table(self):
            candidates_list.append(Candidate(c))
        return candidates_list
        db.close()

    @staticmethod
    def sql_injection(text):
        danger_list = [" AND ", " OR ", " SELECT ", " WHERE ", " UNION ", " DELETE ", " INSERT ", " ORDER ", " UPDATE ",
                       " JOIN ", ",", ")", "'"]

        for d in danger_list:
            if text.find(d) != -1:
                return False
        return True

    def self_check(self):


        try:
            b = datetime.strptime(self.begin, "%d/%m/%Y").date()
            e = datetime.strptime(self.end, "%d/%m/%Y").date()
            if b > e:
                return False
        except:
            return False

        return (Election.sql_injection(self.name) and Election.sql_injection(self.begin) and Election.sql_injection(self.end))

    def __repr__(self):
        return "'{}' date: ('{}' - '{}')".format(self.name, self.begin, self.end)