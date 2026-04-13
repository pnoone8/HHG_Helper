import pandas as pd

df = pd.read_excel("/Users/patricknoone/Desktop/HHG.xlsx")


def group_seasons(seasons):
    seasons = sorted(seasons)

    groups = []
    current_group = [seasons[0]]

    for i in range(1, len(seasons)):
        prev_year = int(seasons[i-1][:4])
        curr_year = int(seasons[i][:4])

        if curr_year == prev_year + 1:
            current_group.append(seasons[i])
        else:
            groups.append(current_group)
            current_group = [seasons[i]]

    groups.append(current_group)

    ranges = []
    for g in groups:
        if len(g) == 1:
            ranges.append(g[0])
        else:
            ranges.append(f"{g[0]}–{g[-1]}")

    return ranges


while True:
    selection = input("Which team would you like to check?\n").strip()\
        .lower()
    selection_words = selection.split()

    found = False
    results = {}

    for season in df.columns:
        for team in df[season].astype(str):
            team_lower = team.lower()
            team_words = team_lower.split()

            if all(word in team_words for word in selection_words):
                found = True

                if team not in results:
                    results[team] = []
                results[team].append(season)

    if found:
        for team, seasons in results.items():
            print(f"\n{team} have played in the Premier League in:\n")

            grouped = group_seasons(seasons)
            print(", ".join(grouped))

        break
    else:
        print("Team not found, please try again.\n")
