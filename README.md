# Analysis-of-Forwards-Scatter-Plot
A scatter plot for analysing the performance of forward players in football/soccer made using the Plotly graphing library in Python 3.0. The data was collected from FBref for 22-23 Premier League season and is accurate as of 11/01/2023. Players with <300 mins were and that did not have FW as their primary position were removed. 

The quadrant analysis looks at the shot frequency and xG value of the shots being achieved by Premier League forwards, i.e. how well are the getting/generating shooting opportunities for themselves and the quality of those opportunities. The colour scale indicates how well they have been converting their chances (non-penalty goals minus non-penalty expected goals). 



For example, Newcastle's Callum Wilson is taking more shots of a higher xG than average and converting about as you would expect. Haaland is not only taking a lot of high xG shots but is significantly overperforming in his ability to finish them. Whereas Bamford and Nunez are getting good xG shooting opportunities but being wasteful with them. 

![newplot (8)](https://user-images.githubusercontent.com/122451735/211809764-64e87c92-3dcb-4c7a-8a8f-e7837f9db23e.png)
