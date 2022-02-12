import pandas as pd
from pandas.io.parsers import read_csv
import plotly.express as px
import datetime as dt

#IF YOU SEE ERRORS ABOVE...DISREGARD THEM...THE IMPORTS ARE WORKING JUST FINE 
# YOU MUST RUN WITH PYTHON3 COMMAND, THE IMPORTS ARE IN A DIFFERENT SPOT THAN THE IMPORTS USED FOR OG 5 APIS

current_time = dt.datetime.now() 
month=current_time.month
day=current_time.day
year=current_time.year
date=str(month)+"/"+str(day)+'/'+str(year)

current_time = dt.datetime.now() - dt.timedelta(days=6)
month=current_time.month
day=current_time.day
year=current_time.year
weekDate=str(month)+"/"+str(day)+'/'+str(year)

current_time = dt.datetime.now() - dt.timedelta(days=13)
month=current_time.month
day=current_time.day
year=current_time.year
twoweekDate=str(month)+"/"+str(day)+'/'+str(year)

current_time = dt.datetime.now() - dt.timedelta(days=29)
month=current_time.month
day=current_time.day
year=current_time.year
monthDate=str(month)+"/"+str(day)+'/'+str(year)

current_time = dt.datetime.now() - dt.timedelta(days=89) 
month=current_time.month
day=current_time.day
year=current_time.year
threeMonthDate=str(month)+"/"+str(day)+'/'+str(year)

current_time = dt.datetime.now() - dt.timedelta(days=179) 
month=current_time.month
day=current_time.day
year=current_time.year
sixMonthDate=str(month)+"/"+str(day)+'/'+str(year)

current_time = dt.datetime.now() - dt.timedelta(days=364) 
month=current_time.month
day=current_time.day
year=current_time.year
yeardate=str(month)+"/"+str(day)+'/'+str(year)

dfTotal = pd.read_csv('CryptoTrackTotalValues.csv')
dfWhole=pd.read_csv("CryptoTrackData.csv")
dfTotal["Date"]=pd.to_datetime(dfTotal["Date"])

#dfBTC=dfWhole.loc(dfWhole["Name"]=="BTC")


numDays=len(dfTotal)

mean=dfTotal["Total"].mean()

writeMeans=open("CryptoTrackTotal.csv","a")

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

dfMeans=pd.read_csv('CryptoTrackTotal.csv')
figVal=px.line(dfMeans,x='Date',y=[dfBTC["Value"],dfETH["Value"],dfVET["Value"],dfDOT["Value"],dfADA["Value"],dfSTORJ["Value"],dfLINK["Value"],dfXTZ["Value"],dfBAT["Value"],dfBNB["Value"],dfDOGE["Value"],dfAAVE["Value"],dfZIL["Value"],dfAMP["Value"],dfSNX["Value"],dfEOS["Value"],dfSAFEMOON["Value"],dfONE["Value"],dfMATIC["Value"],dfCHZ["Value"],dfLUNA["Value"],dfSHIB["Value"],dfMTV["Value"]],title='Breakdown of Asset Diversity')
#FOR V7 WRITE THE NAMES AND 0 VALUE and AMOUNT FOR CRYPTO NOT YET OWNED!!!!!!!!!!
newnames = {'wide_variable_0':'BTC', 'wide_variable_1':'ETH', 'wide_variable_2':'VET', 'wide_variable_3':'DOT', 'wide_variable_4':'ADA', 'wide_variable_5':'STORJ', 'wide_variable_6':'LINK', 'wide_variable_7':'XTZ', 'wide_variable_8':'BAT', 'wide_variable_9':'BNB', 'wide_variable_10':'DOGE', 'wide_variable_11':'AAVE', 'wide_variable_12':'ZIL', 'wide_variable_13':'AMP', 'wide_variable_14':'SNX', 'wide_variable_15':'EOS', 'wide_variable_16':'SAFEMOON', 'wide_variable_17':'ONE', 'wide_variable_18':'MATIC', 'wide_variable_19':'CHZ', 'wide_variable_20':'LUNA', 'wide_variable_21':'SHIB', 'wide_variable_22':'MTV'}
figVal.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                    legendgroup = newnames[t.name],
                                    hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                    )
                )

figVal.show()



