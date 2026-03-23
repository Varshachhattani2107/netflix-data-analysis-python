import csv

total_titles = 0
movies = 0
tv_shows = 0
years = []

with open("netflix_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_titles += 1

        if row["Type"] == "Movie":
            movies += 1
        elif row["Type"] == "TV Show":
            tv_shows += 1

        years.append(int(row["Release_Year"]))

# Oldest & Latest
oldest = min(years)
latest = max(years)

print("Total Titles:", total_titles)
print("Movies:", movies)
print("TV Shows:", tv_shows)
print("Oldest Release Year:", oldest)
print("Latest Release Year:", latest)
