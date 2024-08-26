renaming_dict = {
    'Player':"Name", 'Mat':"Matches", 'Inns':"Innings", 'NO':"Not Outs", 'HS':"Highest Score", 
    'Ave':"Average", '100':'Centuries', '50':"Fifties",'0':"Ducks",
    'Wkts':"Wickets", 'BBI':"Best Innings Figures", 'BBM':"Best Match Figrure",
    'Econ':"Economy", 'SR':"Strike Rate", '5':"Five Wicket Hauls", '10':"Ten Wickest Hauls",
    'Dis':'Dismissals', 'Ct':"Catches", 'St':"Stumpings", 'Ct Wk':"Caught Behinds", 'Ct Fi':"Caught in Outfield",
'MD':"Most Diss in a match", 'D/I':"Dismissal Per Innigs", "Mdns":"Maidens"
}

data_types = {
    'Player':"str",'Mat':"int", 'Inns':"int", 'NO':"int", 'HS':"int", 
    'Ave':"float64", '100':'int', '50':"int",'0':"int",
    'Wkts':"float64", 'BBI':"str", 'BBM':"str", "Balls":"int","4":"int", "6":"int",
    'Econ':"float", 'SR':"float", '5':"int", '10':"int","BF":"str","4s":"int", "6s":"int",
   'Dis':'int', 'Ct':"int", 'St':"int", 'Ct Wk':"int", 'Ct Fi':"int","Overs":"int","Mdns":"int",
'MD':"int", 'D/I':"str", "Runs":"int", "Country":"str", "Debut Year":"int", "Last Match Year":"int"
}

columns_to_show = ['Name', "Innings"]

def strip(string:str)-> str:

    #removing brackets from the string
    string = string[:-1]
    #separting ICC from the strip:
    if "/" in string:
        string = string.split("/")[-1]
        
    return string