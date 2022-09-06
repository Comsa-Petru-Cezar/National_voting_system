from Application.DB import DBManager


class Candidate():

    def __init__(self, candidate_from_db=None, name=None):

        if candidate_from_db:
            self.name = candidate_from_db[0]
            self.votes = candidate_from_db[1]
        else:

            self.name = name
            self.votes = 0

    def is_in_db(self, current_election):
        db = DBManager()

        if db.select_from_election_table(current_election=current_election, current_candidate=self):
            db.close()
            return True
        else:
            db.close()
            return False

    def add_to_db(self, current_election):
        db = DBManager()
        db.insert_in_election_table(current_election=current_election, current_candidate=self)
        db.close()

    def remove_from_db(self, current_election):
        db = DBManager()
        db.remove_from_election_table(current_election=current_election, current_candidate=self)
        db.close()

    def self_check(self):

        return True

    def get_one_vote(self, current_election):
        self.votes = self.votes + 1
        print(self.name, " ", self.votes)
        db = DBManager()
        db.update_candidate_in_election_table(current_election, self)
        db.close()

        pass