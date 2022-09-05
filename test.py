current_election="X"
number_of_candidates=9
text = """CREATE TABLE {} (""".format(current_election)
for c in range(1,number_of_candidates+1):
    text = text + """
    choice {} int""".format(c)
text = text + """
)"""
print(text)