import pandas as pd
from pandas import DataFrame

#Citirea fisierului excel.
df1 = pd.read_excel(r"C:\Users\Mihai\Desktop\Programare\udemy\Ardit Sulce\The Python Mega Course - 10 real world applications\Exercises & other\Pandas\DIDuri_Titu.xlsx", sheet_name = 0, header = None)
#Stergerea coloanei goale dintre cele 2 coloane DID. Folosirea inplace = True pentru a nu crea alt DataFrame.
df1.drop(df1.columns[1:2], 1, inplace = True)
#Stergerea coloanelor dupa cea de a 2a coloana DID.
df2 =  df1.drop(df1.columns[2:], 1)

#Alocarea si despartirea DataFrame-ului in 2 variabile separate.
#did1 cuprinde toate randurile si coloana pana la index 1.
#did2 cuprinde toate randurile si coloana de la index 2.
did1 = df2.iloc[:, :1]
did2 = df2.iloc[:, 1:2]


#Stergerea primului rand(index 0) pentru did1 si did2, deoarece este de forma: 0     DID
did1 = did1.drop(did1.index[0:1], 0)
did2 = did2.drop(did2.index[0:1], 0)

#Redenumirea primei coloane pentru cele 2 DataFrame-uri.
did1.columns = ["DID-uri 1"]
did2.columns = ["DID-uri 2"]

#Convertirea DataFrame-urilor in liste.
lst_did1 = did1["DID-uri 1"].to_list()
lst_did2 = did2["DID-uri 2"].to_list()

#Crearea unei liste goale pentru adaugarea itemilor comuni dintre cele 2 liste.
lst_DIDuri_comune = []

#Nested for loop pentru iteratia prin cele 2 liste. Adaugarea itemilor comuni in lista goala lst_DIDuri_comune.
for item1 in lst_did1:
    for item2 in lst_did2:
        if item1 == item2:
            lst_DIDuri_comune.append(item1)

#Convertirea in 3 serii a listelor precedente pentru a le folosi drept coloane mai tarziu.        
df_did1 = pd.Series(lst_did1)
df_did2 = pd.Series(lst_did2)
df_didComune = pd.Series(lst_DIDuri_comune)

#Concatenarea seriilor intr-un DataFrame si atribuirea de nume coloanelor.
df = pd.DataFrame({'DID-uri DTemp': df_did1, 'DID-uri DFull': df_did2, 'DID-uri Comune': df_didComune})

#Exportarea intr-un fisier excel.
df.to_excel(r"C:\Users\Mihai\Desktop\Programare\udemy\Ardit Sulce\The Python Mega Course - 10 real world applications\Exercises & other\Pandas\DIDuri_Titu - Copy.xlsx")
