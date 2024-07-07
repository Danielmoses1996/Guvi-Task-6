import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Initialize Dash application
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("H1N1 Vaccine Uptake Dashboard"),
    
    dcc.Dropdown(
        id='dropdown-age-bracket',
        options=[{'label': age, 'value': age} for age in df['age_bracket'].unique()],
        value=df['age_bracket'].unique()[0],
        placeholder="Select Age Bracket"
    ),
    
    dcc.Graph(id='bar-chart'),
    dcc.Graph(id='pie-chart'),
    dcc.Graph(id='scatter-plot'),
])

# Define callback to update graphs based on dropdown selection
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure'),
     Output('scatter-plot', 'figure')],
    [Input('dropdown-age-bracket', 'value')]
)
def update_graphs(selected_age_bracket):
    filtered_data = df[df['age_bracket'] == selected_age_bracket]
    
    # charts
    bar_fig = px.bar(filtered_data, x='qualification', y='h1n1_vaccine', color='sex', barmode='group', 
                     labels={'qualification': 'Education Level', 'h1n1_vaccine': 'Vaccine Uptake'})
    
    pie_fig = px.pie(filtered_data, values='h1n1_vaccine', names='race', title='Vaccine Uptake by Race')
    
    scatter_fig = px.scatter(filtered_data, x='h1n1_worry', y='h1n1_awareness', color='sex',
                             size='h1n1_vaccine', hover_data=['income_level'],
                             labels={'h1n1_worry': 'Worry about H1N1', 'h1n1_awareness': 'Awareness of H1N1'})
    
    return bar_fig, pie_fig, scatter_fig

if __name__ == '__main__':
    app.run_server(debug=True)
