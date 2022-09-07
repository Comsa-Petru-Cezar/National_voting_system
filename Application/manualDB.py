from Application.DB import DBManager
from Application.voter import Voter
from Application.admin import Admin
from Application.election import Election


db = DBManager()
try:
    db.clean_all()
except:
    pass
db.create_admin_table()
db.create_voter_table()
db.create_election_tables_table()
db.create_votes_table()
v1 = Voter("1990627014667")
v1.add_to_db()
a1 = Admin(1, "luios12")
a1.add_to_db()
e1 = Election(name="Presidential Election", begin="11/09/2022", end="13/09/2022")
e1.add_to_db()