if(numDays>364):
    dfTotalWeek=dfTotal[dfTotal["Date"].isin(pd.date_range(weekDate,date))]
    WeekMean=dfTotalWeek["Total"].mean()
    writeMeans.write(str(WeekMean))
    writeMeans.write(',')
    
    dfTotal2Week=dfTotal[dfTotal["Date"].isin(pd.date_range(twoweekDate,date))]
    twoWeekMean=dfTotal2Week["Total"].mean()
    writeMeans.write(str(twoWeekMean))
    writeMeans.write(',')
    
    dfTotalMonth=dfTotal[dfTotal["Date"].isin(pd.date_range(monthDate,date))]
    monthMean=dfTotalMonth["Total"].mean()
    writeMeans.write(str(monthMean))
    writeMeans.write(',')
    
    dfTotal3Month=dfTotal[dfTotal["Date"].isin(pd.date_range(threeMonthDate,date))]
    threeMonthMean=dfTotal3Month["Total"].mean()
    writeMeans.write(str(threeMonthMean))
    writeMeans.write(',')

    dfTotal6Month=dfTotal[dfTotal["Date"].isin(pd.date_range(sixMonthDate,date))]
    sixMonthMean=dfTotal6Month["Total"].mean()
    writeMeans.write(str(sixMonthMean))
    writeMeans.write(',')

    dfTotalYear=dfTotal[dfTotal["Date"].isin(pd.date_range(yeardate,date))]
    yearMean=dfTotalYear["Total"].mean()
    writeMeans.write(str(yearMean))
    writeMeans.write(',')
    
    
    writeMeans.write(str(mean))
    
    writeMeans.write("\n")
    writeMeans.close()
    dfMeans=pd.read_csv('CryptoTrackTotal.csv')
    
    fig=px.line(dfMeans,x='Date',y=['WeekMean','2WeekMean',"MonthMean","3MonthMean","6MonthMean","YearMean",'Total','Mean',dfBTC["Price"]*.3],title="Your Crypto Portfolio Over Time")
    fig.show()
elif(numDays>179):
    dfTotalWeek=dfTotal[dfTotal["Date"].isin(pd.date_range(weekDate,date))]
    WeekMean=dfTotalWeek["Total"].mean()
    writeMeans.write(str(WeekMean))
    writeMeans.write(',')
    
    dfTotal2Week=dfTotal[dfTotal["Date"].isin(pd.date_range(twoweekDate,date))]
    twoWeekMean=dfTotal2Week["Total"].mean()
    writeMeans.write(str(twoWeekMean))
    writeMeans.write(',')
    
    dfTotalMonth=dfTotal[dfTotal["Date"].isin(pd.date_range(monthDate,date))]
    monthMean=dfTotalMonth["Total"].mean()
    writeMeans.write(str(monthMean))
    writeMeans.write(',')
    
    dfTotal3Month=dfTotal[dfTotal["Date"].isin(pd.date_range(threeMonthDate,date))]
    threeMonthMean=dfTotal3Month["Total"].mean()
    writeMeans.write(str(threeMonthMean))
    writeMeans.write(',')

    dfTotal6Month=dfTotal[dfTotal["Date"].isin(pd.date_range(sixMonthDate,date))]
    sixMonthMean=dfTotal6Month["Total"].mean()
    writeMeans.write(str(sixMonthMean))
    writeMeans.write(',')
    
    for i in range(1,3):
        writeMeans.write(str(mean))
        if(i<2):
            writeMeans.write(",")
    
    writeMeans.write("\n")
    writeMeans.close()
    dfMeans=pd.read_csv('CryptoTrackTotal.csv')
    
    fig=px.line(dfMeans,x='Date',y=['WeekMean','2WeekMean',"MonthMean","3MonthMean","6MonthMean",'Total','Mean',dfBTC["Price"]*.3],title="Your Crypto Portfolio Over Time")
    fig.show()
