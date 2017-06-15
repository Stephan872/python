


NONE = 0
BLACK ='B'
WHITE = 'W'

class gamestate:
    def __init__(self):
        '''Gamestate contains every function that is needed to
        run the game'''
        
        self.board = []
        self.col = 0
        self.row = 0
        self.turn = 0
        self.white = 0
        self.black = 0
        
    def create_board(self):
        ''' The function to create an empty board'''
        
        for c in range(self.col):
            self.board.append([])
            for r in range(self.row):
                self.board[-1].append(NONE)

        return self.board

    def board_arrangement(self,response:str):
        '''The function to decide how to arrange the board'''
        
        row = self.row
        col = self.col
        
        if response == 'B':
            self.board[int(col/2)-1][int(row/2)-1] = 'B'
            self.board[int(col/2) ][int(row/2) ] = 'B'
            self.board[int(col/2) ][int(row/2)-1] = 'W'
            self.board[int(col/2)-1 ][int(row/2) ] = 'W'
            
        if response =='W':
            self.board[int(col/2)-1][int(row/2)-1] = 'W'
            self.board[int(col/2) ][int(row/2) ] = 'W'
            self.board[int(col/2) ][int(row/2)-1] = 'B'
            self.board[int(col/2)-1 ][int(row/2)] = 'B'
            
        return self.board


    def who_goes_first(self):
        '''The function to decide which player goes first'''
        
        response = input('Which play goes first:')
        if response == 'B':
            self.turn = BLACK
        elif response =='W':
            self.turn = WHITE
            
        
        
    def switch_turn(self,turn:str):
        '''The function to switch the turn of the player'''
        
        if turn == BLACK:
            turn = WHITE
            return turn
        elif turn == WHITE:
            turn = BLACK
            return turn
        

    def check_move(self,col:int,row:int):
        '''The function to check the valid move for the player,
        and if the move if valid, append all the dis that can be fliped to the
        dis_to_flip, then return dis_to_flip'''
        

        if self.board[col][row] != 0 or col >=self.col or col<0 or row<0 or row >=self.row:
            return False
        
        dis_to_flip = []
        
        turn = self.turn
        otherturn = self.switch_turn(turn)

        
        if self.board[col][row] == 0:
            for xaxis, yaxis in  [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                x = col
                y = row
                x += xaxis
                y += yaxis
                
                if x <self.col and x>=0 and y>=0 and y <self.row and self.board[x][y] == otherturn:
                    x += xaxis
                    y += yaxis
                    if x >=self.col or x<0 or y<0 or y >=self.row:
                        continue
                    while self.board[x][y] == otherturn:
                        x += xaxis
                        y += yaxis
                        if  x >=self.col or x<0 or y<0 or y >=self.row:
                            break
                if x >=self.col or x<0 or y<0 or y >=self.row:
                        continue
                if self.board[x][y] == turn:
                    while True:
                        x -= xaxis
                        y -= yaxis
                        if x == col and y == row:
                            break
                        
                        
                        dis_to_flip.append((x,y))
        
                        
        if len(dis_to_flip) == 0:
            return False
        
        return dis_to_flip
        

    def flip(self, col:int,row:int):
        '''Make the move and flip all the dis in dis_to_flip'''
       
        dis_to_flip = self.check_move(col,row)
        if len(dis_to_flip) == 0:
            return False
        else:
            self.board[col][row] = self.turn
           
            for x,y in dis_to_flip:
                self.board[x][y]= self.turn
                
        return self.board
    

    def get_all_valid_move(self):
        '''Get all the valid move by calling the function
        check_move, and append the to the list validmove'''
        
        validmove = []
        for x in range(self.col):
            for y in range(self.row):
                if self.check_move(x,y) != False:
                    validmove.append((x+1,y+1))
        return validmove

    def check_gameover(self):
        '''To check if the game is over'''
        
        move = self.get_all_valid_move()
        if len(move)==0:
            return True
        else:
            return False

    def get_white_score(self):
        '''To get the score of white player'''
       
        white = 0
        for x in range(self.col):
            for y in range(self.row):
                if self.board[x][y] == 'W':
                    white += 1
        return white

    def get_black_score(self):
        '''To get the score of black player'''
        
        black = 0
    
        for x in range(self.col):
            for y in range(self.row):
                if self.board[x][y] == 'B':
                    black += 1
        return black

    def check_winner(self,winner:str):
        '''To check who is the winner'''
        
        if winner == '>':
            if self.white > self.black:
                print('WHITE Wins')
            elif self.white == self.black:
                print ('None')
            else:
                print('BLACK Wins')
        elif winner =='<':
            if self.white > self.black:
                print('BLACK Wins')
            elif self.white == self.black:
                print ('NONE')
            else:
                print('WHITE Wins')
        
            
        
            
        
        
        
        











