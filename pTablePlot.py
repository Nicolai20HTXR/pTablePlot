import sqlite3 as sql
import matplotlib.pyplot as plt

db = sql.connect("pTable.db")

#Opretter funktion til hvad der skal plottes fra x og y aksen som sorteret fra xAksen
def addFig(xAxis,yAxis):
    #SQL query, giver navn, densitet og smelte punkt for element som er sorteret efter densitet
    qString = f"""SELECT name, {xAxis}, {yAxis} FROM periodiskSystem ORDER BY {xAxis}"""
    select = db.execute(qString)

    #Får svar til et array
    select  = select.fetchall()

    #Opretter arrays/lister for Punkterne og navne tilhørende
    xNames = []
    xArr = []
    yArr = []

    #Fylder array/listerne op med de værdi de skal have
    for element in select:
        xNames.append(element[0])
        xArr.append(element[1])
        yArr.append(element[2])

    #Opretter et plot
    fig, ax = plt.subplots()

    #Navngiver x og y akserne
    plt.xlabel(f'{xAxis}')
    plt.ylabel(f'{yAxis}')

    #Indsætter punkterne fra listerne til plot
    plt.scatter(xArr, yArr)

    #Giver navn for de punkter der er plottet
    for i in range(len(xNames)):
        if xArr[i] != None and yArr[i] != None:
            ax.annotate(xNames[i],(xArr[i],yArr[i]))

#Tilføjer flere forskellige måder at plote
addFig("Density","Melt")
addFig("Density","Boil")
addFig("Atomic_mass","Boil")
addFig("Boil","Melt")
addFig("Atomic_mass","Melt")


#Starter plot window for visualisering
plt.show()