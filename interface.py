# Yikang Liu 79955769


import othello

gamestate = othello.gamestate()

def draw_board():
    '''Draw the game board'''
    for y in range(gamestate.col):
        for x in range(gamestate.row):
            if gamestate.board[y][x]== 0:
                print('.', end = ' ')
            elif gamestate.board[y][x] == 'B':
                print('B', end = ' ')
            elif gamestate.board[y][x] == 'W':
                print('W', end = ' ')
        print()

def main():
    
    '''The part to run the function, get all five inuput
    and check move, and place the dis and flip the dis'''

    print('Full')
    
    a = gamestate.create_board()
    gamestate.who_goes_first()
    a = gamestate.board_arrangement()
    winner = input('Most or least:')

    
    b = gamestate.get_black_score()
    w = gamestate.get_white_score()

    print('B:',b, 'W:',w)
    draw_board()
    print('turn =', gamestate.turn)
    

    while gamestate.check_gameover() == False:
        try:

            
            move = input('Enter the move')
            col = int(move[0])
            row = int(move[2])
            
            gamestate.flip(col-1,row-1)
            print('Valid')
            gamestate.turn = gamestate.switch_turn(gamestate.turn)

           

            b = gamestate.get_black_score()
            w = gamestate.get_white_score()

            print('B:',b, 'W:',w)

           
            
            draw_board()
            print('turn =', gamestate.turn)
            
        except:
            print('invalid')

    gamestate.black = gamestate.get_black_score()
    gamestate.white = gamestate.get_white_score()
    gamestate.check_winner(winner)
    
    
    
    

if __name__ == '__main__':
    main()
