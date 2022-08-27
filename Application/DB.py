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

    def insert_in_voter_table(self, voter=()):

        if self.select_from_voter_table(voter) == None:
            self.c.execute("INSERT INTO voters VALUES ('{}')".format(voter[0]))
            self.conn.commit()
            return True
        return False

    def insert_in_admin_table(self, admin): #admins=((),())
        if self.select_from_admin_table(id=admin[0]):
            return False
        self.c.execute("INSERT INTO admins VALUES ('{}','{}')".format(admin[0],admin[1]))
        self.conn.commit()
        return True


    def select_from_voter_table(self, voter=()):
        self.c.execute("SELECT * FROM voters WHERE CNP='{}'".format(voter[0]))
        select = self.c.fetchone()
        #print(select)#c.fetchmany(5)/.fetchone()
        return select

    def select_from_admin_table(self, admin=(), id=None):
        if id != None:
            self.c.execute("SELECT * FROM admins WHERE id='{}'".format(id))
        else:
            self.c.execute("SELECT * FROM admins WHERE id='{}' and password='{}'".format(admin[0], admin[1]))
        select = self.c.fetchone()
        #print(select)  # c.fetchmany(5)/.fetchone()
        return select

    def check_admin(self, admin):
        self.c.execute("SELECT * FROM admins WHERE id='{}' and password='{}'".format(admin[0], admin[1]))
        select = self.c.fetchone()
        # print(select)  # c.fetchmany(5)/.fetchone()
        if select != None:
            return True
        else:
            return False

    def remove_in_voter_table(self, voter=()): #voters = ()
        if self.select_from_voters_table(voter[0]):
            print(self.select_from_voters_table(voter[0]))
            self.c.execute("DELETE FROM voters WHERE ('{}')".format(voter[0]))
            self.conn.commit()
            return True
        return False




    def close(self):
        self.conn.close()