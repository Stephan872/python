# A Hunter is both a Mobile_Simulton and a Pulsator in that it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
       
    
    def __init__(self,x,y):  
        self.hunt = 200 
        Pulsator.__init__(self,x,y)
        width,height = self.get_dimension()
        
        Mobile_Simulton.__init__(self,x,y,width,height,0,5)
        
        self.randomize_angle()
        
        
    def update(self,model):
        
        absorbed = Pulsator.update(self,model)
        
        def check(x):
            if isinstance(x,Prey) == True and self.distance(x.get_location()) <= self.hunt:
                return True
            
        detected = model.find(lambda x :check(x) == True)
        
        if detected:
            l = []
            z = []
            for s in detected:
                z.append(s)
                l.append(self.distance(s.get_location()))
            x = min(l)
            i = l.index(x)
            d = z[i] 
                
            d1 = self.get_location()[0]
            d2 = self.get_location()[1]
            x  = d.get_location()[0]
            y  = d.get_location()[1]
            
            self.set_angle(atan2(y-d2,x-d1))
            
        self.move()
        
        return absorbed

