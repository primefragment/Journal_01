import dash
from dash import dcc, html
import dash.dependencies as dd
import pandas as pd
import plotly.express as px
from pathlib import Path

# Load your CSV file into a DataFrame
current_dir = Path(__file__).parent
root_dir = current_dir.parent
df = pd.read_csv(root_dir / 'data' / 'daily_journal.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

fig1=px.line(df, x='Date', y='6am Club', title='6am Club')
fig2=px.line(df, x='Date', y='Plan the Day', title='Plan the Day')
fig3=px.line(df, x='Date', y='Work per Plan', title='Work per Plan')
fig4=px.line(df, x='Date', y='In Control', title='In Control')

# Create your layout
app.layout = html.Div([
    dcc.Graph(
        id='graph1',
        figure=fig1
    ),
    dcc.Graph(
        id='graph2',
        figure=fig2
    ),
    dcc.Graph(
        id='graph3',
        figure=fig3
    ),
    dcc.Graph(
        id='graph4',
        figure=fig4
    )

])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

