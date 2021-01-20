#Function assigned to print the board
def display(board):
	print("   |   |   ")
	print(" " + board[0] + " | " + board[1] + " | " + board[2])
	print("___|___|___")
	print("   |   |   ")
	print(" " + board[3] + " | " + board[4] + " | " + board[5])
	print("___|___|___")
	print("   |   |   ")
	print(" " + board[6] + " | " + board[7] + " | " + board[8])
	print("   |   |   ")

#Function assigned to check the board for wins
def win(board):
	return ((board[0] == board[1] == board[2] != ' ')		#Top row win
		or (board[3] == board[4] == board[5] != ' ')		#Mid row win
		or (board[6] == board[7] == board[8] != ' ')		#Bot row win
		or (board[0] == board[4] == board[8] != ' ')		#Top left to bot right win
		or (board[6] == board[4] == board[2] != ' ')		#Bot left to top right win
		or (board[0] == board[3] == board[6] != ' ')		#Left col win
		or (board[1] == board[4] == board[7] != ' ')		#Mid col win
		or (board[2] == board[5] == board[8] != ' '))		#Right col win

#Function to check if the board is full resulting in the game ending
def full_board(board):
	for i in board:
		if i == ' ':
			return False	
	return True

#Function announcing win
def win_announce(turn):
	if(turn):
		print("Player 2 (O) has WON!")
		print('____________________________________________________________________________________________________')
	else:
		print("Player 1 (X) has WON!")
		print('____________________________________________________________________________________________________')

#Error checking for spot vacancy
def spot_open(board, loc):
	return board[loc] != 'X' and board[loc] != 'O'

#Error checking for user input
def in_bounds(user_input):
	acceptable_inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 'Y', 'N']
	return user_input in acceptable_inputs


##############################################################################################################################
##																															##
##                                                   END OF HELPER FUNCTIONS											    ##
##																															##
##############################################################################################################################


#global variables
game_on = True
player_turn = True
new_game = True

#main game loop
while(game_on):

	#Setting game board and variables for a new game
	game_board_demo = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	player_turn = True
	new_game = False

	#Opening message and tutorial
	print('Welcome Tic Tac Toe!')
	print('This is the Game Board labelled from 1 to 9. \nA number will indicate where you would like to place your move.')
	print('X goes first! \nConnect 3 in a row to win, Have Fun!')
	display (game_board_demo)

	#Inner game loop to allow replays
	while(new_game == False):
		
		#Setting variables for each turn and taking input
		keep_playing = ' '
		proceed = False
		location = int(input('Please enter a position on the board: ')) - 1

		#User input error checking loop
		while(proceed == False):
			if(in_bounds(location) and spot_open(game_board, location)):
				proceed = True
			elif(in_bounds(location) == False):
				proceed = False
				print('____________________________________________________________________________________________________')
				print('Sorry, NOT IN BOUNDS!')
				print("Please enter a location between 1 and 9, and make sure it hasn't been played.")
				location = int(input('Please enter a position on the board: ')) - 1
			else:
				proceed = False
				print('____________________________________________________________________________________________________')
				print('Sorry, SPOTS TAKEN!')
				print("Please enter a location that hasn't been taken, and make sure it's between 1 and 9.")
				location = int(input('Please enter a position on the board: ')) - 1
	
		#Alternating Turns
		if(player_turn):
			game_board[location] = 'X'
			player_turn = False
		else:
			game_board[location] = 'O'
			player_turn = True

		#Printing Gameboard
		display(game_board)

		#Checking for a possible win or Tie
		if(win(game_board) or full_board(game_board)):
			proceed = False
			if(full_board(game_board) and win(game_board)):
				win_announce(player_turn)
			elif(full_board(game_board)):
				print("It's a TIE!")
				print('____________________________________________________________________________________________________')			
			else:
				win_announce(player_turn)
		
		#Requesting for a replay and error checking input
		while(proceed == False):
			keep_playing = (input('Would you like to play again? (Y/N): ')).upper()
			if(in_bounds(keep_playing) == False):
				print('Sorry, Would you like to play again? (Y/N): ')
				proceed = False
			else:
				if(keep_playing == 'Y'):
					proceed = True
					game_on = True
					new_game = True
				else:
					proceed = True
					game_on = False
					new_game = True
	
#Closing Message			
print('Thanks for playing!')

