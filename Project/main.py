import pandas as pd
import streamlit as sl

sl.title('All Time Video Game Sales')

sl.markdown("# Home Page")
sl.sidebar.markdown("# Home Page")

file = 'CSV Files/vgsales.csv'
game = pd.read_csv(file)
game

#test = "TEST"

#test

#df = pd.DataFrame({'first column': [1,2,3,4],
 #                  'second column': [5,3,7,8]
  #                 })

#sl.line_chart(df)



