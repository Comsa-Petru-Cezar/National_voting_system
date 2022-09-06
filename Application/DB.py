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

    def create_voter_table(self):
        self.c.execute("""CREATE TABLE voters (
                    CNP integer
                    )""")
        self.conn.commit()

    def create_admin_table(self):
        self.c.execute("""CREATE TABLE admins (
                    id integer,
                    password text
                    )""")
        self.conn.commit()

    def create_election_tables_table(self):
        self.c.execute("""CREATE TABLE election_tables (
                            name text,
                            candidates int,
                            begin date,
                            end date
                            )""")
        self.conn.commit()

    def create_election_table(self, current_election):
        if current_election.transferable_vote:
            text = """CREATE TABLE {} (
                                                    candidate text,""".format(current_election.name)
            for c in range(1, current_election.number_of_candidates+1):
                text = text + """
                choice {} int,""".format(c)
            text = text + """
            )"""
            self.c.execute("""CREATE TABLE '{}' (
                                                    candidate text,
                                                    votes int
                                                    )""".format(current_election.name))
        else:
            self.c.execute("""CREATE TABLE '{}' (
                                        candidate text,
                                        votes int
                                        )""".format(current_election.name))
        self.conn.commit()

    def insert_in_voter_table(self, current_voter=None):

        self.c.execute("INSERT INTO voters VALUES ({},'{}')".format(current_voter.cnp, current_voter.region))
        self.conn.commit()

    def insert_in_admin_table(self, add_admin=None):
        self.c.execute("INSERT INTO admins VALUES ({},'{}')".format(add_admin.id, add_admin.password))
        self.conn.commit()

    def insert_in_election_tables_table(self, current_election=None):
        self.c.execute("INSERT INTO election_tables VALUES ('{}',{},{},{})".format(current_election.name,
                                                                                current_election.number_of_candidates,
                                                                                current_election.begin,
                                                                                current_election.end
                                                                                )
                       )
        self.conn.commit()

    def insert_in_election_table(self, current_election=None, current_candidate=None):
        if current_election.transferable_vote:
            pass
        else:
            self.c.execute("INSERT INTO '{}' VALUES('{}',0)".format(current_election.name, current_candidate.name))
        self.conn.commit()

    def select_from_voter_table(self, current_voter=None):
        if current_voter:
            self.c.execute("SELECT * FROM voters WHERE CNP={}".format(current_voter.cnp))
            select = self.c.fetchone()
        else:
            self.c.execute("SELECT * FROM voters")
            selct = self.c.fetchall()
        #print(select)#c.fetchmany(5)/.fetchone()
        return select

    def select_from_admin_table(self, current_admin=None, id=None):
        if current_admin:
            self.c.execute("SELECT * FROM admins WHERE id={} and password='{}'".format(current_admin.id, current_admin.password))
        elif id:
            self.c.execute("SELECT * FROM admins WHERE id={} and password='{}'".format(current_admin.id))
        select = self.c.fetchone()
        #print(select)  # c.fetchmany(5)/.fetchone()
        return select

    def select_from_election_tables_table(self, current_election=None):
        if current_election:
            self.c.execute("SELECT * FROM election_tables WHERE name='{}'".format(current_election.name))
        else:
            self.c.execute("SELECT * FROM election_tables")
        return self.c.fetchall()

    def select_from_election_table(self, current_election, current_candidate=None):
        if current_candidate:
            self.c.execute("Select * FROM '{}' WHERE candidate='{}'".format(current_election.name, current_candidate.name))
        else:
            self.c.execute("Select * FROM '{}'".format(current_election.name))
        return self.c.fetchall()

    def remove_from_voter_table(self, current_voter=None):
        self.c.execute("DELETE FROM voters WHERE cnp={}".format(current_voter.cnp))
        self.conn.commit()

    def remove_from_election_table(self, current_election=None, current_candidate=None):
        self.c.execute("DELETE FROM '{}' WHERE candidate='{}'".format(current_election.name, current_candidate.name))
        self.conn.commit()

    def update_candidate_in_election_table(self, current_election=None, current_candidate=None):
        self.c.execute("UPDATE '{}' set votes = {} WHERE candidate = '{}'".format(current_election.name, current_candidate.votes, current_candidate.name))
        self.conn.commit()

    def close(self):
        self.conn.close()
