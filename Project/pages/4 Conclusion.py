"""The Conclusion Page of my Web App

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

sl.markdown("# Conclusion")
sl.sidebar.markdown("# Conclusion")

text = ("Like I briefly mentioned in the Genres section, it is important to use multiple data points when looking to sell and market a game."
        "As I looked through the data it was quite easy to notice patterns, the most obvious being Nintendo, another pattern that was present that I only briefly mentioned is games were sperated by console they were sold on. So theres a solid chance that Wii sports wasn't the number one game and could be knocked off by soemthing like Grand Theft Auto Five which was quite highly ranked on the list twice"
        "Another data point I didn't delve much into was how sales stacked up against each other based on region, Something like Wii sports sold well in NA, EU and Japense markets but that wasn't entirely true for everything. It was also noticeable that Nintendo sold a lot better in Japanese markets as well which I think is worth metnioning"
        "Overall there is a lot of data too be taken away from this especially if your thinking about selling a game or publish through a larger machine Hope I helped you parse through it even if it was just a little bit!")
text