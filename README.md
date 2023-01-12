# Analysis-of-Forwards-Scatter-Plot
A scatter plot for analysing goalscoring performance of forward players in football/soccer made with Plotly in Python. The data was collected from FBref for the 22-23 PL season (accurate as of 11/01/23). Players included had FW as their primary position tag and a min of 540 mins played at the time of collection. 

![newplot (13)](https://user-images.githubusercontent.com/122451735/212092224-3db58a86-a6b2-469a-bd08-e971b77bcaca.png)

The quadrant analysis looks at shot frequency vs the npxG value of the shots, i.e. how well are forwards getting/generating shooting opportunities and the xG value/quality of them. The colour scale indicates ability to convert by displaying non-penalty goals minus non-penalty expected goals per 90 (np:G-xG / 90). 

For example, Newcastle's Callum Wilson is taking more shots of a higher xG than average and converting them about as you would expect. Haaland is not only taking a lot of high xG shots but is significantly overperforming in his ability to finish them with +0.41 np:G-xG per 90. Nunez is getting a high volume of relatively good xG shooting opportunities but being wasteful with them.

