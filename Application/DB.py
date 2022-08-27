#todo
#


import sqlite3

class DBManager():

    def __init__(self):
        try:
            self.conn = sqlite3.connect('Application/voting.db')
        except:
            self.conn = sqlite3.connect('voting.db')
        self.c = self.conn.cursor()
        self.conn.commit()

    def creat_voter_tables(self):
        self.c.execute("""CREATE TABLE voters (
                    CNP integer
                    )""")
        self.conn.commit()

    def creat_admin_tables(self):
        self.c.execute("""CREATE TABLE admins (
                    id integer,
                    password text
                    )""")
        self.conn.commit()

    def create_election_tables_table(self):
        self.c.execute("""CREATE TABLE election_tables (
                            name text,
                            period date
                            )""")
        self.conn.commit()

    def creat_election_table(self):
        pass

    def insert_in_voter_table(self, current_voter=None):

        self.c.execute("INSERT INTO voters VALUES ('{}')".format(current_voter.cnp))
        self.conn.commit()

    def insert_in_admin_table(self, add_admin=None):
        self.c.execute("INSERT INTO admins VALUES ('{}','{}')".format(add_admin.id,add_admin.password))
        self.conn.commit()

    def select_from_voter_table(self, current_voter=None):
        self.c.execute("SELECT * FROM voters WHERE CNP='{}'".format(current_voter.cnp))
        select = self.c.fetchone()
        #print(select)#c.fetchmany(5)/.fetchone()
        return select

    def select_from_admin_table(self, current_admin=None, id=None):
        if current_admin:
            self.c.execute("SELECT * FROM admins WHERE id='{}' and password='{}'".format(current_admin.id, current_admin.password))
        elif id:
            self.c.execute("SELECT * FROM admins WHERE id='{}' and password='{}'".format(current_admin.id))
        select = self.c.fetchone()
        #print(select)  # c.fetchmany(5)/.fetchone()
        return select

    def remove_from_voter_table(self, current_voter=None):
        self.c.execute("DELETE FROM voters WHERE ('{}')".format(current_voter.cnp))
        self.conn.commit()





    def close(self):
        self.conn.close()