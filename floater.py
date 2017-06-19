# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    
    def __init__(self,x,y):   
        self.radius = 5
        Prey.__init__(self,x,y,self.radius,self.radius,0,5)
        self.randomize_angle()

        
    def update(self,model):
        import random
        number = random.uniform(-0.3,0.3)
        newspeed = random.uniform(max(self.get_speed() + number,3),7)
        self.set_velocity(newspeed,self.get_angle()+number)
        self.move()
 

    def display(self,the_canvas):
        
        the_canvas.create_oval(self._x-self.radius, self._y-self.radius,
                               self._x+self.radius, self._y+self.radius,
                               fill='red')