import PySimpleGUI as sg
from Application.voter import Voter
from Application.election import Election


def voter_login():
    layout = [
        [sg.Text("Welcome?", key="text")],
        [sg.Text("CNP"), sg.InputText(key="cnp")],
        [sg.Button("Login")]
    ]
    voter_login_win = sg.Window(title="National Voting System", layout=layout)

    while True:
        event, values = voter_login_win.read()
        if event == "Login":
            current_voter = Voter(cnp=values["cnp"])
            if current_voter.self_check() and current_voter.is_in_db():
                voter_login_win.close()
                return current_voter
            else:
                voter_login_win["text"].update("Login Failed. Please try again.")
                voter_login_win["cnp"].update("")
                voter_login_win.refresh()
        elif event == sg.WIN_CLOSED:
            break

    voter_login_win.close()
    return False


def vote_on_election(current_election, current_voter):
    layout = []
    candidates_list = current_election.get_candidates()
    i = 0
    for c in candidates_list:
        i = i + 1
        layout.append([sg.Radio(text=" {}".format(c.name), group_id="Radio1", default=False, key="{}".format(i))])

    layout.append([sg.Radio(text="None", group_id="Radio1", default=False)])

    layout.append([sg.Button("Vote")])

    election_win = sg.Window(title="{}".format(current_election.name), layout=layout)

    while True:
        event, values = election_win.read()
        if event == "Vote" or event == sg.WIN_CLOSED:
            i = 1
            while i <= len(candidates_list) and (not values["{}".format(i)]):
                i = i + 1
            if i <= len(candidates_list):
                candidates_list[i-1].get_one_vote(current_election, current_voter)
        break

    election_win.close()


def voter_main(current_voter):
    elections_list = Election.get_elections(current_voter)
    layout = []
    for e in elections_list:
        layout.append([sg.Button(" {} -- ({},{}) ".format(e.name, e.begin, e.end), key="{}".format(e.name), )])
    layout.append([sg.Button("Done")])

    voter_win = sg.Window(title="National Voting System", layout=layout)

    while True:
        event, values = voter_win.read()
        if event == "Done" or event == sg.WIN_CLOSED:
            break
        elif event:
            for e in elections_list:
                if event == "{}".format(e.name):
                    vote_on_election(current_election=e, current_voter=current_voter)
                    voter_win["{}".format(e.name)].update(visible=False)
                    voter_win.refresh()
    voter_win.close()


def app_voter():
    current_voter = voter_login()
    if current_voter:
        voter_main(current_voter)

