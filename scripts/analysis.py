import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('/path/to/US Airline Flight Routes and Fares 1993-2024.csv')

# Group data for market analysis
passenger_trends = df.groupby('Year').agg(total_passengers=('passengers', 'sum')).reset_index()

# Passenger trends chart
fig_passenger = px.line(passenger_trends, x='Year', y='total_passengers', title='Passenger Trends Over Time')
fig_passenger.write_html("passenger_trends.html")  # Save as HTML

# Airline competitor analysis: Total passengers by airline
airline_passenger_trends = df.groupby(['Year', 'carrier_lg']).agg(
    total_passengers=('passengers', 'sum')
).reset_index()

top_airlines = airline_passenger_trends.groupby('carrier_lg')['total_passengers'].sum().nlargest(10).index
top_airlines_summary = airline_passenger_trends[airline_passenger_trends['carrier_lg'].isin(top_airlines)]

fig_airlines = px.line(top_airlines_summary, x='Year', y='total_passengers', color='carrier_lg', title='Passenger Trends by Airline')
fig_airlines.write_html("airline_passenger_trends.html")  # Save as HTML

# Price optimization example (simplified linear regression plot)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Prepare data for linear regression model
X = df[['nsmiles', 'passengers', 'large_ms', 'lf_ms']].fillna(0)  # Handle missing values
y = df['fare']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LinearRegression().fit(X_train, y_train)

y_pred = model.predict(X_test)
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

# Plot predicted vs actual fares
fig_fares = px.scatter(results, x='Actual', y='Predicted', title='Predicted vs Actual Fares')
fig_fares.write_html("price_optimization.html")  # Save as HTML
