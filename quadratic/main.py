import json
import math
from typing import final
from dataclasses import dataclass
import csv 

@dataclass
class Recipient:
    name: str
@dataclass
class TokenGift:
    sender_id: int
    sender_address: str   
    recipient_id: int 
    recipient_address: str 
    tokens: int
    recipient: Recipient

def get_amount_per_user(token_gift: TokenGift):
    return token_gift["recipient_address"], math.sqrt(token_gift["tokens"])

def get_recipient_name(token_gift: TokenGift):
    if(token_gift["recipient"] and token_gift["recipient"]['name']): 
        return token_gift["recipient"]['name']
    return None


def square_amounts(amounts): 
    sqaured_amt = {}
    sum = 0 
    for addr, amt in amounts.items():
        sqaured_amt[addr] = amt * amt 
        sum += amt*amt 
    return sqaured_amt, sum 

def final_ratio(sqaured_amt, sum):
    final_amt = {}
    for addr, amt in sqaured_amt.items():
        final_amt[addr] = [amt, amt / sum]
    return final_amt


def main(): 
    amount = {}
    recipient_address_name_map = {}

    f = open("./files/data.json", 'r')
    data = json.load(f)

    for i in data["data"]["token_gifts"]:
        recipient_address, amt = get_amount_per_user(i)
        if recipient_address in amount: 
            amount[recipient_address] += amt 
        else:
            amount[recipient_address] = amt
        recipient_address_name_map[recipient_address]  = get_recipient_name(i)

    f.close()

    sqaured_amt, sum = square_amounts(amount)
    final_amt = final_ratio(sqaured_amt, sum)

    filename = "./files/output.csv"    
    with open(filename, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["name", "address", "score", "ratio"])
        for addr, vals in final_amt.items(): 
            amt, ratio = vals
            csvwriter.writerow([recipient_address_name_map.get(addr), addr, amt, ratio ])             


