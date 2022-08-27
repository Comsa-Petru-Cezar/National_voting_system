import PySimpleGUI as sg
from Application.DB import DBManager





def login_check(db, admin):
    a = db.check_admin(admin)
    if a:
        print("login")
        return True
    else:
        return False

def login_fail(db, win):
    win["text"].update("Login Failed. Please try again.")
    win.refresh()

def admin_login(db):
    layout = [
        [sg.Text("Welcome?", key="text")],
        [sg.Text("ID           "), sg.InputText()],
        [sg.Text("Password"), sg.InputText()],
        [sg.Button("Login")]
    ]
    login_win = sg.Window(title="National Voting Systm", layout=layout)

    while True:
        event, values = login_win.read()
        if event == "Login":
            if login_check(db, (values[0], values[1])):
                login_win.close()
                return True
            else:
                login_fail(db, login_win)
        elif event == sg.WIN_CLOSED:
            break

    login_win.close()
    return False

def insert_voter(db):
    layout = [
        [sg.Text("Voter:", key="text1"), ],
        [sg.Text("CNP"), sg.InputText(key="cnp")],
        [sg.Button("Insert Voter")],
        [sg.Button("Done")]
    ]
    insert_voter_win = sg.Window(title="Insert voters", layout=layout)

    while True:
        event, values = insert_voter_win.read()
        if event == "Done" or event == sg.WIN_CLOSED:
            break
        if event == "Insert Voter":

            if db.insert_in_voter_table(voter=(values["cnp"])):

                insert_voter_win["text1"].update("Voter added", text_color="white")
                insert_voter_win.refresh()
            else:
                insert_voter_win["text1"].update("Invalid values", text_color="red")
                insert_voter_win.refresh()
            insert_voter_win["cnp"].update("")

    insert_voter_win.close()

def remove_voter(db):
    layout = [
        [sg.Text("Voter:", key="text1"), ],
        [sg.Text("CNP"), sg.InputText(key="cnp")],
        [sg.Button("Remove Voter")],
        [sg.Button("Done")]
    ]
    remove_voter_win = sg.Window(title="Remove voters", layout=layout)

    while True:
        event, values = remove_voter_win.read()
        if event == "Done" or event == sg.WIN_CLOSED:
            break
        if event == "Remove Voter":
            if not db.remove_in_voter_table((values["cnp"])):
                remove_voter_win["text1"].update("Voter Removed", text_color="black")
                remove_voter_win.refresh()
            else:
                remove_voter_win["text1"].update("Invalid values", text_color="red")
                remove_voter_win.refresh()
            remove_voter_win["cnp"].update("")
    remove_voter_win.close()

def add_admin(db):
    layout = [
        [sg.Text("Voter:", key="text1"), ],
        [sg.Text("ID"), sg.InputText(key="id")],
        [sg.Text("Password"), sg.InputText(key="pass")],
        [sg.Button("Insert Admin")],
        [sg.Button("Done")]
    ]
    insert_admin_win = sg.Window(title="Insert admins", layout=layout)

    while True:
        event, values = insert_admin_win.read()
        if event == "Done" or event == sg.WIN_CLOSED:
            break
        if event == "Insert Admin":
            if db.insert_in_admin_table((values["id"], values["pass"])):
                insert_admin_win["text1"].update("Admin Added", text_color="white")
                insert_admin_win.refresh()
            else:
                insert_admin_win["text1"].update("Invalid values for admin", text_color="red")
                insert_admin_win.refresh()
            insert_admin_win["id"].update("")
            insert_admin_win["pass"].update("")
    insert_admin_win.close()


def admin_main(db):
    layout = [
        [sg.Button("Insert Voters")],
        [sg.Button("Remove Voters")],
        [sg.Button("Other Updates")],
        [sg.Button("Create Election")],
        [sg.Button("Inspect Election")],
        [sg.Button("Add Admin")],
        [sg.Button("Done")]
    ]
    admin_win = sg.Window(title="National Voting Systm", layout=layout)

    while True:
        event, values = admin_win.read()
        if event == "Done" or event == sg.WIN_CLOSED:
            break
        if event == "Insert Voters":
            insert_voter(db)
        if event == "Remove Voters":
            remove_voter(db)
        if event == "Add Admin":
            add_admin(db)

    admin_win.close()


def app_Admin():
    db = DBManager()

    if admin_login(db):
       admin_main(db)

    db.close()
