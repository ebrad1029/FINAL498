import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import plotly.io as pio


def main():
	df = pd.read_csv("StateFarm.csv", names=['Date', 'Sentiment_Score', 'Text'])

	df['Dates'] = pd.to_datetime(df['Date']).dt.date
	df = df.groupby(df['Dates']).mean()

	fig = px.line(df, x = df.index, y = 'Sentiment_Score', title = "TWITTER SENTIMENT ANALYSIS FOR STATE FARM’S CRITICAL EVENTS")
	fig.update_xaxes(title_text="Dates (2013-2020)")
	fig.update_yaxes(title_text="Average Sentiment Scores (per day)")

	fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([
		dict(count = 1, label = "1 month", step = "month", stepmode="backward"),
		dict(count = 6, label = "6 months", step = "month", stepmode="backward"),
		dict(count = 1, label = "YTD", step = "year", stepmode = "todate"),
		dict(count = 1, label = "1 year", step = "year", stepmode = "backward"),
		dict(count = 5, label = "5 years", step = "year", stepmode = "backward"),
		dict(step = "all")
		])
	),
	rangeslider = dict(visible = True),
	type = "date"))
	fig.show()


	pio.write_html(fig, file="results.html", auto_open=True)


if __name__ == '__main__':
	main()
