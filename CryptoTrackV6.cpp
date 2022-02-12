#include <string>
#include <iomanip>
#include <array>
#include <iostream>
#include <fstream>
#include <cctype>
#include <vector>
#include <ctime>
#include <Python.h>
using namespace std;

struct DayData
{
    string date;
    vector<string> assetNames;
    vector<double> prices;
    vector<double> amounts;
    vector<double> values;
};

/*
checks if the api keys for this api have been set 
NOTE : api keys that exist are cmc,cb,k,g,b,ku
WARNING : call with a vector of the lines in "API.txt"
*/
bool doesKeyExist(string key,vector<string> apiLines)
{
    for(int i=0; i<apiLines.size(); i++)
    {
        if(key==apiLines[i]) return true;
    }
    return false;
}

/*
Sets users api keys, checks if a key is already set, if so, shall it be updated?
WARNING : call with a vector of the lines in "API.txt"
*/
void setAPIKEYS(vector<string> apiLines)
{
    string input;
    ofstream writeKey;
    ofstream writeKraken;
    writeKraken.open("kraken.txt");
    writeKraken.clear();
    writeKey.open("API.txt");
    writeKey.clear();
    writeKey<<"cmc\n";
    cout<<"\nPlease enter your coinmarketcap api key\n";
    getline(cin,input);
    writeKey<<input<<"\n";

    writeKey<<"cb\n";
    cout<<"\nPlease enter your Coinbase api key\n";
    getline(cin,input);
    writeKey<<input<<"\n";
    cout<<"\nPlease enter your Coinbase api secret key\n";
    getline(cin,input);
    writeKey<<input<<"\n";

    writeKey<<"k\n";
    cout<<"\nPlease enter your Kraken api key\n";
    getline(cin,input);
    writeKraken<<input<<"\n";
    writeKey<<input<<"\n";
    cout<<"\nPlease enter your Kraken api secret key\n";
    getline(cin,input);
    writeKraken<<input<<"\n";
    writeKey<<input<<"\n";

    writeKey<<"g\n";
    cout<<"\nPlease enter your Gemini api key\n";
    getline(cin,input);
    writeKey<<input<<"\n";
    cout<<"\nPlease enter your Gemini api secret key\n";
    getline(cin,input);
    writeKey<<input<<"\n";

    writeKey<<"b\n";
    cout<<"\nPlease enter your Binance api key\n";
    getline(cin,input);
    writeKey<<input<<"\n";
    cout<<"\nPlease enter your Binance api secret key\n";
    getline(cin,input);
    writeKey<<input<<"\n";

    writeKey<<"ku\n";
    cout<<"\nPlease enter your Kucoin api key\n";
    getline(cin,input);
    writeKey<<input<<"\n";
    cout<<"\nPlease enter your Kucoin api secret key\n";
    getline(cin,input);
    writeKey<<input<<"\n";
    cout<<"\nPlease enter your Kucoin api secret code\n";
    getline(cin,input);
    writeKey<<input<<"\n";

}

