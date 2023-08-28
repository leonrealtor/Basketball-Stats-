import pandas as pd 

#the main idea here is to have 0 in the msising places as to not mess up the data ad 
#make sure that the data has complete entreis and has some places where they should not be
team_rebounding_data = pd.read_csv("team_rebounding_data_22.csv")
awards_data = pd.read_csv("awards_data.csv")
team_stats = pd.read_csv("team_stats.csv")
player_stats = pd.read_csv("player_stats.csv")

## i want to round the teamreboudingdata to the 4th degit afte the first 4 
team_rebounding_data['oreb_pct'] = team_rebounding_data['oreb_pct'].round(4)


if 'Unnamed: 0' in team_stats.columns:
    team_stats.drop(columns=['Unnamed: 0'], inplace=True)

if 'Unnamed: 0' in player_stats.columns:
    player_stats.drop(columns=['Unnamed: 0'], inplace=True)
if 'Unnamed: 0.1.1' in awards_data.columns:
    awards_data.drop(columns=['Unnamed: 0.1.1'], inplace=True)

if 'Unnamed: 0' in team_rebounding_data.columns:
    team_rebounding_data.drop(columns=['Unnamed: 0'], inplace=True)




team_stats.fillna(0, inplace=True)
team_rebounding_data.fillna(0, inplace=True)
awards_data.fillna(0, inplace=True)
player_stats.fillna(0, inplace=True)

# Convert 'all_star_game' and 'rookie_all_star_game' columns to numeric values
awards_data['all_star_game'] = awards_data['all_star_game'].replace({'True': 1, 'False': 0}).astype(int)
awards_data['rookie_all_star_game'] = awards_data['rookie_all_star_game'].replace({'True': 1, 'False': 0}).astype(int)


# Save the cleaned data back to the same CSV or a new one
team_rebounding_data.to_csv("team_rebounding_data_22.csv", index=False)
awards_data.to_csv('awards_data.csv',index = False)
team_stats.to_csv("team_stats.csv", index = False)
player_stats.to_csv('player_stats.csv', index= False)