from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import pandas as pd
import os
os.system("cls")
data=pd.read_excel("flights_2019.xlsx")

#filter
filter=(data["destination"] == "France")
data_filtered=data[filter]
numCountryX=data_filtered["destination"].sum()

#Gemiddelde berekenen van passengers
averagePassengers=data["passengers"].mean()

#Het top 5 berekenen van het aantal passengers
data_sorted=data.sort_values("passengers",ascending=False)
top5=data_sorted.head(5)
# Draaitabel op datum
data["departed"]=pd.to_datetime(data["departed"])
data["departed"]=data["departed"].dt.strftime("%Y-%m")
data_pivoted=data.pivot_table(
    index="departed",
    columns="airline",
    values="passengers",
    aggfunc=sum
    )

#Om terug te gaan of te beeindigen
def choice():
    print("---------------------------------")
    answerleave = input("klik enter om verder te gaan anders type X om te stoppen\nVoer in: ")
    if answerleave == "X" or answerleave == "x":
        exit()
    else:
        os.system("cls")
#Gemiddelde berekenen van passengers
isRunning = True
while(isRunning):
    print("Welkom bij Smart City Airport")
    print("1)Toon gemiddelde aantal passagiers")
    print("2)Toon de top 5 van vluchten met meeste passagiers")
    print("3)Toon aantalvluchten naar Frankrijk")
    print("4)Toon draaitabel van maanden versus airlines, met som vanpassagiers")

    answer = int(input("Kies 1 t/m 4 anders X om te stoppen: "))
    
    print(answer)
    if answer == 1:
        print("gemiddelde aantal passagiers")
        print(averagePassengers)
        choice()
    elif answer == 2:
        print("Toon de top 5 van vluchten met meeste passagiers")
        print(top5)
        choice()
    elif answer == 3:
        print("Toon aantalvluchten naar Frankrijk")
        print(f"Aantalvluchtenuit'Frankrijk': {numCountryX} Vluchten")    
        choice()

    elif answer == 4:
        print(data_pivoted)
        data_pivoted.plot(kind="barh", stacked=True)
        plt.show()
        choice()

    elif answer == "X" or  answer == "x":
        exit()
#einde