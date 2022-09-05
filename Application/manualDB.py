from Application.DB import DBManager
from Application.voter import Voter
from Application.admin import Admin
from Application.election import Election


db = DBManager()
db.create_admin_table()
db.create_voter_table()
db.create_election_tables_table()
v1 = Voter(1)
db.insert_in_voter_table(v1)
a1 = Admin(1, "1")
db.insert_in_admin_table(a1)
