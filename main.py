import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
best_movies_webpage = response.text

soup = BeautifulSoup(best_movies_webpage, "html.parser")

movie_tags = soup.select(selector="tbody.lister-list tr")
movies = []
years = []
ratings = []

with open("IMDb Top 250 movies.txt", "w") as f:
    f.write("Sr.No  " + "Movie".ljust(70) + "\t" + "Year".ljust(8) + "\t" + "IMDb Rating" + "\n")
    for sr, tag in enumerate(movie_tags):
        movie = tag.select_one(selector="td.titleColumn a").text
        year = tag.select_one(selector="td.titleColumn span").text
        rating = tag.select_one(selector="td strong").text
        f.write(str(sr + 1).ljust(7) + movie.ljust(70) + "\t" + year.ljust(8) + "\t" + rating + "\n")
        movies.append(movie)
        years.append(year)
        ratings.append(rating)

d = {"Movie": movies, "Year": years, "IMDb Rating": ratings}
df = pd.DataFrame(data=d)
df.index += 1

df.to_csv("IMDb Top 250 movies.csv")
