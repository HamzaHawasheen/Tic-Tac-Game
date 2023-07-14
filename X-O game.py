import time
def showresult():
    print(f"{xcgame[0]}|{xcgame[1]}|{xcgame[2]}    D0|D1|D2")
    print(f"{xcgame[3]}|{xcgame[4]}|{xcgame[5]}    D3|D4|D5")
    print(f"{xcgame[6]}|{xcgame[7]}|{xcgame[8]}    D6|D7|D8")
def win():
    global result
    if choice == 'X':
        for h in range(9):
            if h % 2 == 0:
                if (xcgame[0] == xcgame[1] == xcgame[2]):
                    if xcgame[0] == 'X' and xcgame[1] == 'X' and xcgame[2] == 'X':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[3] == xcgame[4] == xcgame[5]:
                    if xcgame[3] == 'X' and xcgame[4] == 'X' and xcgame[5] == 'X':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[6] == xcgame[7] == xcgame[8]:
                    if xcgame[6] == 'X' and xcgame[7] == 'X' and xcgame[8] == 'X':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[0] == xcgame[3] == xcgame[6]:
                    if xcgame[0] == 'X' and xcgame[3] == 'X' and xcgame[6] == 'X':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[1] == xcgame[4] == xcgame[7]:
                    if xcgame[1] == 'X' and xcgame[4] == 'X' and xcgame[7] == 'X':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[2] == xcgame[5] == xcgame[8]:
                    if xcgame[2] == 'X' and xcgame[5] == 'X' and xcgame[8] == 'X':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[0] == xcgame[4] == xcgame[8]:
                    if xcgame[0] == 'X' and xcgame[4] == 'X' and xcgame[8] == 'X':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[2] == xcgame[4] == xcgame[6]:
                    if xcgame[2] == 'X' and xcgame[4] == 'X' and xcgame[6] == 'X':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
            else:
                if xcgame[0] == xcgame[1] == xcgame[2]:
                    if xcgame[0] == 'O' and xcgame[1] == 'O' and xcgame[2] == 'O':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[3] == xcgame[4] == xcgame[5]:
                    if xcgame[3] == 'O' and xcgame[4] == 'O' and xcgame[5] == 'O':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[6] == xcgame[7] == xcgame[8]:
                    if xcgame[6] == 'O' and xcgame[7] == 'O' and xcgame[8] == 'O':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[0] == xcgame[3] == xcgame[6]:
                    if xcgame[0] == 'O' and xcgame[3] == 'O' and xcgame[6] == 'O':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[1] == xcgame[4] == xcgame[7]:
                    if xcgame[1] == 'O' and xcgame[4] == 'O' and xcgame[7] == 'O':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[2] == xcgame[5] == xcgame[8]:
                    if xcgame[2] == 'O' and xcgame[5] == 'O' and xcgame[8] == 'O':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[0] == xcgame[4] == xcgame[8]:
                    if xcgame[0] == 'O' and xcgame[4] == 'O' and xcgame[8] == 'O':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[2] == xcgame[4] == xcgame[6]:
                    if xcgame[2] == 'O' and xcgame[4] == 'O' and xcgame[6] == 'O':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
    else:
        for g in range(9):
            if g % 2 == 0:
                if xcgame[0] == xcgame[1] == xcgame[2]:
                    if xcgame[0] == 'X' and xcgame[1] == 'X' and xcgame[2] == 'X':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[3] == xcgame[4] == xcgame[5]:
                    if xcgame[3] == 'X' and xcgame[4] == 'X' and xcgame[5] == 'X':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[6] == xcgame[7] == xcgame[8]:
                    if xcgame[6] == 'X' and xcgame[7] == 'X' and xcgame[8] == 'X':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[0] == xcgame[3] == xcgame[6]:
                    if xcgame[0] == 'X' and xcgame[3] == 'X' and xcgame[6] == 'X':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[1] == xcgame[4] == xcgame[7]:
                    if xcgame[1] == 'X' and xcgame[4] == 'X' and xcgame[7] == 'X':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[2] == xcgame[5] == xcgame[8]:
                    if xcgame[2] == 'X' and xcgame[5] == 'X' and xcgame[8] == 'X':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[0] == xcgame[4] == xcgame[8]:
                    if xcgame[0] == 'X' and xcgame[4] == 'X' and xcgame[8] == 'X':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[2] == xcgame[4] == xcgame[6]:
                    if xcgame[2] == 'X' and xcgame[4] == 'X' and xcgame[6] == 'X':
                        print(f"{second_player_name} is win! congratulations!")
                        print(f"{first_player_name} is lose! hard luck")
                        result += 1
                        break
            else:
                if (xcgame[0] == xcgame[1] == xcgame[2]):
                    if xcgame[0] == 'O' and xcgame[1] == 'O' and xcgame[2] == 'O':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[3] == xcgame[4] == xcgame[5]:
                    if xcgame[3] == 'O' and xcgame[4] == 'O' and xcgame[5] == 'O':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[6] == xcgame[7] == xcgame[8]:
                    if xcgame[6] == 'O' and xcgame[7] == 'O' and xcgame[8] == 'O':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[0] == xcgame[3] == xcgame[6]:
                    if xcgame[0] == 'O' and xcgame[3] == 'O' and xcgame[6] == 'O':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[1] == xcgame[4] == xcgame[7]:
                    if xcgame[1] == 'O' and xcgame[4] == 'O' and xcgame[7] == 'O':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[2] == xcgame[5] == xcgame[8]:
                    if xcgame[2] == 'O' and xcgame[5] == 'O' and xcgame[8] == 'O':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[0] == xcgame[4] == xcgame[8]:
                    if xcgame[0] == 'O' and xcgame[4] == 'O' and xcgame[8] == 'O':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
                if xcgame[2] == xcgame[4] == xcgame[6]:
                    if xcgame[2] == 'O' and xcgame[4] == 'O' and xcgame[6] == 'O':
                        print(f"{first_player_name} is win! congratulations!")
                        print(f"{second_player_name} is lose! hard luck")
                        result += 1
                        break
