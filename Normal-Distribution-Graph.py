import pandas as pd 
import plotly.figure_factory as ff 

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Avg_Rating"].tolist()], ["Avg_rating"])
fig.show()