
import time
import os
import sys

cards = (" ", "@", "ß", "Đ", "€", "§", "$", "Ł", "&")

board_coor = {'A1': cards[0], 'A2': cards[0], 'A3': cards[0], 'A4': cards[0],
              'B1': cards[0], 'B2': cards[0], 'B3': cards[0], 'B4': cards[0],
              'C1': cards[0], 'C2': cards[0], 'C3': cards[0], 'C4': cards[0],
              'D1': cards[0], 'D2': cards[0], 'D3': cards[0], 'D4': cards[0]}


def print_board():
    print("")
    print('     1   2   3   4  ')
    print('   -----------------')
    print('   |   |   |   |   |')
    print(' A | ' + board_coor['A1'] + ' | ' + board_coor['A2'] + ' | ' + board_coor['A3'] + ' | ' + board_coor['A4'] + ' | ')
    print('   |   |   |   |   |')
    print('   -----------------')
    print('   |   |   |   |   |')
    print(' B | ' + board_coor['B1'] + ' | ' + board_coor['B2'] + ' | ' + board_coor['B3'] + ' | ' + board_coor['B4'] + ' | ')
    print('   |   |   |   |   |')
    print('   -----------------')
    print('   |   |   |   |   |')
    print(' C | ' + board_coor['C1'] + ' | ' + board_coor['C2'] + ' | ' + board_coor['C3'] + ' | ' + board_coor['C4'] + ' | ')
    print('   |   |   |   |   |')
    print('   -----------------')
    print('   |   |   |   |   |')
    print(' D | ' + board_coor['D1'] + ' | ' + board_coor['D2'] + ' | ' + board_coor['D3'] + ' | ' + board_coor['D4'] + ' | ')
    print('   |   |   |   |   |')
    print('   -----------------')
    print("")


def card_turn():
    mark1 = input("Type the card's coordinate to turn it: ").upper()
    while mark1 not in board_coor:
        mark1 = input("Type the card's coordinate to turn it: ").upper()

    if mark1 == 'A1':
        board_coor['A1'] = cards[1]
    elif mark1 == 'A2':
        board_coor['A2'] = cards[1]
    elif mark1 == 'A3':
        board_coor['A3'] = cards[1]
    elif mark1 == 'A4':
        board_coor['A4'] = cards[1]
    elif mark1 == 'B1':
        board_coor['B1'] = cards[1]
    elif mark1 == 'B2':
        board_coor['B2'] = cards[1]
    elif mark1 == 'B3':
        board_coor['B3'] = cards[1]
    elif mark1 == 'B4':
        board_coor['B4'] = cards[1]
    elif mark1 == 'C1':
        board_coor['C1'] = cards[1]
    elif mark1 == 'C2':
        board_coor['C2'] = cards[1]
    elif mark1 == 'C3':
        board_coor['C3'] = cards[1]
    elif mark1 == 'C4':
        board_coor['C4'] = cards[1]
    elif mark1 == 'D1':
        board_coor['D1'] = cards[1]
    elif mark1 == 'D2':
        board_coor['D2'] = cards[1]
    elif mark1 == 'D3':
        board_coor['D3'] = cards[1]
    elif mark1 == 'D4':
        board_coor['D4'] = cards[1]

    mark2 = input("Type the second card's coordinate to turn it up: ").upper()
    while mark2 not in board_coor:
        mark2 = input("Type the second card's coordinate to turn it up: ").upper()

    if mark2 == 'A1':
        board_coor['A1'] = cards[1]
    elif mark2 == 'A2':
        board_coor['A2'] = cards[1]
    elif mark2 == 'A3':
        board_coor['A3'] = cards[1]
    elif mark2 == 'A4':
        board_coor['A4'] = cards[1]
    elif mark2 == 'B1':
        board_coor['B1'] = cards[1]
    elif mark2 == 'B2':
        board_coor['B2'] = cards[1]
    elif mark2 == 'B3':
        board_coor['B3'] = cards[1]
    elif mark2 == 'B4':
        board_coor['B4'] = cards[1]
    elif mark2 == 'C1':
        board_coor['C1'] = cards[1]
    elif mark2 == 'C2':
        board_coor['C2'] = cards[1]
    elif mark2 == 'C3':
        board_coor['C3'] = cards[1]
    elif mark2 == 'C4':
        board_coor['C4'] = cards[1]
    elif mark2 == 'D1':
        board_coor['D1'] = cards[1]
    elif mark2 == 'D2':
        board_coor['D2'] = cards[1]
    elif mark2 == 'D3':
        board_coor['D3'] = cards[1]
    elif mark2 == 'D4':
        board_coor['D4'] = cards[1]

    marks = [mark1, mark2]
    return marks


def compare(marks):
    if marks[0] == marks[1]:
        print("You cannot turn same cards - try again!")
        board_coor[marks[0]] = emptycard
    elif marks[0] != marks[1]:
        if board_coor[marks[0]] == board_coor[marks[1]]:
            print("Congrats - it's a match!")
        else:
            print("No match - try again!")
            board_coor[marks[0]] = emptycard
            board_coor[marks[1]] = emptycard
            os.system('clear')


def gameend():
    if str(" ") not in board_coor.values():
        continuegame = input("Would you like to continue? If yes, type 'y' or 'n' to exit the game: ")
        if continuegame == 'y' or continuegame == 'Y':
            board_coor['A1'] = cards[0]
            board_coor['A2'] = cards[0]
            board_coor['A3'] = cards[0]
            board_coor['A4'] = cards[0]
            board_coor['B1'] = cards[0]
            board_coor['B2'] = cards[0]
            board_coor['B3'] = cards[0]
            board_coor['B4'] = cards[0]
            board_coor['C1'] = cards[0]
            board_coor['C2'] = cards[0]
            board_coor['C3'] = cards[0]
            board_coor['C4'] = cards[0]
            board_coor['D1'] = cards[0]
            board_coor['D2'] = cards[0]
            board_coor['D3'] = cards[0]
            board_coor['D4'] = cards[0]
            os.system('clear')
            timer()
        if continuegame == 'n' or continuegame == 'N':
            os.system('clear')
            print("See you!")
            sys.exit()


def timer():
    end = time.time()
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("You did it! Your time is: ")
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
    #if elapsed_time <= 100:
    #    print("You did it! Yout time is: ")
    #    print(elapsed_time)
    #    print("You have a great memory!")
    #elif elapsed_time >= 101:
    #    print("Improve your memory! Play again!")


#def output_clearing
   
while True:
    start = time.time()
    print_board()
    marks = card_turn()
    print_board()
    compare(marks)
    gameend()
