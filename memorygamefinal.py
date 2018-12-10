# solution:
#   @ßĐ€
#   §Đ$Ł
#   &@ß§
#   €$&Ł

import time

emptycard = " "
card1 = "@"
card2 = "ß"
card3 = "Đ"
card4 = "€"
card5 = "§"
card6 = "$"
card7 = "Ł"
card8 = "&"
card11 = "@"
card22 = "ß"
card33 = "Đ"
card44 = "€"
card55 = "§"
card66 = "$"
card77 = "Ł"
card88 = "&"

board_coor = {'A1': emptycard, 'A2': emptycard, 'A3': emptycard, 'A4': emptycard,
              'B1': emptycard, 'B2': emptycard, 'B3': emptycard, 'B4': emptycard,
              'C1': emptycard, 'C2': emptycard, 'C3': emptycard, 'C4': emptycard,
              'D1': emptycard, 'D2': emptycard, 'D3': emptycard, 'D4': emptycard}



def print_board():
    print("")
    print('     1   2   3   4  ')
    print('   -----------------')
    print('   |   |   |   |   |')
    print(' A | ' + board_coor['A1'] + ' | ' + board_coor['A2'] + ' | ' + board_coor['A3']+ ' | ' + board_coor['A4']+ ' | ')
    print('   |   |   |   |   |')
    print('   -----------------')
    print('   |   |   |   |   |')
    print(' B | ' + board_coor['B1'] + ' | ' + board_coor['B2']+ ' | ' + board_coor['B3']+ ' | ' + board_coor['B4']+ ' | ')
    print('   |   |   |   |   |')
    print('   -----------------')
    print('   |   |   |   |   |')
    print(' C | ' + board_coor['C1'] + ' | ' + board_coor['C2'] + ' | ' + board_coor['C3']+ ' | ' + board_coor['C4']+ ' | ')
    print('   |   |   |   |   |')
    print('   -----------------')
    print('   |   |   |   |   |')
    print(' D | ' + board_coor['D1'] + ' | ' + board_coor['D2']+ ' | ' + board_coor['D3']+ ' | ' + board_coor['D4']+ ' | ')
    print('   |   |   |   |   |')
    print('   -----------------')
    print("")


def card_turn():
    mark1 = input("Type the card's coordinate to turn it: ").upper()
    while mark1 not in board_coor:
        mark1 = input("Type the card's coordinate to turn it: ").upper()


    if mark1 == 'A1':
        board_coor['A1'] = card1
    elif mark1 == 'A2':
        board_coor['A2'] = card2
    elif mark1 == 'A3':
        board_coor['A3'] = card3
    elif mark1 == 'A4':
        board_coor['A4'] = card4
    elif mark1 == 'B1':
        board_coor['B1'] = card5
    elif mark1 == 'B2':
        board_coor['B2'] = card6
    elif mark1 == 'B3':
        board_coor['B3'] = card7
    elif mark1 == 'B4':
        board_coor['B4'] = card8
    elif mark1 == 'C1':
        board_coor['C1'] = card11
    elif mark1 == 'C2':
        board_coor['C2'] = card22
    elif mark1 == 'C3':
        board_coor['C3'] = card33
    elif mark1 == 'C4':
        board_coor['C4'] = card44
    elif mark1 == 'D1':
        board_coor['D1'] = card55
    elif mark1 == 'D2':
        board_coor['D2'] = card66
    elif mark1 == 'D3':
        board_coor['D3'] = card77
    elif mark1 == 'D4':
        board_coor['D4'] = card88
    

    mark2 = input("Type the second card's coordinate to turn it up: ").upper()
    while mark2 not in board_coor:
        mark2 = input("Type the second card's coordinate to turn it up: ").upper()

    if mark2 == 'A1':
        board_coor['A1'] = card1
    elif mark2 == 'A2':
        board_coor['A2'] = card2
    elif mark2 == 'A3':
        board_coor['A3'] = card3
    elif mark2 == 'A4':
        board_coor['A4'] = card4
    elif mark2 == 'B1':
        board_coor['B1'] = card5
    elif mark2 == 'B2':
        board_coor['B2'] = card6
    elif mark2 == 'B3':
        board_coor['B3'] = card7
    elif mark2 == 'B4':
        board_coor['B4'] = card8
    elif mark2 == 'C1':
        board_coor['C1'] = card11
    elif mark2 == 'C2':
        board_coor['C2'] = card22
    elif mark2 == 'C3':
        board_coor['C3'] = card33
    elif mark2 == 'C4':
        board_coor['C4'] = card44
    elif mark2 == 'D1':
        board_coor['D1'] = card55
    elif mark2 == 'D2':
        board_coor['D2'] = card66
    elif mark2 == 'D3':
        board_coor['D3'] = card77
    elif mark2 == 'D4':
        board_coor['D4'] = card88
    
    marks = [mark1, mark2]
    return marks

def compare(marks):
    if marks[0] == marks[1]:
        print("You cannot turn same cards - try again!")
        board_coor[marks[0]] = emptycard
    elif marks[0]!= marks[1]:
        if board_coor[marks[0]] == board_coor[marks[1]]:
            print("Congrats - it's a match!")
        else:
            print("No match - try again!")
            board_coor[marks[0]] = emptycard
            board_coor[marks[1]] = emptycard
 

def gameend():
    if str(" ") not in board_coor.values():
        print("You win! Cheers!")
        continuegame = input("Would you like to continue? If yes, type 'y' or 'no' to exit the game: ")
        if continuegame == 'y' or continuegame == 'Y':
            board_coor['A1'] = emptycard
            board_coor['A2'] = emptycard
            board_coor['A3'] = emptycard
            board_coor['A4'] = emptycard
            board_coor['B1'] = emptycard
            board_coor['B2'] = emptycard
            board_coor['B3'] = emptycard
            board_coor['B4'] = emptycard
            board_coor['C1'] = emptycard
            board_coor['C2'] = emptycard
            board_coor['C3'] = emptycard
            board_coor['C4'] = emptycard
            board_coor['D1'] = emptycard
            board_coor['D2'] = emptycard
            board_coor['D3'] = emptycard
            board_coor['D4'] = emptycard
        if continuegame == 'n' or continuegame == 'N':
            print("See you!")

def score():
    elapsed_time = time.time() - start_time
    time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    if elapsed_time <= 100:
        print("You have great memory")
    elif elapsed_time >= 101:
        print("Improve your memory! Play again!")

   
while True:
    print_board()
    start_time = time.time()
    marks = card_turn()
    print_board()
    compare(marks)
    gameend()
    score()