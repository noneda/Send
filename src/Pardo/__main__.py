import numpy as np

# * Activity 1
Users : dict[tuple[str , int]]

Users = {
    "1" : ("Kathryn Oliver", 14 ),  # * 1
    "2" :("Sue Roy", 22 ),   # * 2
    "3" :("Celia Wilkins", 32 ),   # * 3
    "4" :("Jackson Gregory", 4 ),   # * 4
    "5" :("Derek Marshall", 55 ),   # * 5
    "6" :("Scott Jennings", 34 ),   # * 6
    "7" :("Sam Dawson", 22 ),   # * 7
    "8" :("Nancy Crawford", 45 ),   # * 8
    "9" :("Brent Walsh", 72 ),   # * 9
    "10" :("Alice Hall", 31 ),  # * 10
    "11" :("Shawn Curry", 22 ),  # * 11
    "12" :("Estelle Ross", 19 ),  # * 12
    "13" :("Jorge Hampton", 78 ),  # * 13
    "14" :("Alfred Crawford", 56 ),  # * 14
    "15" :("Chase Allison", 40 )   # * 15  
}

MoreThan30 = lambda: [user[0] for user in Users.values() if user[1] >= 30]
MinusAge = lambda: [user[0] for user in Users.values() if user[1] <= 18]
OtherByAge = lambda: [user[0] for user in Users.values() if user[1] <= 18 or user[1] >= 40]

#TODO print(MoreThan30())
#TODO print(MinusAge())
#TODO print(OtherByAge())

# * Activity 2
NumberRandom = lambda: [np.random.random_integers(1, 100) for i in range(1, 20)]   

NumpyArray =  np.array(NumberRandom())

#TODO print(NumpyArray)
#TODO print(np.mean(NumpyArray))
#TODO print(np.amin(NumpyArray))
#TODO print(np.amax(NumpyArray))

PowerArray = np.power(NumpyArray, 2)

#TODO print(PowerArray)

# * Activity 3


Cities = {
    "Zofehjer" : (64, 251 ),  # * 1
    "Pazdozu" :(173, 61 ),   # * 2
    "Fafwavuw" :(143, 233 ),   # * 3
    "Aliniupu" :(9, 22),   # * 4
    "Kaktarbe" :(246, 207 ),   # * 5
    "Buhteme" :(231, 138 ),   # * 6
    "Zeponi" :(1, 153 ),   # * 7
    "Diwboka" :(113, 98 ),   # * 8
    "Kodehjam" :(169, 168 ),   # * 9
    "Otafanec" :(3, 109 ),  # * 11
    "Onuvorza" :(134, 147 ),  # * 10
    "Kawijap" :(113, 244 ),  # * 12
    "Rofbepaz" :(129, 181 ),  # * 13
    "Padlamce" :(79, 246 ),  # * 14
    "Puaskam" :(148, 68 )   # * 15  
}

ShowCity = lambda: [city for city in Cities]
QuestionToUser = lambda search: Cities[str(search)] if str(search) in Cities else "Not Found!"


print(ShowCity())
print(QuestionToUser(input("Select a Country: \n")))
