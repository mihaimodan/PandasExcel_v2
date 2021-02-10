import pandas as pd
import numpy as np

#importing the excel content as a DataFrame.
df = pd.read_excel(r"C:\Users\Mihai\Desktop\Programare\udemy\Ardit Sulce\The Python Mega Course - 10 real world applications\Exercises & other\Pandas\DIDuri_Titu.xlsx", sheet_name = 0)
#Getting rid of all the possible "Unnamed" columns in the DataFrame.
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

def lstCommonItems(datframe_input = df):
    lstCommon = []
    lstUncommon = []
    for k, v in df.iteritems():
        for k2, v2 in v.iteritems():
            if v2 not in lstUncommon:
                lstUncommon.append(v2)
            else:
                lstCommon.append(v2)
    return lstCommon
nan = "nan"
nanLst = ['$2006', '$2047', '$205F', '$209B', '$209D', '$20CC', '$20CD', '$20CE', '$20CF', '$20D0', '$20D1', '$20D3', '$2102', '$2103', '$2104', '$2105', '$2108', '$210D', '$210E', '$210F', '$2110', '$2111', '$2112', '$2113', '$2114', '$211D', '$211E', '$2141', '$2142', '$2143', '$2144', '$2145', '$2146', '$2147', '$2148', '$2149', '$214A', '$214B', '$214C', '$214D', '$214E', '$214F', '$2150', '$2151', '$2152', '$2153', '$2154', '$2155', '$2156', '$2157', '$2158', '$2159', '$215A', '$215B', '$215C', '$215D', '$2162', '$2165', '$2168', '$2169', '$216A', '$216B', '$2181', '$2184', '$219B', '$21A1', '$21A2', '$21A3', '$21A4', '$21A5', '$21A6', '$21A7', '$21A8', '$21A9', '$21AA', '$21AB', '$21AC', '$21AD', '$21AE', '$21AF', '$21B0', '$21B1', '$21B2', '$21B3', '$21B4', '$21B5', '$21B6', '$21B7', '$21B8', '$21B9', '$21BA', '$21BB', '$21BC', '$21BD', '$21BE', '$21BF', '$21C1', '$21C2', '$21C3', '$21C4', '$21C6', '$21C7', '$21C8', '$222F', '$2230', '$223F', '$228C', '$228E', '$228F', '$2290', '$2291', '$2292', '$2299', '$22AA', '$2457', '$2458', '$2459', '$245A', '$245B', '$245C', '$245D', '$247A', '$24C9', '$24DD', '$2501', '$2502', '$2503', '$2504', '$2505', '$2536', '$2847', '$2848', '$2849', '$284A', '$2851', '$2852', '$285F', '$2865', '$2866', '$2867', '$288D', 
'$288E', '$291D', '$291E', '$29DF', '$29E1', '$2A31', '$2A44', '$2A45', '$2A46', '$2AF9', '$2B34', '$2B59', '$2B63', '$3114', '$2897', '$2B4F', '$2BDE', '$206E', '$216D', '$247B', '$24C3', '$2862', '$29C3', '$29C4', '$29C5', '$29C6', '$29C7', '$29C8', '$29C9', '$29CA', '$29CB', '$29CC', '$29CD', '$29CE', '$29CF', '$29D0', '$29D1', '$29D2', '$29D3', '$29D4', '$29D5', '$29D6', '$29D7', '$29D8', '$29D9', '$29DA', '$29DB', '$29DC', '$29DD', '$29DE', '$2A26', '$2A27', '$2A28', '$2AB6', '$2AFC', '$2AFD', '$F1A2', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan]
nanLst.remove("nan")
print(len(nanLst))