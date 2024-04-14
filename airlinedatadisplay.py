import datetime

def columnOutput(dbData,cols,formatStr):
# dbData is a list of tuples
# cols is a dictionary with column name as the key and data type as the item
# formatStr uses the following format, with one set of curly braces {} for each column.
# For each column "{: <10}" determines the width of the column, padded with spaces (10 spaces in this example)
#   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
#   The following example is for 3 columns of output: left-aligned, 5 characters wide; centred, 10 characters; right-aligned 15 characters:
#       formatStr = "{: <5}  {: ^10}  {: >15}"
# You can also pad with something other than a space and put characters between the columns, 
# e.g. this pads with full stops '.' and separates the columns with the pipe character | :
#       formatStr = "{:.<5} | {:.^10} | {:.>15}"
    print(formatStr.format(*cols))
    for row in dbData:
        rowList=list(row)
        for index,item in enumerate(rowList):
            if item==None:      # Removes any None values from the rowList, which would cause the print(*rowList) to fail
                rowList[index]=""       # Replaces them with an empty string
            elif type(item)==datetime.date or type(item)==datetime.datetime or type(item)==datetime.time or type(item)==datetime.timedelta:    # If item is a date, date-time, time or timedelta, convert to a string to avoid formatting issues
                rowList[index]=str(item)
        print(formatStr.format(*rowList))

colPassengers = {"PassengerID":int,"FirstName":str,"LastName":str,"EmailAddress":str,"PhoneNumber":str,"PassportNumber":str,"DateOfBirth":str,"LoyaltyTier":int}

dbPassengers = [(1654,"Jonty","Jensen","Jonty_Jensen@gmail.com","(04) 120-8776","SKW4330434","1986-04-26",1),
(1655,"Kate","McArthur","K_McArthur94@gmail.com","(028) 195-3665","AXI1222486","1993-11-29",1),
(1656,"Jack","Hopere","Jack643@gmail.com","(022) 497-2003","QIN8880246","1956-12-10",1),
(1657,"Chloe","Mathewson","Chloe572@gmail.com","(023) 662-1370","PFI3398028","1947-01-16",1),
(1658,"Kate","McLeod","KMcLeod112@gmail.com","(027) 557-8364","CUB3732904","1991-04-12",1),
(1659,"Sam","Dawson","SamDawson@gmail.com","(07) 172-1045","ZVS873898","1938-05-03",1),
(1660,"Heidi","Delaney","HDelaney@gmail.com","(028) 294-2819","SGP2753266","2014-12-27",1),
(1661,"Michael","Wright","Michael_Wright@gmail.com","(03) 751-2653","MAV3792881","2018-12-26",1),
(1662,"Elizabeth","Preston","ElizabethPreston@gmail.com","(09) 425-5377","UXH6220582","1959-10-14",1),
(1663,"Angus","Chambers","Angus.Chambers@gmail.com","(08) 526-6654","LJS7610310","2019-05-06",1),
(1664,"Shannon","Brown","ShannonBrown@gmail.com","(029) 272-8865","OWC1908420","1936-11-16",1),
(1665,"Eve","Miller","Eve.Miller@gmail.com","(027) 697-1535","ABC8570388","1965-08-19",1),
(1666,"Oliver","Cartwright","O_Cartwright42@gmail.com","(028) 116-8325","LPV189043","1971-05-28",1),
(1667,"Jodie","Sparrow","Jodie382@gmail.com","(024) 748-5128","HDK413015","1974-11-16",1),
(1668,"George","Church","George_Church@gmail.com","(09) 207-6646","JGM5342219","1968-06-25",1),
(1669,"Hone","Atkins","Hone974@gmail.com","(028) 153-3607","ZBB292746","1960-03-10",1),
(1670,"William","Laidlaw","WLaidlaw87@gmail.com","(029) 408-4514","LDP3874015","1944-12-24",1),
(1671,"Dillon","Burt","DillonBurt@gmail.com","(025) 515-9120","MZW5846149","1954-12-05",2),
(1672,"Charlotte","Gallagher","Charlotte721@gmail.com","(020) 463-9870","MBR6068618","1992-06-12",2),
(1673,"Jock","Morgan","Jock164@gmail.com","(029) 865-9089","BSF6336508","1987-09-13",1),
(1674,"Luke","Francis","Luke.Francis@gmail.com","(03) 848-7649","CQF3427300","1997-06-04",1),
(1675,"William","Sanders","William_Sanders@gmail.com","(03) 796-9108","XLF7717445","1993-01-09",1),
(1676,"Harry","Taylor","HarryTaylor@gmail.com","(07) 149-1551","SUP501391","1958-07-09",1),
(1677,"Jordan","Ding","JDing@mail.com","(029) 956-4459","FEQ1416271","2000-02-17",1),
(1678,"Scott","Hogan","S_Hogan@mail.com","(026) 980-4834","WSK2132121","1962-08-02",1),
(1679,"Sarah","Rowe","Sarah364@mail.com","(023) 158-5804","SFT3783709","1958-07-04",3),
(1680,"Charlie","Wilson","Charlie502@mail.com","(027) 301-9148","RCK2446665","1984-02-24",1),
(1681,"Hamish","Knowles","HKnowles81@mail.com","(023) 638-4113","RIC4976153","2021-07-20",1),
(1682,"Jess","Cullen","J.Cullen95@mail.com","(025) 173-8697","UTN6643450","1962-07-06",1),
(1683,"Tipene","Black","T_Black51@mail.com","(029) 515-4770","GKG2633601","1973-12-21",1),
(1684,"Alex","Smith","ASmith63@mail.com","(024) 773-3130","FRH5995435","1958-11-18",1),
(1685,"Holly","Douglas","HollyDouglas@mail.com","(06) 623-3330","KSM311271","2008-10-18",3),
(1686,"Liam","Leonard","LLeonard11@mail.com","(022) 716-9526","GOX5217123","2014-02-21",1)]


## Use the columnOutputfunction to display the dbPassengers information
## Experiment with the alignment of each column and how wide each one needs to be
## This is an example of how to call the function as a reminder, remember you will need to change the variable names
## columnOutput(dbTeams,colTeams,"| {: ^6} | {: ^20} | {: ^9} |") #example of how to call columnOutput function