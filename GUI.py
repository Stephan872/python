

import tkinter
import othello
import window


gamestate = othello.gamestate()


class createboard:
    def __init__(self):
        '''the part to get all the value from window and pass
        them to the self'''


        app1 = window.GreetingsApplication()
        app1.start()
        
        app1._root_window.quit()

        self._columns =app1._col
        self._rows = app1._row
        self.turn =app1._turn
        self.arrange =app1._arrange 
        self.win = app1._win

        

        

        self.white = 2
        self.black = 2

        self.click = False
        self.col =0
        self.row = 0
        
        gamestate.col = self._columns
        gamestate.row = self._rows

        self.board = gamestate.create_board()
        self.board = gamestate.board_arrangement(self.arrange)
        
        
        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 500, height = 500,
            background = '#006000')

        self._canvas.pack(fill = tkinter.BOTH, expand = True)
        self._canvas.bind('<Configure>',self.draw_handler)
        
        self._canvas.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        
    def run(self):
        '''give the control to _root_window'''
        
        self._root_window.mainloop()

        

    def clicked(self,event: tkinter.Event):
        '''draw the spot where the user clicked, and pass the
        coordinate to the gamelogic'''
        
        
        x = event.x
        y = event.y
        coordinates = self._canvas.coords("current")


        row = coordinates[2]/(self._canvas.winfo_width()/self._columns)
        col = coordinates[3]/(self._canvas.winfo_height()/self._rows)

        self.eachrow = self._canvas.winfo_width()/self._columns
        self.eachcol = self._canvas.winfo_height()/self._rows



        self.row = int(row)
        self.col = int(col)

        
        gamestate.turn = self.turn
        try:
            self.dis_to_flip = gamestate.check_move(int(self.col)-1,int(self.row)-1)

            gamestate.flip(int(self.col)-1,int(self.row)-1)
        

            for y,x in self.dis_to_flip:
                x += 1
                y += 1



                if self.turn =='B':
                    self._canvas.create_oval(
                        (x-1)*self.eachrow, (y-1)*self.eachcol ,
                        x*self.eachrow , y*self.eachcol,
                        fill = 'black', outline = '#000000')
                elif self.turn == 'W':
                    self._canvas.create_oval(
                        (x-1)*self.eachrow, (y-1)*self.eachcol ,
                        x*self.eachrow , y*self.eachcol,
                        fill = 'white', outline = '#000000')
                
                
                    



            self.board = gamestate.board
                
            
            if self.turn == 'B':
                self._canvas.create_oval(
                        coordinates[0], coordinates[1],
                        coordinates[2]  , coordinates[3],
                        fill = 'black', outline = '#000000')

                self.turn = gamestate.switch_turn(self.turn)
                
                
            elif self.turn =='W':
                self._canvas.create_oval(
                        coordinates[0], coordinates[1],
                        coordinates[2]  , coordinates[3],
                        fill = 'white', outline = '#000000')
                
                
                self.turn = gamestate.switch_turn(self.turn)
                                
                
            self.update()
        except:
            print('This move is invalid, please try again')


    def drawline(self):
        '''create the gameboard and the window with the turn
        and white and black show on it'''
        
        self._canvas.delete(tkinter.ALL)
        column_width = self._canvas.winfo_width()/self._columns
        row_height = self._canvas.winfo_height()/self._rows
        for  x in range(self._columns):
            for y in range(self._rows):
                x1 = x * column_width
                y1 = y * row_height
                x2 = x1 + column_width
                y2 = y1 + row_height
                r = self._canvas.create_rectangle(x1,y1,x2,y2,fill = 'green')
                self._canvas.tag_bind(r,'<ButtonPress-1>',self.clicked)
                
                self._canvas.create_rectangle(x1,y1,x2,y2)
        self._canvas.bind('<Configure>',self.draw_handler)

        self._canvas.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._turn_label = tkinter.Label(
            master = self._root_window, text = 'turn = {}'.format(self.turn),
            font = ('Helvetica', 20))

        self._turn_label.grid(
            row = 1, column = 0, padx = 10, pady = (10, 0),
            sticky = tkinter.W + tkinter.E)

        self._white_label = tkinter.Label(
            master = self._root_window, text = 'white = {}'.format(gamestate.get_white_score()),
            font = ('Helvetica', 20))

        self._white_label.grid(
            row = 2, column = 0, padx = 10, pady = (10, 0),
            sticky = tkinter.W)

        self._black_label = tkinter.Label(
            master = self._root_window, text = 'black = {}'.format(gamestate.get_black_score()),
            font = ('Helvetica', 20))

        self._black_label.grid(
            row = 3, column = 0, padx = 10, pady = (10, 0),
            sticky = tkinter.W)




    def drawoval(self):
        '''draw the oval on the gameboard with the provided
        arrangement from the window'''

        center_x = self._canvas.winfo_width()/2
        center_y = self._canvas.winfo_height()/2

        radius_x = self._canvas.winfo_width()/self._columns/2
        radius_y = self._canvas.winfo_height()/self._rows/2

        if self.arrange == 'W':

            self._canvas.create_oval(
                    center_x - 2*radius_x, center_y - 2*radius_y,
                    center_x , center_y,
                    fill = 'white', outline = '#000000')

            self._canvas.create_oval(
                    center_x , center_y ,
                    center_x + 2*radius_x , center_y + 2*radius_y ,
                    fill = 'white', outline = '#000000')

            self._canvas.create_oval(
                    center_x+2*radius_x, center_y,
                    center_x, center_y-2*radius_y,
                    fill = 'black', outline = '#000000')
            
            self._canvas.create_oval(
                    center_x-2*radius_x, center_y,
                    center_x, center_y+2*radius_y,
                    fill = 'black', outline = '#000000')
        elif self.arrange == 'B':

            self._canvas.create_oval(
                    center_x - 2*radius_x, center_y - 2*radius_y,
                    center_x , center_y,
                    fill = 'black', outline = '#000000')

            self._canvas.create_oval(
                    center_x , center_y ,
                    center_x + 2*radius_x , center_y + 2*radius_y ,
                    fill = 'black', outline = '#000000')

            self._canvas.create_oval(
                    center_x+2*radius_x, center_y,
                    center_x, center_y-2*radius_y,
                    fill = 'white', outline = '#000000')
            
            self._canvas.create_oval(
                    center_x-2*radius_x, center_y,
                    center_x, center_y+2*radius_y,
                    fill = 'white', outline = '#000000')
            

    def draw_handler(self,event):
        '''draw the oval and the board'''
        
        self.drawline()
        self.drawoval()
    
    
    def update(self):
        '''update the turn and the score on the board'''
        white = gamestate.get_white_score()
        black = gamestate.get_black_score()
        self._turn_label['text'] = 'turn = {}'.format(self.turn)
        self._white_label['text'] = 'white = {}'.format(white)
        self._black_label['text'] = 'black = {}'.format(black)
        
        

if __name__ == '__main__':
    createboard().run()
    
    

    


    