/*
calls a text file and returns a vector of that file's lines
WARNING : if deleteFile is true it will delete file after reading
*/
vector<string> readTextFile(const char *fileName,bool deleteFile)
{
    string line;
    ifstream readTextFile;
    vector<string> lines;
    
    readTextFile.open(fileName);
    while(getline(readTextFile,line))
    {
        //cout<<endl<<line<<endl;
        if(line.substr(line.length()-1,1)=="\r" || line.substr(line.length()-1,1)=="\n") line=line.substr(0,line.length()-1);
        lines.push_back(line);
    }
    readTextFile.close();
    if(deleteFile) remove(fileName);
    return lines;
}
/*
Checks if a name exists within the given name vector
*/
bool doesNameExist(string name,vector<string> names)
{
    for(int i=0; i<names.size(); i++)
    {
        if(names[i]==name) return true;
    }
    return false;
}
/*
returns the index of a given name withing the given name vector, returns -1 if a name is not found
*/
int getNameIndex(string name, vector<string> names)
{
    for(int i=0; i<names.size();i ++)
    {
        if(name==names[i]) return i;
    }
    return -1;
}
/*
retuns the price of a given name from the price data
*/
double getNamePrice(string name,vector<string> priceData)
{
    for(int i=0; i<priceData.size();i++)
    {
        if(priceData[i]==name) return stod(priceData[i+1]);
    }
    return 0;
}
// maintains current asset names in "Names.txt"
//NOTE: NOT IN USE
void UpdateNames(vector<string> names)
{
    bool update=false;
    vector<string> currNames=readTextFile("Names.txt",0);
    vector<int> indexes;
    for(int i=0; i<currNames.size();i++)
    {
        if(names[i]!=currNames[i]) update=true;
        if(update) break;
    }
    ofstream updateNames;
    if(update)
    {
        updateNames.open("Names.txt");
        updateNames.clear();
        for(int i=0; i<names.size();i++)
        {
            updateNames<<names[i]<<endl;
        }
        updateNames.close();
    }
    
}
/*
returns the current system set date in the format MM/DD/YYYY, note that intergers less than 10 will not be led with a zero
*/
string getCurrentDate()
{
    std::time_t t = std::time(0);
    std::tm* now = std::localtime(&t);
    std::string day=std::to_string(now->tm_mday);
    std::string month=std::to_string(now->tm_mon+1);
    std::string year=std::to_string(now->tm_year+1900);
    std::string date=month+'/'+day+'/'+year;
    return date;
}
// 0 for print, 1 for string, any mode not equal to 1 will return empty string
string buildBox(std::string key,bool mode)
{
    string box=""; 
    std::cout<<"\n";
    int length=key.length();
    int numT=length*2+key.length();
    int numSpaces=(numT-length)/2;
    if(mode==0)
    {
        if(length%2!=0)//number must be even, bc we will devide by 2, and it must be a whole number after dividing
        {
            length++;
        }
        for(int i=0; i<numT; i++)
        {
            std::cout<<"=";
        }   
        std::cout<<"\n||";
        for(int i=0; i<numSpaces-2; i++)
        {
            std::cout<<" ";
        }
        std::cout<<key;
        for(int i=0; i<numSpaces-2; i++)
        {
            std::cout<<" ";
        }
        std::cout<<"||\n";
        for(int i=0; i<numT; i++)
        {
            std::cout<<"=";
        }
    }
    else if(mode==1)
    {
        if(length%2!=0)//number must be even, bc we will devide by 2, and it must be a whole number after dividing
        {
            length++;
        }
        for(int i=0; i<numT; i++)
        {
            box+="=";
        }   
        box+="\n||";
        for(int i=0; i<numSpaces-2; i++)
        {
            box+=" ";
        }
        box+=key;
        for(int i=0; i<numSpaces-2; i++)
        {
            box+=" ";
        }
        box+="||\n";
        for(int i=0; i<numT; i++)
        {
            box+="=";
        }
    }
    else
    {
        cout<<"an invalid mode was selected for buildBox()... should be 0 or 1"<<endl;
    }
    return box;
}
// writes the data stored to various .csv files
void writeDataToFile(DayData dayData)
{
//CryptoTrackTotal
bool empty=false;
ifstream isFileEmpty;
ofstream writeFile;

isFileEmpty.open("CryptoTrackTotalValues.csv");
isFileEmpty.seekg(0, ios::end);  
if (isFileEmpty.tellg() == 0) empty=true;
isFileEmpty.close();
writeFile.open("CryptoTrackTotalValues.csv",_S_app);
if(empty) writeFile<<"Date,Total\n";
string date=getCurrentDate();
char sep=',';
writeFile<<date<<sep<<dayData.values[dayData.values.size()-1]<<endl;
writeFile.close();

isFileEmpty.open("CryptoTrackTotal.csv");
isFileEmpty.seekg(0, ios::end);  
if (isFileEmpty.tellg() == 0) empty=true;
isFileEmpty.close();
writeFile.open("CryptoTrackTotal.csv",_S_app);
if(empty) writeFile<<"Date,Total,WeekMean,2WeekMean,MonthMean,3MonthMean,6MonthMean,YearMean,Mean\n";
writeFile<<date<<sep<<dayData.values[dayData.values.size()-1]<<sep;
writeFile.close();
//CryptoTrackData
empty=false;
isFileEmpty.open("CryptoTrackData.csv");
isFileEmpty.seekg(0, ios::end);  
if (isFileEmpty.tellg() == 0) empty=true;
isFileEmpty.close();
writeFile.open("CryptoTrackData.csv",_S_app);
if(empty) writeFile<<"Name,Amount,Price,Value,Date\n";
for(int i=0; i<dayData.assetNames.size()-1;i++)
{
    writeFile<<dayData.assetNames[i]<<sep<<dayData.amounts[i]<<sep<<dayData.prices[i]<<sep<<dayData.values[i]<<sep<<date<<endl;
}
writeFile.close();
}



