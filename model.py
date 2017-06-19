import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=


simulton = set()

execute = False
cycle = 0
clicked = None
pause = False

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global execute,cycle,simulton,pause
    
    cycle = 0
    pause = False
    simulton = set()
    execute = False


#start execute the simulation
def start ():
    global execute
    execute = True

#stop execute the simulation (freezing it)
def stop ():
    global execute
    execute = False


#tep just one update in the simulation
def step ():
    global execute,pause
    
    execute = True
    pause = True


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global clicked
    clicked = kind
    
    


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    
    if clicked == 'Remove':
        
        def check(z):
            if z.contains((x,y)) == True:
                return True
        for y in find(lambda x : check(x) == True):
            simulton.discard(y) 
        
    elif clicked == None:
        print('choose an object')        
                                     
    else:
        simulton.add(eval(clicked+'('+ str(x)+','+ str(y)+')'))   


#add simulton s to the simulation
def add(s):
    global simulton
    simulton.add(s)
    
    

# remove simulton s from the simulation    
def remove(s):
    global simulton
    simulton.discard(s)
    
    

#find/return a set of simulton that each satisfy predicate p    
def find(p):
    d = set()
    for x in set(simulton):
        if p(x) == True:
            d.add(x)
    return d
        
    


#call update for every simulton in the simulation
def update_all():
    global execute, pause,cycle,world
    if execute == True:
        
        cycle = cycle + 1
        
        for x in set(simulton):
            if x in simulton:
                x.update(model) 
                
        if pause != False:
            execute = False
            pause = False
    else:
        pass
                

#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for x in controller.the_canvas.find_all():
        controller.the_canvas.delete(x)
    for x in simulton:
        x.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(cycle)+' cycles/'+str(len(simulton))+' simultons')