xcgame = [" "," "," "," "," "," "," "," "," "] # assume xcgame is xogame
result = 0
print("X-O Game")
time.sleep(1)
print("You must have 2 players to be able to play")
time.sleep(1)
print("The player who chooses X is the one who starts first")
time.sleep(1)
print("Please enter the names of the player")
time.sleep(1)
print("Please enter the name of first player: ")
first_player_name = input().title().strip()
time.sleep(1)
print("Please enter the name of second player: ")
second_player_name = input().title().strip()
time.sleep(1)
print(f"Hello {first_player_name}")
print(f"Hello {second_player_name}")
time.sleep(1)
print(f"{first_player_name} please choose X or O: ")
choice = input().upper().strip()
showresult()
if choice == 'X':
    print(f"{first_player_name} will start first")
    time.sleep(1)
    for i in range(9):
        if i % 2 == 0:
            print(f"{first_player_name} please enter the X in any place: ")
            print("Note! enter one of the this choose D1,D2,D3,D4,D5,D6,D7,D8 and D9")
            win()
            if result > 0:
                break
            anyplace = input().upper().strip()
            if anyplace == 'D0':
                xcgame.pop(0)
                xcgame.insert(0, "X")
            if anyplace == 'D1':
                xcgame.pop(1)
                xcgame.insert(1, "X")
            if anyplace == 'D2':
                xcgame.pop(2)
                xcgame.insert(2, "X")
            if anyplace == 'D3':
                xcgame.pop(3)
                xcgame.insert(3, "X")
            if anyplace == 'D4':
                xcgame.pop(4)
                xcgame.insert(4, "X")
            if anyplace == 'D5':
                xcgame.pop(5)
                xcgame.insert(5, "X")
            if anyplace == 'D6':
                xcgame.pop(6)
                xcgame.insert(6, "X")
            if anyplace == 'D7':
                xcgame.pop(7)
                xcgame.insert(7, "X")
            if anyplace == 'D8':
                xcgame.pop(8)
                xcgame.insert(8, "X")
            showresult()
        else:
            print(f"{second_player_name} please enter the O in any place: ")
            print("Note! enter one of the this choose D1,D2,D3,D4,D5,D6,D7,D8 and D9")
            win()
            if result > 0:
                break
            anyplace = input().upper().strip()
            if anyplace == 'D0':
                xcgame.pop(0)
                xcgame.insert(0, "O")
            if anyplace == 'D1':
                xcgame.pop(1)
                xcgame.insert(1, "O")
            if anyplace == 'D2':
                xcgame.pop(2)
                xcgame.insert(2, "O")
            if anyplace == 'D3':
                xcgame.pop(3)
                xcgame.insert(3, "O")
            if anyplace == 'D4':
                xcgame.pop(4)
                xcgame.insert(4, "O")
            if anyplace == 'D5':
                xcgame.pop(5)
                xcgame.insert(5, "O")
            if anyplace == 'D6':
                xcgame.pop(6)
                xcgame.insert(6, "O")
            if anyplace == 'D7':
                xcgame.pop(7)
                xcgame.insert(7, "O")
            if anyplace == 'D8':
                xcgame.pop(8)
                xcgame.insert(8, "O")
            showresult()
