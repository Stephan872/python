

import tkinter



DEFAULT_FONT = ('Helvetica', 14)





class NameDialog:
    def __init__(self):
        '''the function to create all the label and entry'''
        
        self._dialog_window = tkinter.Toplevel()


        

        who_label = tkinter.Label(
            master = self._dialog_window, text = 'Othello',
            font = DEFAULT_FONT)

        who_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        row_label = tkinter.Label(
            master = self._dialog_window, text = 'row:',
            font = DEFAULT_FONT)

        row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._row_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        col_label = tkinter.Label(
            master = self._dialog_window, text = 'col:',
            font = DEFAULT_FONT)

        col_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._col_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._col_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        turn_label = tkinter.Label(
            master = self._dialog_window, text = 'turn:',
            font = DEFAULT_FONT)

        turn_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._turn_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._turn_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        arrange_label = tkinter.Label(
            master = self._dialog_window, text = 'arrange:',
            font = DEFAULT_FONT)

        arrange_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._arrange_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._arrange_entry.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        win_label = tkinter.Label(
            master = self._dialog_window, text = 'win:',
            font = DEFAULT_FONT)

        win_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._win_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._win_entry.grid(
            row = 5, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)


        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)


        

        self._ok_clicked = False
        self.col = 0
        self.row = 0
        self.turn = ''
        self.arrange = ''
        self.win = ''


    def show(self) -> None:
        '''show all the label and entry'''
        
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()


   
    def was_ok_clicked(self) -> bool:
        '''return ok_clicked'''
        return self._ok_clicked


   

    def _on_ok_button(self) -> None:
        '''check it the buttom is clicked and get all the value in the entry'''
        self._ok_clicked = True
        
        self.row = int(self._row_entry.get())
        self.col = int(self._col_entry.get())
        self.turn = self._turn_entry.get()
        self.arrange = self._arrange_entry.get()
        self.win = self._win_entry.get()

        self._dialog_window.destroy()


    def _on_cancel_button(self) -> None:
        '''destroy the window'''
        
        self._dialog_window.destroy()






class GreetingsApplication:
    def __init__(self):
        '''create the start buttom and the string on the bottom'''
        self._root_window = tkinter.Tk()
        

        greet_button = tkinter.Button(
            master = self._root_window, text = 'Start', font = DEFAULT_FONT,
            command = self._on_greet)

        greet_button.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)


        self._greeting_text = tkinter.StringVar()
        self._greeting_text.set('Press start!')

       
        greeting_label = tkinter.Label(
            master = self._root_window, textvariable = self._greeting_text,
            font = DEFAULT_FONT)

        greeting_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def start(self) -> None:
        '''start the main loop'''
        self._root_window.mainloop()


    def _on_greet(self) -> None:
        '''get all the value in the window and destroy the window'''
        
        dialog = NameDialog()
        dialog.show()

      
        if dialog.was_ok_clicked():

            
            self._col = dialog.col
            self._row = dialog.row
            self._turn = dialog.turn
            self._arrange = dialog.arrange
            self._win = dialog.win
            

            self._root_window.destroy()

