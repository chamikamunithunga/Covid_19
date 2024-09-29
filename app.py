from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load data
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
covid_data = pd.read_csv(url)

@app.route('/')
def index():
    # Example of processing data and creating a plot
    covid_data_grouped = covid_data.groupby('Country/Region').sum().iloc[:, 4:]
    plt.figure(figsize=(10, 6))
    plt.plot(covid_data_grouped.T)
    plt.title('COVID-19 Confirmed Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.legend(covid_data_grouped.index, loc='upper left', fontsize='small')
    
    # Save the plot to a PNG image and encode it in base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close()  # Close the figure

    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