else:
    print(f"{second_player_name} will start first")
    time.sleep(1)
    for j in range(9):
        if j % 2 == 0:
            print(f"{second_player_name} please enter the X in any place: ")
            print("Note! enter one of the this choose D1,D2,D3,D4,D5,D6,D7,D8 and D9")
            win()
            if result > 0:
                break
            anyplace = input().upper().strip()
            if anyplace == 'D0':
                xcgame.pop(0)
                xcgame.insert(0, "X")
            if anyplace == 'D1':
                xcgame.pop(1)
                xcgame.insert(1, "X")
            if anyplace == 'D2':
                xcgame.pop(2)
                xcgame.insert(2, "X")
            if anyplace == 'D3':
                xcgame.pop(3)
                xcgame.insert(3, "X")
            if anyplace == 'D4':
                xcgame.pop(4)
                xcgame.insert(4, "X")
            if anyplace == 'D5':
                xcgame.pop(5)
                xcgame.insert(5, "X")
            if anyplace == 'D6':
                xcgame.pop(6)
                xcgame.insert(6, "X")
            if anyplace == 'D7':
                xcgame.pop(7)
                xcgame.insert(7, "X")
            if anyplace == 'D8':
                xcgame.pop(8)
                xcgame.insert(8, "X")
            showresult()
        else:
            print(f"{first_player_name} please enter the O in any place: ")
            print("Note! enter one of the this choose D0,D1,D2,D3,D4,D5,D6,D7 and D8")
            win()
            if result > 0:
                break
            anyplace = input().upper().strip()
            if anyplace == 'D0':
                xcgame.pop(0)
                xcgame.insert(0, "O")
            if anyplace == 'D1':
                xcgame.pop(1)
                xcgame.insert(1, "O")
            if anyplace == 'D2':
                xcgame.pop(2)
                xcgame.insert(2, "O")
            if anyplace == 'D3':
                xcgame.pop(3)
                xcgame.insert(3, "O")
            if anyplace == 'D4':
                xcgame.pop(4)
                xcgame.insert(4, "O")
            if anyplace == 'D5':
                xcgame.pop(5)
                xcgame.insert(5, "O")
            if anyplace == 'D6':
                xcgame.pop(6)
                xcgame.insert(6, "O")
            if anyplace == 'D7':
                xcgame.pop(7)
                xcgame.insert(7, "O")
            if anyplace == 'D8':
                xcgame.pop(8)
                xcgame.insert(8, "O")
            showresult()