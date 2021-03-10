import pandas as pd
import plotly.express as px

df = pd.read_csv("/Users/suhanirana/Desktop/python/class 103/Assignment/Copy+of+data+-+data.csv")
fig = px.scatter(df, x="date", y="cases",
	             color="country")
fig.show()
