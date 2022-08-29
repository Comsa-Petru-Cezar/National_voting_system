from Application.DB import DBManager
from Application.voter import voter
from Application.admin import admin
from Application.election import election


db = DBManager()
db.create_admin_table()
db.create_voter_table()
db.create_election_tables_table()
v1 = voter(1)
db.insert_in_voter_table(v1)
a1 = admin(1, "1")
db.insert_in_admin_table(a1)
