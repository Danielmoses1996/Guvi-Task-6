import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Initialize Dash application
app = dash.Dash(__name__)

# Dropdown options for countries
country_options = [{'label': country, 'value': country} for country in zomato_df['Country'].unique()]

# Define app layout
app.layout = html.Div([
    html.H1("Zomato Dashboard"),
    
    dcc.Dropdown(
        id='country-dropdown',
        options=country_options,
        value='India',
        clearable=False,
        style={'width': '50%'}
    ),
    
    dcc.Graph(id='chart1'),
    dcc.Graph(id='chart2'),
])

# Callback to update charts based on dropdown selection
@app.callback(
    [Output('chart1', 'figure'),
     Output('chart2', 'figure')],
    [Input('country-dropdown', 'value')]
)
def update_charts(selected_country):
    filtered_data = zomato_df[zomato_df['Country'] == selected_country]
    
    chart1 = px.bar(filtered_data, x='Cuisines', y='Cost_INR', title='Cost of Cuisines in INR')
    chart2 = px.pie(filtered_data, names='City', title='Distribution of Ratings by City')
    
    return chart1, chart2

if __name__ == '__main__':
    app.run_server(debug=True)
