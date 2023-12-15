import streamlit as sl
import pandas as pd
import main

sl.markdown("# Publishers")
sl.sidebar.markdown("# Publishers")
game = main.game

body = "Publisher Analysis"
body
text = "So we looked at Nintendo and there dominance over the industry but is that the whole story? Taking a look how the other publishers might stack up against the giant"
text
publish = game[:100]
publish
text = "This is the top 100 games on the list, if you notice the top 14 are all claimed by Nintendo but once you get out of it you notice the variety kicks it up a notch"
text
pub_totals = game.groupby('Publisher')['Publisher'].count()
pub_totals
pub_total = pub_totals.count()
text = f"This is a list that is compiled of ever publisher and they're number of appearances in the list. There is {pub_total} total publishers present and scrolling through will show you that despite the intial strong showing Nintendo might not be the top dog overall"
text
pub_totals = pub_totals.sort_values(ascending = False)
pub_totals
text = "EA taking the lead is quite interesting to me especially if you are in the space and the amount of talk you here about them. But they Eclipse Nintendo almost doubling there amount of entries"
text
ea = game.loc[game['Publisher'] == 'Electronic Arts']
sl.bar_chart(ea, x="Year", y="Global_Sales", color=None)
text = "Just as comparison to Nintendo's year by year sales EA seems to have had most of there profit in games published in 2009, Interesting to look as EA doesn't have there own console like nintendo does and doesn't puclish exclusively either"
ea_nine_sales = ea.loc[ea['Year'] == 2009]
ea_nine_sales
tot = int(ea_nine_sales["Name"].count())
total_sales = int(ea_nine_sales["Global_Sales"].sum() * 1000000)
text = f"Interesting to note that EA only has one game in the top 10. Also interesting to see multiple of the same game for different platforms, which can show of the strategy EA can take as opposed to what Nintendo does. But for games realeased in 2009 EA has sold a total of {total_sales} titles"
text
publish = game.filter(items=['Publisher'], axis=1)
ea_total = publish.value_counts()['Electronic Arts']
act_total = publish.value_counts()['Activision']
nbg_total = publish.value_counts()['Namco Bandai Games']
total = int(publish.count());
ea_percent = int(ea_total/total * 100)
act_percent = int(act_total/total * 100)
nbg_percent = int(nbg_total/total * 100)
text = f"The top three publishers Electronic Arts, Activision and Namco Bandai Games take up {ea_percent}%, {act_percent}% and {nbg_percent}% respectively"
text
text = "Next I'd like to take a look at genres and see how well specific genres sell overall"
