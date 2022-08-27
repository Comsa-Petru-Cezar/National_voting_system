from Application.DB import DBManager

db = DBManager()
db.creat_admin_tables()
db.creat_voter_tables()
db.create_election_tables_table()
voter = (1,)
db.insert_in_voter_table(voter)
admin = (1, "1")
db.insert_in_admin_table(admin)