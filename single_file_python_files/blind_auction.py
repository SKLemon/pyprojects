#Created as a part of the BAIL repository on Github. Created 12/02/2024

# A secret auction set in the terminal

from art import logo_secret_auction

def bid_comparison (bid_dictionary):
    highest_bid = 0
    highest_bidder = ""
    for each_bidder in bid_dictionary:
        if bid_dictionary[each_bidder] > highest_bid:
            highest_bid = bid_dictionary[each_bidder]
            highest_bidder = each_bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")

print(logo_secret_auction)
bids = {}

while True:
    user_name = (input("What is your name?:\n"))
    bid = int(input("What is your bid?: \n$"))
    bids[user_name] = bid

    user_repeat = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    print("\n" * 30) #Simulated clear
    if user_repeat != "yes":
        bid_comparison(bids)
        break
