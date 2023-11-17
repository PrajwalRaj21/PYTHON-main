#scraps data from html or website

import pandas as pd

top_gear = pd.read_html("https://en.wikipedia.org/wiki/List_of_Top_Gear_(2002_TV_series)_episodes")

print(len(top_gear))

print(top_gear[1])  #extracts the second season data