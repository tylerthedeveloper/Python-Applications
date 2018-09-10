board = []
player = 'p1','p2'
ship_row = 0; ship_col = 0

for x in range(10):
	board.append(["0"]*5)

def print_board():
	for row in board:
		print " ".join(row)

def flip_board():
	for row in reversed(board):
		print " ".join(row)

def place_ships():
	bool = True
	player = 'p1'
	while bool:
		while player == 'p1':
			print player
			for x in range(4):
				ship_row = int(raw_input("Select Row:"))
				ship_col = int(raw_input("Select Col:"))
				for y in range(4):	
					board[ship_row][ship_col] = ('X')
			player = 'p2'	

		while bool:	
			print player
			for x in range(4):
				ship_row = len(board)-1-int(raw_input("Select Row:"))
				ship_col = len(board[0])-1-int(raw_input("Select Col:"))
				for y in range(4):	
					board[ship_row][ship_col] = ('X')
				bool = False
			
player = 'p1'
winner = True; looper = 0; count = 0; count1 = 0
place_ships()
print_board()
while winner:
		while looper<1 and count<=4 and winner:
			if player == 'p1':
				print 'test:', ship_row, ship_col
				print "Player:", player
				guess_row = int(raw_input("Guess Row:"))
				guess_col = int(raw_input("Guess Col:"))
				count = count
					
			else:
				print 'test:', ship_row, ship_col
				print "Player:", player
				guess_row = len(board)-int(raw_input("Guess Row:"))
				guess_col = len(board)-int(raw_input("Guess Col:"))
				count = count1
			
	
			if count == 4:
				print "P1 wins"; winner = False; print_board()

			elif count1==4:
				print "P1 wins"; winner = False; print_board()
				
			else:
				if board[guess_row][guess_col] == 'X' and board[guess_row][guess_col] != 'H':
					print "That's a hit, go again"; board[guess_row][guess_col] = 'H'; count +=1
					print 'player:', player, "The count is", count; print_board(); looper=0

				else:
					if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
						print "That was off the board, go again"; looper-=1; print_board()
						
					elif board[guess_row][guess_col] == ('H' or 'X'):
						print "You went there already, go again"; looper-=1; print_board()
						
					else:
						print "That's a miss"; board[guess_row][guess_col] = 'M'
						
						if player == 'p1':
							player = 'p2'; print 'player:', player; looper-=1; flip_board()
						
						else:
							player = 'p1'; print 'player:', player; looper-=1; flip_board()