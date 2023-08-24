import pandas as pd 

#the main idea here is to have 0 in the msising places as to not mess up the data ad 
#make sure that the data has complete entreis and has some places where they should not be
team_rebounding_data = pd.read_csv("team_rebounding_data_22.csv")
awards_data = pd.read_csv("awards_data.csv")
team_stats = pd.read_csv("team_stats.csv")
player_stats = pd.read_csv("player_stats.csv")


team_stats.fillna(0, inplace=True)
team_rebounding_data.fillna(0, inplace=True)
awards_data.fillna(0, inplace=True)
player_stats.fillna(0, inplace=True)

# Save the cleaned data back to the same CSV or a new one
team_rebounding_data.to_csv("team_rebounding_data_22.csv", index=False)
awards_data.to_csv('awards_data.csv')
team_stats.to_csv("team_stats.csv")
player_stats.to_csv('player_stats.csv')