import csv
import math

# print for testing
def printdict(dictionary):
    print("-----")
    for line in dictionary:
        print(line, dictionary[line])
    print("-----")

# does project have enough teams assigned?
def teamCount():
    for proj in final:
        if len(final[proj]) < minteams:
            return False
    return True

# calculate disappointment (see readme for reasoning)
def calcDisappoint():
    total = 0
    for proj in final:
        for team in final[proj]:
            pref = teampicks[team].index(proj)
            disappoint = 3**(pref) - 1
            total += disappoint
    return total
            
# make dict of teams and their picks
# { teamname : [list of picks in order of preference]
# ...
# }
teampicks = {}
with open("code-olympics-selections.txt", "r") as file:
    for line in file:
        temp = line.strip().split(", ")
        teampicks[temp[0]] = temp[1:]
    del teampicks["Team"]

# make set of all possible options
options = set()
for line in teampicks:
    options.update(set(teampicks[line]))

# add not-selected options to the end of each team's picks.
for team in teampicks:
    teampicks[team] += list(options - set(teampicks[team]))


# least teams for each project
minteams = math.ceil(len(teampicks) / (len(options) - 1))

# make dict of teams assigned to each project
final = {}
for option in options:
    final[option] = {team for team in teampicks}


# Remove team from its least preferred project
# until min count of teams on each project is reached.
for pick in range(len(options)-1,0,-1):
    for team in teampicks:
        if teamCount():
            proj = teampicks[team][pick]
            final[proj].remove(team)

# If team has more than one project, add team to list of dupes
duplicates = []
for team in teampicks:
    # list of projects each team has
    thing = []
    for proj in final:
        for team2 in final[proj]:
            if team == team2:
                thing.append(proj)
    if len(thing) > 1:
        duplicates += [team]*(len(thing)-1)

while len(duplicates) != 0:
    # find proj with most teams
    longest = 0
    for proj in final:
        if len(final[proj]) > longest:
            longproj = proj
            longest = len(final[proj])
    # in the proj with most teams
    # check each team for least preference.
    # delete team with least preference from project.
    leastpref = -1
    for team in final[longproj]:
        pref = teampicks[team].index(longproj)
        if pref > leastpref and team in duplicates:
            leastpref = pref
            leastteam = team
    final[longproj].remove(leastteam)
    duplicates.remove(leastteam)

printdict(final)
print("Disappointment:",calcDisappoint())
            









