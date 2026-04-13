import streamlit as st
import pandas as pd

df = pd.read_excel("https://raw.githubusercontent.com/pnoone8/HHG_Helper/main/HHG.xlsx")

st.title("Happy Hunting Grounds Helper Tool")


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


selection = st.text_input("Enter a team name")

if selection:
    selection = selection.lower().strip()
    selection_words = selection.split()

    found = False
    results = {}

    for season in df.columns:
        for team in df[season].astype(str):
            team_lower = str(team).lower()
            team_words = team_lower.split()

            if all(word in team_words for word in selection_words):
                found = True

                if team not in results:
                    results[team] = []
                results[team].append(season)

    if found:
        for team, seasons in results.items():
            st.subheader(f"{team} have played in the Premier League in:")

            grouped = group_seasons(seasons)
            st.write(", ".join(grouped))
    else:
        st.error("Team not found")
