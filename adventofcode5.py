"""
FBFBBFFRLR: row 44, column 5, seat ID 357.
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.

[0:6] = row
[7:9] = column
row * 8 + column = seat ID

F means to take the lower half
B means to take the upper half

R means to take the upper half
L means to take the lower half
"""

def seat(input):
    ticket=input.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
    row=0
    col=0
    for i in range(0, 7):
        row+=pow(2, 6-i)*int(ticket[i])
        # print(row)
    for j in range(7, 10):
        col+=pow(2, 2+7-j)*int(ticket[j])
        # print(col)
    # print(int(row),int(col))
    return(int(row)*8+int(col))

tickets='FBFBBFFRLR','BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL'
for ticket in tickets:
    seat(ticket)
    
try:
    tickets=open("C:\\Users\\mika1\\Downloads\\input (4).txt", "r").readlines()
except IOError:    #This means that the file does not exist (or some other IOError)
    print("File not found")

passengers=[]
for ticket in tickets:
    passengers.append(seat(ticket))

max(passengers)

# Part 2
freeseats=[]
for i in range(max(passengers)):
    if not i in passengers:
        freeseats.append(i)

# max(freeseats)

for seat in freeseats:
    if seat-1 in passengers and seat+1 in passengers:
        print(seat)
