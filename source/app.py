
from pathlib import Path

import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")

# Load your CSV file into a DataFrame
current_dir = Path(__file__).parent
root_dir = current_dir.parent
df = pd.read_csv(root_dir / 'data' / 'daily_journal_oct_2024.csv')
df['Total Work'] = df['GameDev'] + df['Growth'] + df['Finance'] + df['Venture']

st.line_chart(df['Wakeup Time'])