//adds data stored in various vectors to a single DayData struct varible, returns the new dayData varible
DayData AddDayData(vector<string> AssetNames,vector<double> Prices,vector<double> Amounts,vector<double> Values)
{
    DayData dayData;
    double total=0;
    for(int i=0; i<AssetNames.size();i++)
    {
        total+=Values[i];
    }
    AssetNames.push_back("Total");
    Values.push_back(total);
    Prices.push_back(0);
    Amounts.push_back(0);
    dayData.assetNames=AssetNames;
    dayData.prices=Prices;
    dayData.amounts=Amounts;
    dayData.values=Values;
    return dayData;
}

void getData(vector<string> apiKeysLines,char *fileNameBinance,char *fileNameKraken,char *fileNameGemini,char *fileNameCoinbase,char *fileNamePrices,char *fileNameKucoin)
{
    bool keysSet=false;
    if(!doesKeyExist("cmc",apiKeysLines) && !doesKeyExist("cb",apiKeysLines) && !doesKeyExist("k",apiKeysLines) && !doesKeyExist("g",apiKeysLines) && !doesKeyExist("b",apiKeysLines) && !doesKeyExist("ku",apiKeysLines))
    {
        std::cout<<"\nFirst time user detected, you will be asked to enter your api keys\n";
        setAPIKEYS(apiKeysLines);
        keysSet=true;

    }
    else if(!doesKeyExist("cmc",apiKeysLines) || !doesKeyExist("cb",apiKeysLines) || !doesKeyExist("k",apiKeysLines) || !doesKeyExist("g",apiKeysLines) || !doesKeyExist("b",apiKeysLines)|| !doesKeyExist("ku",apiKeysLines))
    {
        //some key does not exists fix this, if they do not want to ewnter this key, enter "key" or "skey" where key should be
        std::cout<<"\nAPI errors detected, you will be asked to re-enter your api keys\n";
        setAPIKEYS(apiKeysLines);
        keysSet=true;
    }
    else keysSet=true;
    if(keysSet)
    {
        std::cout<<"\nObtaining Current Binance Account Data, This Will Take a Moment\n";                              
        system(fileNameBinance);
        std::cout<<"\nObtaining Current Kraken Account Data, This Will Take a Moment\n";                              
        system(fileNameKraken);
        std::cout<<"\nObtaining Current Gemini Account Data, This Will Take a Moment\n";                              
        system(fileNameGemini);
        std::cout<<"\nObtaining Current Coinbase Account Data, This Will Take a Moment\n";                              
        system(fileNameCoinbase);
        std::cout<<"\nObtaining Current Kucoin Main Account Data, This Will Take a Moment\n";
        system(fileNameKucoin);
        std::cout<<"\nObtaining Current Crypto Prices, This Will Take a Moment\n";                              
        system(fileNamePrices);
    }
}
int main()
{
    string date=getCurrentDate();
    ifstream checkDate;
    vector<string> checkDates=readTextFile("CryptoTrackTotalValues.csv",false);
    bool done=false;
    for(int i=0; i<checkDates.size(); i++)
    {
        if(checkDates[i].substr(0,date.length())==date)
        {
            done=true;
            system("python3 DisplayGraphs.py");
            return 0;
        }
    }
    std::cout<<"\n\nCurrently, CryptoTrack supports the following exchanges. Binance, Kraken, Gemini, Coinbase, and Kucoin.\n"<< 
    "\nAdditionlly CryptoTrack utilizes coinmarketcap to obtain currnet crypto prices\n\nYou will need api keys with your account(s) to use CryptoTrack\n";
    char fileNamePrices[]="python3 -m Prices.py";
    char fileNameCoinbase[]="python.exe \"c:/Code/Tests/CryptoTrack/CryptoV6/CoinbaseAPI.py\"";
    char fileNameKraken[]="python.exe \"c:/Code/Tests/CryptoTrack/CryptoV6/KrakenAPI.py\"";
    char fileNameGemini[]="python.exe \"c:/Code/Tests/CryptoTrack/CryptoV6/GeminiAPI.py\"";
    char fileNameBinance[]="python.exe \"c:/Code/Tests/CryptoTrack/CryptoV6/BinanceAPI.py\"";
    char fileNameCryptoTotal[]="python3 Graphs.py";
    char fileNmaeKucoin[]="python3 KucoinAPI.py";
    char fileAPI[]="API.txt";
    vector<string> apiKeysLines=readTextFile(fileAPI,false);
    getData(apiKeysLines,fileNameBinance,fileNameKraken,fileNameGemini,fileNameCoinbase,fileNamePrices,fileNmaeKucoin);
    vector<string> PriceData=readTextFile("PriceData.txt",1);
    vector<string> CoinbaseData=readTextFile("CoinBaseWallets.txt",1);
    vector<string> BinanceData=readTextFile("BinanceData.txt",1);
    vector<string> GeminiData=readTextFile("GeminiData.txt",1);
    vector<string> KrakenData=readTextFile("KrakenData.txt",1);
    vector<string> KucoinData=readTextFile("KukoinWallets.txt",1);
    PriceData.push_back("USD");
    PriceData.push_back("1.00");
    KrakenData.push_back("BNB");
    KrakenData.push_back("0.409");
    KrakenData.push_back("SAFEMOON");
    KrakenData.push_back("206914586.84");
    vector<double> Prices;
    vector<double> Amounts;
    vector<double> Values;
    vector<string> Names;
    double Price;
    double Value;
    double Amount;
    string name;
    
    for(int i=0; i<CoinbaseData.size(); i++)
    {
        if(isalpha(CoinbaseData[i][0])) name=CoinbaseData[i];
        else if(isdigit(CoinbaseData[i][0]))
        {
            Value=stod(CoinbaseData[i]);
            Price=getNamePrice(name,PriceData);
            Amount=Value/Price;
            if(doesNameExist(name,Names))
            {
                Values[getNameIndex(name,Names)]+=Value;
                Amounts[getNameIndex(name,Names)]+=Amount;
            }
            else
            {
                Names.push_back(name);
                Prices.push_back(Price);
                Values.push_back(Value);
                Amounts.push_back(Amount);
            }
        }  
    }
    for(int i=0; i<KrakenData.size(); i++)
    {
        if(isalpha(KrakenData[i][0])) name=KrakenData[i];
        else if(isdigit(KrakenData[i][0]))
        {
            Amount=stod(KrakenData[i]);
            Price=getNamePrice(name,PriceData);
            Value=Amount*Price;
            if(doesNameExist(name,Names))
            {
                Values[getNameIndex(name,Names)]+=Value;
                Amounts[getNameIndex(name,Names)]+=Amount;
            }
            else
            {
                Names.push_back(name);
                Prices.push_back(Price);
                Values.push_back(Value);
                Amounts.push_back(Amount);
            }
        } 
    }
    for(int i=0; i<GeminiData.size(); i++)
    {
        if(isalpha(GeminiData[i][0])) name=GeminiData[i];
        else if(isdigit(GeminiData[i][0]))
        {
            Amount=stod(GeminiData[i]);
            Price=getNamePrice(name,PriceData);
            Value=Amount*Price;
            if(doesNameExist(name,Names))
            {
                Values[getNameIndex(name,Names)]+=Value;
                Amounts[getNameIndex(name,Names)]+=Amount;
            }
            else
            {
                Names.push_back(name);
                Prices.push_back(Price);
                Values.push_back(Value);
                Amounts.push_back(Amount);
            }
        }
    }
    for(int i=0; i<BinanceData.size(); i++)
    {
        if(isalpha(BinanceData[i][0])) name=BinanceData[i];
        else if(isdigit(BinanceData[i][0]))
        {
            Amount=stod(BinanceData[i]);
            Price=getNamePrice(name,PriceData);
            Value=Amount*Price;
            if(doesNameExist(name,Names))
            {
                Values[getNameIndex(name,Names)]+=Value;
                Amounts[getNameIndex(name,Names)]+=Amount;
            }
            else
            {
                Names.push_back(name);
                Prices.push_back(Price);
                Values.push_back(Value);
                Amounts.push_back(Amount);
            }
        } 
    }
    for(int i=0; i<KucoinData.size(); i++)
    {
        if(isalpha(KucoinData[i][0])) name=KucoinData[i];
        else if(isdigit(KucoinData[i][0]))
        {
            Amount=stod(KucoinData[i]);
            Price=getNamePrice(name,PriceData);
            Value=Amount*Price;
            if(doesNameExist(name,Names))
            {
                Values[getNameIndex(name,Names)]+=Value;
                Amounts[getNameIndex(name,Names)]+=Amount;
            }
            else
            {
                Names.push_back(name);
                Prices.push_back(Price);
                Values.push_back(Value);
                Amounts.push_back(Amount);
            }
        } 
    }
    DayData dayData=AddDayData(Names,Prices,Amounts,Values);
    writeDataToFile(dayData);
    //UpdateNames(dayData.assetNames);
    system(fileNameCryptoTotal);
    return 0;
}