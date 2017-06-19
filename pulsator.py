# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
       

    def __init__(self,x,y):   
        self.count = 30
        self.item = 0
        Black_Hole.__init__(self,x,y)
        
        
        
    def update(self,model):
        
        absorbed = Black_Hole.update(self,model)
        
        self.item = self.item + 1
        
        if self.item == self.count :
            self.change_dimension(-1,-1)
            if self.get_dimension()[1] == 0 or self.get_dimension()[0] == 0:
                model.remove(self)
            self.item = 0
            
        if len(absorbed) != 0:
            x = len(absorbed)
            self.change_dimension(x,x)
            self.item = 0
            
        return absorbed