# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 08:29:55 2017

@author: hn7569
"""

import pandas as pd
from tkinter import *
from tkinter import filedialog
import xlsxwriter
import time

#Frequency
def freq_table(num_add1,df):
    tempdf=df[[num_add1]]
    tempdf['Count']=1
    temp_col_list=list(tempdf)
    tempdf.columns=['col1','Count']
    df_output=tempdf.groupby('col1',as_index=False).sum() 
    df_output.columns=[temp_col_list]
    df_output['Percent of Total']=(df_output['Count']/df_output['Count'].sum())
    return df_output

#Function needed to figure out length
def length_add(tempdf):
    return len(tempdf['col1'])

#Qualitative Stat Table

def qual_table(df,num_add1):
    tempdf=df[[num_add1]]
    tempdf['Stat']='Unique Values'
    tempdf.columns=['col1','Stat']
    p1=tempdf.groupby('Stat').col1.nunique()
    p1=pd.DataFrame(data=p1,index=None)
    p1=p1.reset_index(drop=False)
    #Duplicates
    p2=p1
    p2['Duplicates']=p2['col1']<len(df)
    p2=p2.drop(['Stat','col1'],axis=1)
    p2['Stat']='Duplicates'
    p2.columns=['col1','Stat']
    p2=p2[['Stat','col1']]
    #Add Length
    p3=df[[num_add1]]
    tempdf=p3
    tempdf.columns=['col1']
    tempdf['col1']=tempdf.apply(length_add,axis=1)
    p3=df[[num_add1]]
    p3=pd.concat([p3,tempdf],axis=1)
    #Shortest Length
    p4=p3
    p4['Stat']='Shortest Length'
    p4=p4.groupby('Stat',as_index=False).min()
    p4.columns=['Stat','col2','col1']
    p4=p4.drop('col2',axis=1)
    #Shortest Value
    p5 = p4.merge(p3, left_on='col1', right_on='col1', how='inner')
    p5=p5[:1]
    p5.columns=['col1','col2','col3','col4']
    p5=p5.drop(['col1','col2','col4'],axis=1)
    p5['Stat']='Shortest Value'
    p5.columns=['col1','Stat']
    p5=p5[['Stat','col1']]
    #Longest Length
    p6=p3
    p6['Stat']='Longest Length'
    p6=p6.groupby('Stat',as_index=False).max()
    p6.columns=['Stat','col2','col1']
    p6=p6.drop('col2',axis=1)
    #Longest Value
    p7 = p6.merge(p3, left_on='col1', right_on='col1', how='inner')
    p7=p7[:1]
    p7.columns=['col1','col2','col3','col4']
    p7=p7.drop(['col1','col2','col4'],axis=1)
    p7['Stat']='Longest Value'
    p7.columns=['col1','Stat']
    p7=p7[['Stat','col1']]
    #Combine Tables
    frames= [p1,p2,p4,p5,p6,p7]
    stat_table=pd.concat(frames)
    stat_table.columns=['col1','Qualitative Stat','Value']
    stat_table=stat_table.drop('col1',axis=1)
    return stat_table

#Stats Table
def quant_table(df,num_add1):
    #Sum
    s1=df[[num_add1]]
    s1['Stat']='Sum of Values'
    s1.columns=['col1','Stat']
    s1=s1.groupby('Stat',as_index=False).sum()
    s1
    #Min
    s2=df[[num_add1]]
    s2['Stat']='Min'
    s2.columns=['col1','Stat']
    s2=s2.groupby('Stat',as_index=False).min()
    #Max
    s3=df[[num_add1]]
    s3['Stat']='Max'
    s3.columns=['col1','Stat']
    s3=s3.groupby('Stat',as_index=False).max()
    #Mean
    s4=df[[num_add1]]
    s4['Stat']='Mean'
    s4.columns=['col1','Stat']
    s4=s4.groupby('Stat',as_index=False).mean()
    #median
    s5=df[[num_add1]]
    s5['Stat']='Median'
    s5.columns=['col1','Stat']
    s5=s5.groupby('Stat',as_index=False).median()
    #Combine Quant stats
    frames= [s1,s2,s3,s4,s5]
    s_table=pd.concat(frames)
    s_table.columns=['Stat','Value']
    return s_table

print("Greetings! This is a basic data profiler. ")

input("\nPress ENTER when ready to select input file.")

window=Tk()
window.filename = filedialog.askopenfilename(filetypes= (("CSV Files", "*.csv"),("All Files","*.*")))
filename=window.filename
window.destroy()
print( filename )

type=filename[-4:]

if type == ".xls":
    while True:
        try:
            sn=input("\nWhat sheet in the file?")
            basicDF = pd.read_excel(filename,sheetname=sn)
            break
        except:
            print("\nThat was not a valid sheet name. Try again.")
elif type == "xlsx":
    while True:
        try:
            sn=input("\nWhat sheet in the file?")
            basicDF = pd.read_excel(filename,sheetname=sn)
            break
        except:
            print("\nThat was not a valid sheet name. Try again.")
else:
    basicDF = pd.read_csv(filename)

# Select Files
origColList = list(basicDF)

print("\nColumns: ", origColList)

print("\nYou will now be asked for columns in which to check for duplicates")

dpColList=[]

while True:
    while True:
        fieldName = input("\nPlease enter column name (enter d if done): ")
        
        if fieldName == 'd' or fieldName in origColList: break
        
        print("Invalid column name")
         
    if fieldName == 'd': break
    dpColList.append(fieldName)

#Output
timestr = time.strftime("%Y%m%d")
doc_date=time.strftime("%B %d, %Y")

filename = ("/Data_Profile " + timestr + ".xlsx")

input("\nPress ENTER to indicate where you want the file to be exported.")

window=Tk()
window.filepath = filedialog.askdirectory()
filepath=window.filepath
window.destroy()

print("\nPlease wait while I prepare the file.")

#Set up book
writer = pd.ExcelWriter(filepath + filename, engine='xlsxwriter')

#Set up for tables
df=basicDF[dpColList]
num_of_col=len(dpColList)
num_add1=0

# Put together Excel book
while num_add1 < num_of_col :
    df_output=freq_table(num_add1,df)
    if len(df_output)<5000:
        df_output.to_excel(writer,sheet_name=str(dpColList[num_add1]),index=False,startrow=3)
    try:
        q_table=qual_table(df,num_add1)
        q_table.to_excel(writer,sheet_name=str(dpColList[num_add1]),index=False,startrow=3, startcol=4)
    except:
       s_table=quant_table(df,num_add1)
       s_table.to_excel(writer,sheet_name=str(dpColList[num_add1]),index=False,startrow=3, startcol=4)     
    num_add1=num_add1+1

print("Please wait while I prepare this file...")

writer.save()

input("Finished. Press ENTER.")




