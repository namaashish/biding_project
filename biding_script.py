dictionary = {
    "ashish" : "ashish is a good boy",
    "friends" : ["vyna", "shiva" , "vyshnavi"]

}

print(dictionary["friends"][1])

nested_list = ["A","B",["C","D"]]

print(nested_list[2][1])

dictionary = {
    "bio_data" : {
        "ashish" : [10 , 20 , 30 , 40] ,
        "about"  : "ashish is a good boy",

    },

    "bio_data2" :{
        "ashish" : [10 , 20 , 30 , 40] ,
        "about"  : "ashish is a good boy",
        
    } 
}

print(dictionary["bio_data"]["ashish"][3])


#project using dictionaries for highest bid value 
bids = {}

continue_bidng = True

def find_highest_bider(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f'the winner is {winner} with a bid of ${highest_bid}')





while continue_bidng:
    Name_of_bid = input("what's your name ?")
    bid_value = int(input("how much you want to bid ?"))
    bids[Name_of_bid] = bid_value
    should_continue = input("Are ther any other bidders ? type 'yes' or 'no' . \n")
    if should_continue == "no":
        continue_bidng = False
        find_highest_bider(bids)
    elif should_continue == "yes":
        print ("\n" *20)
            


number =int( input('enter a number :'))

if number %2 == 0 :
    print('its not a prime number')
else:
    print('its a prime number')

def prime_number(input):
    if input%input == 0 or input%1 == 0 :
        print("its a prime number ")
    
    else:
        input%2 == 0
        print('its not a prime number')

prime_number(number)