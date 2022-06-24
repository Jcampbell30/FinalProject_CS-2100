from Currency import Currency
def main(): 
 hongKongCurrency = Currency("China","HK$",True,True,7882911.355) 
 hungaryCurrency = Currency("Hungary","Ft",False,False,3719.34) 
 switzerlandCurrency = Currency("Switzerland","fr",True,False,2828128.4) 
 saudiArabiaCurrency = Currency("Saudi Arabia","SAR",False,True,999999) 
 AmericanCurrency = Currency('America','$','left','comma',1)
 ArgentinaCurrency = Currency('Argentina','$','left','decimal',8.405692)
 
 print(hongKongCurrency) 
 print(hungaryCurrency) 
 print(switzerlandCurrency) 
 print(saudiArabiaCurrency) 
 print(AmericanCurrency)
 print(ArgentinaCurrency)
 
main()