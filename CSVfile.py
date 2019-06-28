import csv
movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("CSV.csv","w") as f:
          w=csv.writer(f,delimiter=",")
          for row in movies:
              w.writerow(row)
