from Application.DB import DBManager
from Application.voter import Voter
from Application.admin import Admin
from Application.election import Election


db = DBManager()
db.create_admin_table()
db.create_voter_table()
db.create_election_tables_table()
v1 = Voter(1, "1")
v1.add_to_db()
a1 = Admin(1, "1")
a1.add_to_db()
e1=Election(name=1, begin=1, end=1)
e1.add_to_db()
