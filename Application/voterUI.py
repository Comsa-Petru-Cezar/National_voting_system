import PySimpleGUI as sg
from Application.DB import DBManager





def login_check(db, voters):
    a = db.select_from_voters_table(voters)
    if a:
        print("login")
        return True
    else:
        return False

def login_fail(db, win):
    win["text"].update("Login Failed. Please try again.")
    win.refresh()



def voter_login(db):
    layout = [
        [sg.Text("Welcome?", key="text")],
        [sg.Text("CNP"), sg.InputText()],
        [sg.Button("Login")]
    ]
    login_win = sg.Window(title="National Voting Systm", layout=layout)

    while True:
        event, values = login_win.read()
        if event == "Login":
            if login_check(db, (values[0])):
                login_win.close()
                return True
            else:
                login_fail(db, login_win)
        elif event == sg.WIN_CLOSED:
            break

    login_win.close()
    return False

def voter_main(db):
    layout = [
        [sg.Button("Yes")]
    ]
    voter_win = sg.Window(title="National Voting Systm", layout=layout)

    while True:
        event, values = voter_win.read()
        if event == "Yes" or event == sg.WIN_CLOSED:
            break


    voter_win.close()


def app_Voter():
    db = DBManager()

    if voter_login(db):
       voter_main(db)

    db.close()
