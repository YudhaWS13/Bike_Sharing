import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Load datasets
Day = pd.read_csv('https://raw.githubusercontent.com/YudhaWS13/Bike_Sharing/refs/heads/main/data/day.csv')
Hour = pd.read_csv('https://raw.githubusercontent.com/YudhaWS13/Bike_Sharing/refs/heads/main/data/hour.csv')

# Convert 'dteday' to datetime format for better handling of dates
Day['dteday'] = pd.to_datetime(Day['dteday'])
Hour['dteday'] = pd.to_datetime(Hour['dteday'])

# Calculate average rental per day
average_rental_per_day = Day['cnt'].mean()

# Calculate hourly rentals
hourly_rental = Hour.groupby('hr')['cnt'].sum().reset_index()

# Plot hourly rentals
hourly_fig = px.line(hourly_rental, x='hr', y='cnt', title="Penyewaan Sepeda per Jam")

# Create Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Dashboard Penyewaan Sepeda'),
    
    # Display average rentals per day
    html.Div(children=[
        html.H2(f"Rata-rata Penyewaan Sepeda per Hari: {average_rental_per_day:.2f}")
    ]),
    
    # Graph for hourly rentals
    html.Div(children=[
        dcc.Graph(
            id='hourly-rental-graph',
            figure=hourly_fig
        )
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
