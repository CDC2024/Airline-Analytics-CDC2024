// Passenger Trends Chart
var passengerTrends = {
    x: [1993, 1994, 1995, 1996, 1997], // Add your data here
    y: [500000, 520000, 540000, 530000, 550000], // Example passenger data
    type: 'scatter',
    mode: 'lines+markers',
    name: 'Total Passengers',
    line: {shape: 'linear', color: 'blue'}
};

var passengerLayout = {
    title: 'Total Passengers Over Time',
    xaxis: {title: 'Year'},
    yaxis: {title: 'Total Passengers'}
};

Plotly.newPlot('passenger-trends', [passengerTrends], passengerLayout);

// Fare Trends Chart
var fareTrends = {
    x: [1993, 1994, 1995, 1996, 1997], // Add your data here
    y: [100, 105, 110, 108, 112], // Example fare data
    type: 'scatter',
    mode: 'lines+markers',
    name: 'Average Fare',
    line: {shape: 'linear', color: 'green'}
};

var fareLayout = {
    title: 'Average Fare Over Time',
    xaxis: {title: 'Year'},
    yaxis: {title: 'Average Fare ($)'}
};

Plotly.newPlot('fare-trends', [fareTrends], fareLayout);
