import sqlite3 as sql
import matplotlib.pyplot as plt

db = sql.connect("pTable.db")

#SQL query, giver navn, densitet og smelte punkt for element som er sorteret efter densitet
select = db.execute("""SELECT NAME, DENSITY, MELT FROM periodiskSystem ORDER BY DENSITY""")

#Får svar til et array
select  = select.fetchall()

#Opretter arrays/lister for Punkterne og navne tilhørende
xNames = []
xDensity = []
yMelt = []

#Fylder array/listerne op med de værdi de skal have
for element in select:
    xNames.append(element[0])
    xDensity.append(element[1])
    yMelt.append(element[2])

#Opretter et plot
fig, ax = plt.subplots()

#Navngiver x og y akserne
plt.xlabel('Density  g/cm3')
plt.ylabel('Melt  Kelvin')

#Indsætter punkterne fra listerne til plot
plt.scatter(xDensity, yMelt)

#Giver navn for de punkter der er plottet
for i in range(len(xNames)):
    if xDensity[i] != None and yMelt[i] != None:
        ax.annotate(xNames[i],(xDensity[i],yMelt[i]))

#Starter plot window for visualisering
plt.show()