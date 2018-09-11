#!python3

import collections

#GLOBALS: 

turn=0




board=[range(0,3),range(0,3), range(0,3)] # lista miejsc 3x3

def print_board(board):
    i=0
    while  i<3:
        for place in board[i]:

            if isinstance(place,str):
                print(place, end = ' ')
            else: 
                print('.', end=' ')

        i+=1
        print('')


def make_move(player,board):
	""" 
	INPUT : Player ID
	OUTPUT: List of coordinates of player's move or False if the move is imposible

	"""

	print (player+ " it's your turn !")

	the_move=input('Enter  your move :')

	# check if move is possible

	

	coordinates=split(the_move)

	coordinates[0]=int(coordinates[0])  #conversion to int list
	coordinates[1]=int(coordinates[1])

	# error check in "The move - splited"

	if coordinates[0] >=3 and coordinates[1] >= 3 and coordinates [0]<0 and coordinates[1]<0:
		print(' out of board,dude ! ')
		return False


	if board[coordinates[0]][coordinates[1]] == 'X' or board[coordinates[0]][coordinates[1]] == 'O':

		 print ("You can't do that ! ")
		return False


	update_board(coordinates, player, board)

	

	return split(the_move)


def update_board(move, player, board)
	board[move[0]] [move[1]] =  player



def check_if_win(board, move):
	"""
	INPUT: BOARD, POSITION OF LAST MOVE
	OUTPUT: SIGN OF WINNER OR FALSE (if there is no winner yet)

	Program gets through lines and cross lines on the board and checks if there is a win. 
	For lines counter is implemented, that counts if there is exactly 3 of one sign
	"""



	if turn>=3:
		

		#skosy
		if board[1][1]== board[0][0] and board[1][1]== board[2][2]:
			return board[1][1]
		if board[1][1]== board[0][2] and board[1][1] == board[2][0]:
			return board[1][1]


		line_checking_counter=collections.Counter()
		# linie

		for column in board:
			for place in column:
				line_checking_counter[place]+=1

		if line_checking_counter[column[0]]==3: 
			return column[0]



		#reset
		line_checking_counter['X']=0
		line_checking_counter['O']=0


		while i<3:
			for column in board:
				line_checking_counter[column[i]]+=1
			if line_checking_counter[column[i]]==3
				return column[i]
			i+=1

		
		if turn == 9:  # For Tie situation
			return 'No_One'




first_player=''
secound_player=''


game_end=False
want_reply=False


first_player=input("Write X or O")
if first_player== 'X':
	secound_player='O'
elif first_player == 'O':
	secound_player='X'
else:
	print('NO OTHER SIGNS !')
	game_end=True # ??? 

while !game_end:



	# jakieś testy trzeba zrobić