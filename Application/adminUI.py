import PySimpleGUI as sg
from Application.voter import voter
from Application.admin import admin




def admin_login():
    layout = [
        [sg.Text("Welcome?", key="text")],
        [sg.Text("ID           "), sg.InputText(key="id")],
        [sg.Text("Password"), sg.InputText(key="pass")],
        [sg.Button("Login")]
    ]
    login_win = sg.Window(title="National Voting System", layout=layout)

    while True:
        event, values = login_win.read()
        if event == "Login":
            current_admin = admin(values["id"], values["pass"])
            if current_admin.login():
                login_win.close()
                return True
            else:
                login_win["text"].update("Login Failed. Please try again.")
                login_win["id"].update("")
                login_win["pass"].update("")
                login_win.refresh()
        elif event == sg.WIN_CLOSED:
            break

    login_win.close()
    return False


def insert_voter():
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
            current_voter = voter(values["cnp"])
            if current_voter.in_db():
                insert_voter_win["text1"].update("Invalid values", text_color="red")
                insert_voter_win.refresh()

            else:
                current_voter.add_to_db()
                insert_voter_win["text1"].update("Voter added", text_color="white")
                insert_voter_win.refresh()
            insert_voter_win["cnp"].update("")

    insert_voter_win.close()


def remove_voter():
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
            current_voter = voter(values["cnp"])
            if current_voter.in_db():
                current_voter.remove_from_db()
                remove_voter_win["text1"].update("Voter Removed", text_color="black")
                remove_voter_win.refresh()
            else:
                remove_voter_win["text1"].update("Invalid values", text_color="red")
                remove_voter_win.refresh()
            remove_voter_win["cnp"].update("")
    remove_voter_win.close()


def add_admin():
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
            add_admin = admin(values["id"], values["pass"])
            if add_admin.in_db():
                add_admin.add_to_db()
                insert_admin_win["text1"].update("Admin Added", text_color="white")
                insert_admin_win.refresh()
            else:
                insert_admin_win["text1"].update("Invalid values for admin", text_color="red")
                insert_admin_win.refresh()
            insert_admin_win["id"].update("")
            insert_admin_win["pass"].update("")
    insert_admin_win.close()


def manage_elections():
    layout = [
        [sg.Button("Create Election")],
        [sg.Button("Done")]
    ]

    manage_elections_win = sg.Window(title="Manage Elections", layout=layout)

    while True:
        event, values = manage_elections_win.read()
        if event == "Done" or event == sg.WIN_CLOSED:
            break

    manage_elections_win.close()


def admin_main():
    layout = [
        [sg.Button("Insert Voters")],
        [sg.Button("Remove Voters")],
        [sg.Button("Other Updates")],
        [sg.Button("Manage Elections")],
        [sg.Button("Add Admin")],
        [sg.Button("Done")]
    ]
    admin_win = sg.Window(title="National Voting Systm", layout=layout)

    while True:
        event, values = admin_win.read()
        if event == "Done" or event == sg.WIN_CLOSED:
            break
        if event == "Insert Voters":
            insert_voter()
        if event == "Remove Voters":
            remove_voter()
        if event == "Add Admin":
            add_admin()
        if event == "Manage Elections":
            manage_elections()

    admin_win.close()


def app_Admin():
    if admin_login():
        admin_main()

