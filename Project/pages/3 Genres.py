"""The Genres Page of my Web App

Author: Sam Dansereau
Class: CSI-260-02
Assignment: Final Project
Due Date: December 15th 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
import streamlit as sl
import pandas as pd
import main

sl.markdown("# Genres")
sl.sidebar.markdown("# Genres")
game = main.game

body = "Genre Analysis"
body

gen_totals = game.groupby('Genre')['Genre'].count()
gen_totals = gen_totals.sort_values(ascending = False)
gen_total = gen_totals.count()

text = f"A total of {gen_total} make up the list of genres in the set as seen below "
gen_totals
text

sl.line_chart(game, x="Year", y="Global_Sales", color="Genre")
text = "As you can see there has never really been one genre that has overpowered the market for all time it's interesting that each genre has had moments in the sun"
text
text = "This graph isn't the most valuble data overall especilly with the outlier that is Wii sports carrying the sports genre to that peak"
text
text = "Genres are rather difficult to parse, and it's hard to give a game one genre. For a recent example, turn based RPG's were quite low on the spectrum of genre and when researcing that if you wanted to make one you would see that, but if you researched that in the last year would receive very different reults due to the massive succes of Larian's Studios Baldurs Gate 3. I think using gneres to determine psosible profit can be beneficial but more on a case to case basis rather then an overall one."
text