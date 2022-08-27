from Application.DB import DBManager

db = DBManager()
db.creat_admin_tables()
db.creat_voters_tables()
db.inser_in_admins_table()
db.inser_in_voters_table()