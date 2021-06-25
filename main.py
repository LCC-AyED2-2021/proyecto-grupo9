import personal_library
import algo1
import pickle

personal_library.create('local_path')

end = False
while end != True:
    print("enter a keyword")
    A = algo1.input_str("")
    
    with open('libreria', 'br') as lib:
        B = pickle.load(lib)
    
    personal_library.search(B,A)
    
    print('enter *exit* to end')
    a = algo1.input_str("")
    if a == 'exit':
        end = True
print ('end')   
    
