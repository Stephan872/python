# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    
    
    def __init__(self,x,y): 
        self.raduis = 10  
        Simulton.__init__(self,x,y,self.raduis*2,self.raduis*2)
        
        
    def update(self,model):
        def check(x):
            if isinstance(x,Prey) == True and self.contains(x.get_location()) == True:
                return True
            
        absorbed = model.find(lambda x : check(x) == True)
        
        for x in absorbed:
            model.remove(x) 
        return absorbed
        
 
 
    def contains(self,xy):
        if self.get_dimension()[1]/2 >= self.distance(xy) or self.get_dimension()[0]/2 >= self.distance(xy):
            return True

               
    def display(self,the_canvas):
        width,height = self.get_dimension()
        the_canvas.create_oval(self._x-width * 0.5, self._y-height * 0.5,
                               self._x+width * 0.5, self._y+height * 0.5,
                               fill='black')