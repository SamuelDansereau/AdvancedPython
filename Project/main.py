"""The Landing Page of my Web App

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
import pandas as pd
import streamlit as sl

sl.title('All Time Video Game Sales')

sl.markdown("# Home Page")
sl.sidebar.markdown("# Home Page")

opening = "Below is a chart that shows the sales data of every video game that sold 100,000 copies by the end of 2016!"
opening

file = 'CSV Files/vgsale.csv'
game = pd.read_csv(file)
game

continued = "As you can see this is a lot of data to digest all at once, allow me to break it down for you in some more useful sets!"
continued

pattern = "Just to start here is one of the most obvious patterns you can see in the dataframe"
pattern

top_ten = game[:10]
top_ten

pattern = "This is the top 10 entries in the best selling games of all time, all 10 of them were published by nintendo"
pattern