elif(numDays>89):
    dfTotalWeek=dfTotal[dfTotal["Date"].isin(pd.date_range(weekDate,date))]
    WeekMean=dfTotalWeek["Total"].mean()
    writeMeans.write(str(WeekMean))
    writeMeans.write(',')
    
    dfTotal2Week=dfTotal[dfTotal["Date"].isin(pd.date_range(twoweekDate,date))]
    twoWeekMean=dfTotal2Week["Total"].mean()
    writeMeans.write(str(twoWeekMean))
    writeMeans.write(',')
    
    dfTotalMonth=dfTotal[dfTotal["Date"].isin(pd.date_range(monthDate,date))]
    monthMean=dfTotalMonth["Total"].mean()
    writeMeans.write(str(monthMean))
    writeMeans.write(',')
    
    dfTotal3Month=dfTotal[dfTotal["Date"].isin(pd.date_range(threeMonthDate,date))]
    threeMonthMean=dfTotal3Month["Total"].mean()
    writeMeans.write(str(threeMonthMean))
    writeMeans.write(',')
    
    for i in range(1,4):
        writeMeans.write(str(mean))
        if(i<3):
            writeMeans.write(",")
    
    writeMeans.write("\n")
    writeMeans.close()
    dfMeans=pd.read_csv('CryptoTrackTotal.csv')
    
    fig=px.line(dfMeans,x='Date',y=['WeekMean','2WeekMean',"MonthMean","3MonthMean",'Total','Mean',dfBTC["Price"]*.3],title="Your Crypto Portfolio Over Time")
    fig.show()
elif(numDays>30):
    dfTotalWeek=dfTotal[dfTotal["Date"].isin(pd.date_range(weekDate,date))]
    WeekMean=dfTotalWeek["Total"].mean()
    writeMeans.write(str(WeekMean))
    writeMeans.write(',')
    
    dfTotal2Week=dfTotal[dfTotal["Date"].isin(pd.date_range(twoweekDate,date))]
    twoWeekMean=dfTotal2Week["Total"].mean()
    writeMeans.write(str(twoWeekMean))
    writeMeans.write(',')
    
    dfTotalMonth=dfTotal[dfTotal["Date"].isin(pd.date_range(monthDate,date))]
    monthMean=dfTotalMonth["Total"].mean()
    writeMeans.write(str(monthMean))
    writeMeans.write(',')
    
    for i in range(1,5):
        writeMeans.write(str(mean))
        if(i<4):
            writeMeans.write(",")
    
    writeMeans.write("\n")
    writeMeans.close()
    dfMeans=pd.read_csv('CryptoTrackTotal.csv')
    
    fig=px.line(dfMeans,x='Date',y=['WeekMean','2WeekMean',"MonthMean",'Total','Mean',dfBTC["Price"]*.3],title="Your Crypto Portfolio Over Time")
    fig.show()
elif(numDays>13):
    dfTotalWeek=dfTotal[dfTotal["Date"].isin(pd.date_range(weekDate,date))]
    WeekMean=dfTotalWeek["Total"].mean()
    writeMeans.write(str(WeekMean))
    writeMeans.write(',')
    
    dfTotal2Week=dfTotal[dfTotal["Date"].isin(pd.date_range(twoweekDate,date))]
    twoWeekMean=dfTotal2Week["Total"].mean()
    writeMeans.write(str(twoWeekMean))
    writeMeans.write(',')
    
    for i in range(1,6):
        writeMeans.write(str(mean))
        if(i<5):
            writeMeans.write(",")
    
    writeMeans.write("\n")
    writeMeans.close()
    dfMeans=pd.read_csv('CryptoTrackTotal.csv')
    
    fig=px.line(dfMeans,x='Date',y=['WeekMean','2WeekMean','Total','Mean',dfBTC["Price"]*.3],title="Your Crypto Portfolio Over Time")
    fig.show()
elif(numDays>6):
    dfTotalWeek=dfTotal[dfTotal["Date"].isin(pd.date_range(weekDate,date))]
    WeekMean=dfTotalWeek["Total"].mean()
    writeMeans.write(str(WeekMean))
    writeMeans.write(',')
    
    for i in range(1,7):
        writeMeans.write(str(mean))
        if(i<5):
            writeMeans.write(",")
    
    writeMeans.write("\n")
    writeMeans.close()
    dfMeans=pd.read_csv('CryptoTrackTotal.csv')
    
    fig=px.line(dfMeans,x='Date',y=['WeekMean','Total','Mean',dfBTC["Price"]*.3],title="Your Crypto Portfolio Over Time")
    fig.show()
else:
    for i in range(1,8):
        writeMeans.write(str(mean))
        if(i<7):
            writeMeans.write(",")
    
    fig=px.line(dfTotal,x='Date',y=['Mean',dfBTC["Price"]*.3],title="Your Crypto Portfolio Over Time")
    fig.show()

dfData=pd.read_csv('CryptoTrackData.csv')
dfDay=dfData.loc[dfData["Date"]==date]
figPie=px.pie(dfDay,values='Value',names="Name",title='Breakdown of Asset Diversity')
figPie.show()


