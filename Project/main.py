import pandas as pd
import streamlit as sl

file = 'vgsales.csv'
#game = pd.read_csv(file)

test = "TEST"

test

df = pd.DataFrame({'first column': [1,2,3,4],
                   'second column': [5,3,7,8]
                   })

sl.line_chart(df)

