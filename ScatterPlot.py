# import packages

import pandas as pd
import plotly.express as px

# load csv as dataframe

df = pd.read_csv(r'example\replace_with_csv_location.csv')

# preview data has loaded correctly

df.head()

# convert columns into lists

shot_90 = list(df.Sh90)
npxg_shot = list(df.npxGSh)
player = list(df.Player)
overperformance = list(df.npGxG)

# calcualte averages for quadrant lines


shot_90_avg = sum(shot_90) / len(shot_90)
npxg_shot_avg = sum(npxg_shot) / len(npxg_shot)

# create the scatter plot

fig = px.scatter(x=shot_90, y=npxg_shot, text=player, color=overperformance,
                   color_continuous_scale=px.colors.sequential.Jet, title="Premier League Forwards 22-23: shots per 90 vs npxG per shot")

# update how player names display

fig.update_traces(textposition='bottom right')

# customise graph

fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', font_family="Arial", plot_bgcolor="black", 
                  autosize=False, width=1000, height=750, coloraxis_colorbar=dict(title="np:G-xG"),
                  paper_bgcolor="black", font = dict(color='white'), xaxis=dict(title_text="Shots per 90", titlefont=dict(size=20)), 
                  yaxis=dict(title_text="npxG per Shot", titlefont=dict(size=20)))

# add quadrant lines 

fig.add_hline(y=npxg_shot_avg, opacity=.5, line_color="#39FF14")
fig.add_vline(x=shot_90_avg, opacity=.5, line_color="#39FF14")

# alter colour of grid lines

fig.layout.xaxis.gridcolor="#3B3B3B"
fig.layout.yaxis.gridcolor="#3B3B3B"

# display chart

fig.show()
