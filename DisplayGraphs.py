import pandas as pd
from pandas.io.parsers import read_csv
import plotly.express as px
import datetime as dt

def Graphs():
    dfWhole=pd.read_csv("CryptoTrackData.csv")
    dfMeans=read_csv('CryptoTrackTotal.csv')
    dfBTC=dfWhole.loc[dfWhole["Name"]=="BTC"]
    dfETH=dfWhole.loc[dfWhole["Name"]=="ETH"]
    dfVET=dfWhole.loc[dfWhole["Name"]=="VET"]
    dfDOT=dfWhole.loc[dfWhole["Name"]=="DOT"]
    dfSAFEMOON=dfWhole.loc[dfWhole["Name"]=="SAFEMOON"]
    dfADA=dfWhole.loc[dfWhole["Name"]=="ADA"]
    dfONE=dfWhole.loc[dfWhole["Name"]=="ONE"]
    dfMATIC=dfWhole.loc[dfWhole["Name"]=="MATIC"]
    dfEOS=dfWhole.loc[dfWhole["Name"]=="EOS"]
    dfSTORJ=dfWhole.loc[dfWhole["Name"]=="STORJ"]
    dfLINK=dfWhole.loc[dfWhole["Name"]=="LINK"]
    dfXTZ=dfWhole.loc[dfWhole["Name"]=="XTZ"]
    dfSHIB=dfWhole.loc[dfWhole["Name"]=="SHIB"]
    dfBAT=dfWhole.loc[dfWhole["Name"]=="BAT"]
    dfCHZ=dfWhole.loc[dfWhole["Name"]=="CHZ"]
    dfBNB=dfWhole.loc[dfWhole["Name"]=="BNB"]
    dfUNI=dfWhole.loc[dfWhole["Name"]=="UNI"]
    dfDOGE=dfWhole.loc[dfWhole["Name"]=="DOGE"]
    dfEQX=dfWhole.loc[dfWhole["Name"]=="EQX"]
    dfAAVE=dfWhole.loc[dfWhole["Name"]=="AAVE"]
    dfLUNA=dfWhole.loc[dfWhole["Name"]=="LUNA"]
    dfZIL=dfWhole.loc[dfWhole["Name"]=="ZIL"]
    dfAMP=dfWhole.loc[dfWhole["Name"]=="AMP"]
    dfSNX=dfWhole.loc[dfWhole["Name"]=="SNX"]
    dfKNC=dfWhole.loc[dfWhole["Name"]=="KNC"]
    dfBAL=dfWhole.loc[dfWhole["Name"]=="BAL"]
    dfMTV=dfWhole.loc[dfWhole["Name"]=="MTV"]
    
    figVal=px.line(dfMeans,x='Date',y=[dfBTC["Value"],dfETH["Value"],dfVET["Value"],dfDOT["Value"],dfADA["Value"],dfSTORJ["Value"],dfLINK["Value"],dfXTZ["Value"],dfBAT["Value"],dfBNB["Value"],dfDOGE["Value"],dfAAVE["Value"],dfZIL["Value"],dfAMP["Value"],dfSNX["Value"],dfEOS["Value"],dfSAFEMOON["Value"],dfONE["Value"],dfMATIC["Value"],dfCHZ["Value"],dfLUNA["Value"],dfSHIB["Value"],dfMTV["Value"]],title='Breakdown of Asset Diversity')
    #FOR V7 WRITE THE NAMES AND 0 VALUE and AMOUNT FOR CRYPTO NOT YET OWNED!!!!!!!!!!
    newnames = {'wide_variable_0':'BTC', 'wide_variable_1':'ETH', 'wide_variable_2':'VET', 'wide_variable_3':'DOT', 'wide_variable_4':'ADA', 'wide_variable_5':'STORJ', 'wide_variable_6':'LINK', 'wide_variable_7':'XTZ', 'wide_variable_8':'BAT', 'wide_variable_9':'BNB', 'wide_variable_10':'DOGE', 'wide_variable_11':'AAVE', 'wide_variable_12':'ZIL', 'wide_variable_13':'AMP', 'wide_variable_14':'SNX', 'wide_variable_15':'EOS', 'wide_variable_16':'SAFEMOON', 'wide_variable_17':'ONE', 'wide_variable_18':'MATIC', 'wide_variable_19':'CHZ', 'wide_variable_20':'LUNA', 'wide_variable_21':'SHIB', 'wide_variable_22':'MTV'}
    figVal.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )
    
    figVal.show()
    
    fig=px.line(dfMeans,x='Date',y=['WeekMean','2WeekMean','MonthMean','Total','Mean',dfBTC["Price"]*.3],title="Your Crypto Portfolio Over Time")
    fig.show()
    

    current_time = dt.datetime.now() 
    month=current_time.month
    day=current_time.day
    year=current_time.year
    date=str(month)+"/"+str(day)+'/'+str(year)
    dfData=pd.read_csv('CryptoTrackData.csv')
    dfDay=dfData.loc[dfData["Date"]==date]
    
    
    
    figPie=px.pie(dfDay,values='Value',names="Name",title='Breakdown of Asset Diversity')
    figPie.show()

Graphs()