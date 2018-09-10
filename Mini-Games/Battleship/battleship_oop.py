class Board:
	
	grid = []
	
	def __init__(self):
		
		self.grid += [ ['0' for x in range(5)] for j in range (10)]
		#self.grid += [ ['X' for x in range(5)] for j in range (5,10)]
		
	def print_grid(self):
#		for col in self.grid[0]:
#			for row in self.grid[0]:
#			print range(self.grid[0])
#			print ''.join(str(range(len(self.grid[0]))))
#		print [int(range(self.grid[0])) for x in range(len(self.grid[0]))]
		print ' ----------'
		for row in self.grid:
			print '#','|', ' '.join(row)

class Player:
		
	def __init__(self, name):
		self.name = name
		self.score = 0
		self.boat_list = []
		self.miss_list = []
		self.hit_list = []
		self.result = ""
		
	def boats(self, cord):
		self.boat_list.append(cord)
		return self.boat_list

	def enuf_boats(self):
		max_boats = 2
		return (len(self.boat_list) < max_boats)
			
	def make_guess(self, guess):
		(x,y) = guess
		return guess

	def max_score(self):
		if self.score < len(self.boat_list):
			return True
		else:
			print "you won %s " % self.name
			return False

# 	def render_grid(self, Board):
# 	
# 		for b in self.boat_list:
# 			board.grid[b[0]][b[1]] = 'B'		
# 	
# 		for m in self.miss_list:
# 			board.grid[m[0]][m[1]] = 'M'
# 	
# 		for h in self.hit_list:
# 			board.grid[h[0]][h[1]] = 'H'


	def is_playing(self):
		return self.max_score() and self.result != "Miss"
		
def play():
	board = Board()
			
 	p1 = Player(raw_input("Please enter p1 name: "))
	while p1.enuf_boats():
 		p1.boat_list = p1.boats((int(input("Select Row: ")), int(input("Select Col: "))))
 	# 	p1.place_boats()
	p2 = Player(raw_input("Please enter p2 name: "))
	while p2.enuf_boats():
 		p2.boat_list = p2.boats((int(input("Select Row: ")), int(input("Select Col: "))))
 	# 	p2.place_boats()	


	# if 'hit' (i.e. guess is in the list): p1. convert boats...
	#else: p1. missed_boats
	
	# var =  p1.convert_boats()
# 	for j in p1.convert_boats():
#  		board.grid[var[0]][var[1]] = 'B'
#  	board.print_grid()

# 	second_var =  p1.missed_boats()
# 	for j in p1.convert_boats():
#  		board.grid[var[0]][var[1]] = 'M'
#  	board.print_grid()



#	hit =  True
	while (p1.is_playing() or p2.is_playing()): # if max_score... break
#		if p1.max_score() or p2.max_score() ... break
#		else: continue

		while p1.is_playing():
		
#			p1.render_grid()

			for b in p1.boat_list:
				board.grid[b[0]][b[1]] = 'B'		
	
			for m in p1.miss_list:
				board.grid[m[0]][m[1]] = 'M'
	
			for h in p1.hit_list:
				board.grid[h[0]][h[1]] = 'H'

	 		board.print_grid()
			
 			print 'The boat list for p1 is ' , p1.boat_list
			print 'The miss list for p1 is ' ,  p1.miss_list
			print 'The score for p1 is ' ,  p1.score
			guess = p1.make_guess((int(input("Guess Row: ")), int(input("Guess Col: "))))
			if guess in p2.boat_list:
				print 'Hit, go again!'
				p1.score+=1
				p1.result = "Hit"
				p1.hit_list.append(guess)
				# var =  p1.convert_boats()
# 				for j in p1.convert_boats():
# 			 		board.grid[var[0]][var[1]] = 'B'
# 				 	board.print_grid()

			else:
				p1.miss_list.append(guess)
				print 'The miss list for p1 is ' ,  p1.miss_list
				print "Miss: it is now %s\'s turn" % p2.name
				#Player = p2
				#hit = False
				p1.result = "Miss"
				print p1.result


			for m in p1.miss_list:
				board.grid[m[0]][m[1]] = 'M'
			
			board.print_grid()


				# mvar =  p1.missed_boats()
# 				for j in p1.convert_boats():
# 		 			board.grid[mvar[0]][mvar[1]] = 'M'
# 	 				board.print_grid()
 	
#		while p2:
	 	while p2.is_playing():
	
# 			for x in p2.convert_boats():
# 				board.grid = 'B'
# 			
# 				if not 'B' and not 'M':
# 					board.grid = '0'		
# 	 		
# 	 		for y in p2.missed_boats():
# 				board.grid[y][y] = 'M'

			for b in p2.boat_list:
				board.grid[b[0]][b[1]] = 'B'		
	
			for m in p2.miss_list:
				board.grid[m[0]][m[1]] = 'M'
	
			for h in p2.hit_list:
				board.grid[h[0]][h[1]] = 'H'
			
			board.print_grid()
	 		
			print 'The boat list for p2 is ' , p2.boat_list
			print 'The miss list for p2 is ' ,  p2.miss_list
			print 'The score for p2 is ' ,  p2.score
			guess = p2.make_guess((int(input("Guess Row: ")), int(input("Guess Col: "))))
			if guess in p1.boat_list:
				print 'Hit, go again!'
				p2.score+=1 
				p2.result = "Hit"
				p2.hit_list.append(guess)
			else:
				p2.miss_list.append(guess)
				print 'The miss list for p2 is ' ,  p2.miss_list
				print "Miss: it is now %s \'s turn" % p1.name
				#Player = p1
#				p2.result = False
				p2.result = "Miss"
				print p2.result
				
				for m in p2.miss_list:
					board.grid[m[0]][m[1]] = 'M'				
		p1.result = "reset"	
		p2.result = "reset"	


if __name__ == "__main__":
	play()