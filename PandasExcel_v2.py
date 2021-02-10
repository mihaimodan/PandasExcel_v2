import pandas as pd

#importing the excel content as a DataFrame.
df = pd.read_excel(r"C:\Users\Mihai\Desktop\Programare\udemy\Ardit Sulce\The Python Mega Course - 10 real world applications\Exercises & other\Pandas\ItemsToCompare.xlsx", sheet_name = 0)
#Getting rid of all the possible "Unnamed" columns in the DataFrame.
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

#Iterating through the DataFrame and splitting the items into 2 lists:
#lstCommon - for duplicates/ lstUncommon - for the rest.
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

#Getting rid of the nan's from the resulted list.
def delNan(lst = lstCommonItems):
    cleanedList = [x for x in lst() if str(x) != 'nan'] #return me X if string of x is not "nan" from lst()
    return cleanedList

#Converting the function to a data frame and assign it a column name.
#Export to excel.
df2 = pd.DataFrame(delNan(), columns = ["Common Items"])
df2.to_excel(r"C:\Users\Mihai\Desktop\Programare\udemy\Ardit Sulce\The Python Mega Course - 10 real world applications\Exercises & other\Pandas\Output_v2.xlsx", columns = ["Common Items"])


