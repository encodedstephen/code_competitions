import re

seats = []
with open('./input.txt') as input:
    seats = input.read().splitlines()


def convert_to_seat_ids(seats):

    def to_seat_id(seat:str): 
        row = int(seat[0:7].replace('F', '0').replace('B','1'), 2)
        col = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
        return row * 8 + col
    
    seat_ids = [ to_seat_id(x) for x in seats] 

    return sorted(seat_ids)

def find_missing(sorted_seats):

    prev = sorted_seats[0]
    for seat in sorted_seats[1:]:
        if seat != prev + 1:
            return seat - 1
        prev = seat
    
    return None
    
sorted_seats = convert_to_seat_ids(seats)
print(sorted_seats[-1])

missing_seat = find_missing(sorted_seats)
print(missing_seat)
