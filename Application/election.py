from Application.DB import DBManager
from Application.candidate import Candidate


class Election():
    def __init__(self, election_from_db=None, name=None, number_of_candidates=None, begin=None, end=None, transferable_vote=False):
        if election_from_db:
            self.name = election_from_db[0]
            self.number_of_candidates = election_from_db[1]
            self.begin = election_from_db[2]
            self.end = election_from_db[3]
            self.transferable_vote = election_from_db[4]
        else:
            self.name = name
            self.number_of_candidates = number_of_candidates
            self.begin = begin
            self.end = end
            self.transferable_vote = transferable_vote
            """if db:
                self.extract_from_db()
            else:
                self.track = {}"""

    def extract_from_db(self):
        pass

    @classmethod
    def get_elections(cls):
        db = DBManager()
        elections_list = []
        for e in db.select_from_election_tables_table():
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

    def self_check(self):
        return True

    def __repr__(self):
        return "'{}' date: ('{}' - '{}') stv: ".format(self.name, self.begin, self.end, self.transferable_vote)