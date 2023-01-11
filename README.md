# Analysis-of-Forwards-Scatter-Plot
A scatter plot for analysing the performance of forward players in football/soccer made using the Plotly graphing library in Python 3.0. The data was collected from FBref for the 22-23 Premier League season and is accurate as of 11/01/2023. All players included had FW as their primary positional tag and a minimum of six 90s played (540 mins). 

![newplot (11)](https://user-images.githubusercontent.com/122451735/211830487-aad94fc3-d387-46a9-922b-c99654cbd373.png)

The quadrant analysis looks at the shot frequency and npxG value of the shots being achieved by Premier League forwards, i.e., how well are they generating shooting opportunities for themselves, and the quality of those opportunities based on xG value. The colour scale indicates how well they have been converting their chances by displaying the their non-penalty goals minus non-penalty expected goals per 90 rate. 

For example, Newcastle's Callum Wilson is taking more shots of a higher xG than average and converting them about as you would expect. Haaland is not only taking a lot of high xG shots but is significantly overperforming in his ability to finish them with +0.41 np:G-xG per 90. Whereas Nunez is getting a high volume of relatively good xG shooting opportunities but being wasteful with them. Bournemouth's Kieffer Moore is taking above average xG shots and being clinical with them but is failing to generate shooting chances at a high enough frequency. Mitrovic and Antony are getting a healthy amount of shots away and converting them fairly effectively but could improve by taking shots from higher xG areas of the pitch. 

