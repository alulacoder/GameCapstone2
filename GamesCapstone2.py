import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly
from plotly.subplots import make_subplots
import pandas as pd
import re

data = pd.read_csv("games.csv")

data = data[["Rating", "Plays", "Wishlist", "Playing", "Title"]]

for i in data:
    data[["Plays","Playing","Wishlist"]] = re.sub("^0-10000000000000000", " ", i)



import datetime as dt

def convertTime(t):
    t = int(t)
    return dt.datetime.fromtimestamp(t)

data["Plays"] = data["Plays"]*1000
data["Wishlist"] = data["Wishlist"]*1000
data["Playing"] = data["Playing"]*1000

top10_plays = pd.DataFrame(data.groupby("Title")["Plays"].sum().nlargest(10).sort_values(ascending=False))
top10_rating = pd.DataFrame(data.groupby("Title")["Rating"].sum().nlargest(10).sort_values(ascending=False))
top10_Wishlist = pd.DataFrame(data.groupby("Title")["Wishlist"].sum().nlargest(10).sort_values(ascending=False))
top10_Playing = pd.DataFrame(data.groupby("Title")["Playing"].sum().nlargest(10).sort_values(ascending=False))

fig1 = px.scatter(top10_plays, x = top10_plays.index, y = "Plays", size = "Plays", size_max= 120, color = top10_plays.index, title = "Top 10 Games by Rating")
fig1.write_html("first_figure.html", auto_open = True)
