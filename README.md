# Analysis-of-Forwards-Scatter-Plot
A scatter plot for analysing the performance of forward players in football/soccer made using the Plotly graphing library in Python 3.0. The data was collected from FBref for 22-23 Premier League season and is accurate as of 11/01/2023. All players included had FW as their primary position and players with <300 mins playtime were removed. 

![newplot (11)](https://user-images.githubusercontent.com/122451735/211830487-aad94fc3-d387-46a9-922b-c99654cbd373.png)

The quadrant analysis looks at the shot frequency and xG value of the shots being achieved by Premier League forwards, i.e., how well are they generating shooting opportunities for themselves, and the quality of those opportunities based on xG. The colour scale indicates how well they have been converting their chances by displaying the player’s non-penalty goals minus non-penalty expected goals per 90 rate. 

For example, Newcastle's Callum Wilson is taking more shots of a higher xG than average and converting them about as you would expect. Haaland is not only taking a lot of high xG shots but is significantly overperforming in his ability to finish them with +0.41 np:G-xG per 90. Whereas Bamford and Nunez are getting plenty of good xG shooting opportunities but are being wasteful with them. Bournemouth's Kieffer Moore is taking above average xG shots and being clinical with them but is failing to generate shooting chances at a high enough frequency. Mitrovic is getting a healthy amount of shots away and converting them effectively but could improve by taking his shots from higher xG areas of the pitch. Almiron, Foden, and Kane are all performing well and are inside the top right quadrant in red.

