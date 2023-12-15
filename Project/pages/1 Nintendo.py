import pandas as pd
import streamlit as sl
import main

sl.markdown("# Nintendo")
sl.sidebar.markdown("# Nintendo")
game = main.game


text = "Nintendo Analysis"

text

nintendo = game.filter(items=['Publisher'], axis=1)
nintendo_total = nintendo.value_counts()['Nintendo']
total = int(nintendo.count());
percent = int(nintendo_total/total * 100)
text = f"Just to count Nintendo takes up {nintendo_total} of the {total} entries in this dataframe, that would be {percent}% of the whole set! I'll get into how that stacks up against other publishers a little bit later."
text
nintendo = game.loc[game['Publisher'] == 'Nintendo']
nintendo
nintendo_sales = nintendo.sort_values(by='Global_Sales', ascending=True)
text = "Heres what that set looks like just, Just Nintendo this time, and still incredibly Daunting!"
text
sl.bar_chart(nintendo_sales, x="Year", y=["Global_Sales"], color='Name')
text = "Take a look at this bar chart it becomes obvious that the most profitable release year for Nintendo was 2006, which makes sense it coincides with the realease of the Nintendo Wii and also the highest selling game of all time Wii Sports. Lets take a bit of a deeper dive into 2006 for Nintendo"
text
nintendo_six_sales = nintendo.loc[nintendo['Year'] == 2006]
nintendo_six_sales
tot = int(nintendo_six_sales["Name"].count())
text = f"This the sales of every game released by Nintendo in 2006. It contains 3 of the top 10 games including the number 1 game like previouly mentioned, with another game in the top 25. This is followed but an incredibly steep drop off where the remaining {tot - 4} games don't even crack the top 100"
text
sl.bar_chart(nintendo_six_sales, x="Genre", y=['Global_Sales'], color='Name')
text = "Interesting to look at this year and see how much of the profits were carried by Wii Sports. Interesting that a console exclusive game is the highest grossing, I feel it is important to note that Wii Sports was sold with the Wii so that data is essentially the sales of the Wii"
text
total_sales = int(nintendo["Global_Sales"].sum() * 1000000)
text = f"Nintendo as a publisher is a quite profitable coming in with total of {total_sales} sales overall when this list was created. Curious how they stack up against other publishers chek out the publishers section."
text