
from pathlib import Path
import os
import glob
import shutil
import os.path, time



def main():
    
    ''' This is the main part of the function,
    user should put the path of a file as the input '''
    
    root = input()

    while os.path.exists(root)==False:
        print ('ERROR')

    
    first_step(root)

    
def first_step(root):
    
    ''' This is the first part of the function, user should type N,E or S to decide
    which way of searching file should be applied'''
    
    command  = input()
    
    if command[0] !='N' and command[0] != 'E'and  command[0] !='S':
        print ('ERROR')
        first_step(root)
        
    elif command[0] == 'N':
        file = search_file_name(command[2:],root)
        second_step(file)

    elif command[0] == 'E':
        file = seaech_file_extension(command[2:],root)
        second_step(file)

    elif command[0] == 'S':
        try:
            size = int(command[2:])
            List = search_file_size(size,root)
            second_step(List)
            
        except:
            print('ERROR')
            first_step(root)


def second_step(L:list):
    
    '''This is the second part of the function, user should type P,F,D or T to
    decide which instruction should be applied'''

    command = input()

    if command[0] !='P' and command[0] != 'F'and  command[0] !='D'and  command[0] !='T':
        print('ERROR')
        second_step(L)

    elif command[0] == 'P':
        for item in L:
            print (item)

    elif command[0] == 'F':
        for item in L:
            file = item.open()
            print(item)
            print(file.readline())
            

    elif command[0] == 'D':
        
        for item in L:
            copy_file(item)

    elif command[0] == 'T':
        for item in L:
            a  = str(item)
           
            os.utime(a,(os.path.getatime(a),time.time()))
            
            

def search_file_name(file_name:str,root)->list:
    '''This function search the file by its name'''
    list_of_file = []
 

    for root, dirs, files in os.walk(root):
        for file in files:
            
            

            if file_name in file and os.path.isdir(file)==False:
                
                list_of_file.append(file)

               
            elif os.path.isdir(file)==True:
                for directory in dirs:
                    search_file_name(file_name, file)
                    
    return list_of_file
            
            


def seaech_file_extension(file_name:str,root)->list:
    '''This function search the file by its extension'''

    list_of_file = []
    for root, dirs, files in os.walk(root):
        for file in files:
            if file.endswith(file_name) and os.path.isdir(file)==False:
                list_of_file.append(file)

            elif os.path.isdir(file)==True:
                seaech_file_extension(file_name,file)
                
            

    return list_of_file
            
                

    

def search_file_size(size:int,root)->list:
    '''This function search the file by looking for the file that is bigger that
    the size input'''

    List_of_file = []

    result = list(Path(root).glob('**/*.*'))
    for item in result:
        if item.stat().st_size >= size:
            List_of_file.append(item)
    
    return List_of_file

def copy_file(file_path:Path):
    '''This function copy the content of an orginial file to
    a duplicated file'''
    
    new_path = str(file_path) + '.dup'
    shutil.copy(str(file_path), new_path)


        
main()      
    






    
