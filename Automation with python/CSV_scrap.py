import pandas as pd

football_data = pd.read_csv("https://www.football-data.co.uk/mmz4281/2324/E0.csv")


football_data.rename(columns={'PCAHA' : "home_goals"}, inplace = True)

print(football_data)