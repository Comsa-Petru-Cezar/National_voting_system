import PySimpleGUI as sg
from Application.voter import Voter
from Application.admin import Admin
from Application.election import Election
from Application.candidate import Candidate

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
            current_admin = Admin(values["id"], values["pass"])
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
            current_voter = Voter(values["cnp"])
            if not current_voter.is_in_db() and current_voter.self_check():
                current_voter.add_to_db()
                insert_voter_win["text1"].update("Voter added", text_color="white")

            else:
                insert_voter_win["text1"].update("Invalid values", text_color="red")
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
            current_voter = Voter(values["cnp"])
            if current_voter.is_in_db():
                current_voter.remove_from_db()
                remove_voter_win["text1"].update("Voter Removed", text_color="black")

            else:
                remove_voter_win["text1"].update("Invalid values", text_color="red")
            remove_voter_win["cnp"].update("")
            remove_voter_win.refresh()
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
            add_admin = Admin(values["id"], values["pass"])
            if not add_admin.is_in_db() and add_admin.self_check():
                add_admin.add_to_db()
                insert_admin_win["text1"].update("Admin Added", text_color="white")

            else:
                insert_admin_win["text1"].update("Invalid values for admin", text_color="red")
            insert_admin_win["id"].update("")
            insert_admin_win["pass"].update("")
            insert_admin_win.refresh()
    insert_admin_win.close()


def create_election():
    layout = [
        [sg.Text("", key="text1"), ],
        [sg.Text("Name:"), sg.InputText(key="name")],
        [sg.Text("Number of candidates:"), sg.InputText(key="number")],
        [sg.Text("Begin date dd/mm/yyyy:"), sg.InputText(key="begin")],
        [sg.Text("End date dd/mm/yyyy:"), sg.InputText(key="end")],
        [sg.Checkbox("Transferable vote", default=False, key="tv")],
        [sg.Button("Create Election")],
        [sg.Button("Done")]
    ]
    create_election_win = sg.Window(title="Insert admins", layout=layout)

    while True:
        event, values =  create_election_win.read()
        if event == "Done" or event == sg.WIN_CLOSED:
            break
        if event == "Create Election":
            current_election = Election(name=values["name"], number_of_candidates=values["number"], begin=values["begin"], end=values["end"], transferable_vote=values["tv"])
            if not current_election.is_in_db() and current_election.self_check():
                current_election.add_to_db()
                create_election_win["text1"].update("Election Created", text_color="white")
                print(current_election.self_check())
            else:
                create_election_win["text1"].update("Invalid data", text_color="red")
            create_election_win["name"].update("")
            create_election_win["number"].update("")
            create_election_win["begin"].update("")
            create_election_win["end"].update("")
            create_election_win["tv"].update("")
            create_election_win.refresh()



    create_election_win.close()


def add_candidate(current_election):
    layout = [
        [sg.Text("Add Candidate", key="text")],
        [sg.Text("Candidate name: "), sg.InputText(key="name")],
        [sg.Button("Add Candidate")],
        [sg.Button("Done")]
                      ]

    add_candidate_win = sg.Window(title="Add Candidate", layout=layout)

    while True:
        event, values = add_candidate_win.read()

        if event == "Done" or event == sg.WIN_CLOSED:
            break

        if event == "Add Candidate":
            current_candidate = Candidate(name=values["name"],)
            if not current_candidate.is_in_db(current_election):
                add_candidate_win["text"].update("Candidate added", text_color="black")
                current_candidate.add_to_db(current_election=current_election)
            else:
                add_candidate_win["text"].update("Invalid values for candidate", text_color="red")
            add_candidate_win["name"].update("")
            add_candidate_win.refresh()

    add_candidate_win.close()


def manage_election(current_election):
    layout = []
    candidates_list = current_election.get_candidates()
    for c in candidates_list:
        layout.append([sg.Text("{} -- {}".format(c.name, c.votes)), sg.Button("Remove", key="{}".format(c.name))])
    layout.append([sg.Button("Add Candidate")])
    layout.append([sg.Button("Done")])

    manage_election_win = sg.Window(title="Manage Election '{}'".format(current_election.name), layout=layout)

    while True:
        event, values = manage_election_win.read()

        if event == "Done" or event == sg.WIN_CLOSED:
            break

        if event == "Add Candidate":
            manage_election_win.close()
            add_candidate(current_election)
            break
        if event:
            for c in candidates_list:
                if event == "{}".format(c.name):
                    c.remove_from_db(current_election)
                    manage_election_win.close()
                    break

    manage_election_win.close()


def manage_elections():
    elections_list = Election.get_elections()
    layout = []
    for e in elections_list:
        layout.append([sg.Button(" {} -- ({},{}) ".format(e.name, e.begin, e.end))])
    layout.append([sg.Button("Done")])

    manage_elections_win = sg.Window(title="Manage Elections", layout=layout)

    while True:
        event, values = manage_elections_win.read()

        if event == "Done" or event == sg.WIN_CLOSED:
            break
        elif event:
            for e in elections_list:
                if event == " {} -- ({},{}) ".format(e.name, e.begin, e.end):
                    manage_elections_win.close()
                    manage_election(e)
                    break

    manage_elections_win.close()


def admin_main():
    layout = [
        [sg.Button("Insert Voters")],
        [sg.Button("Remove Voters")],
        [sg.Button("Other Updates")],
        [sg.Button("Create Election")],
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
        if event == "Create Election":
            create_election()
        if event == "Manage Elections":
            manage_elections()


    admin_win.close()


def app_admin():
    if admin_login():
        admin_main()

