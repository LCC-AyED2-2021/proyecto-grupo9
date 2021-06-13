import personal_library
import algo1
#este codigo lo escribi para poder probar  como funciona 
"""create Tarda mas de 5 M en ejecutarse con los 
documentos dados por los profes(cambiar el path)"""
B=personal_library.create('your path')


end = False
while end != True:
    A=algo1.input_str('ingrese una wor_key  ')
    
    
    # ------search tarda menos pero aun no funciona 
    personal_library.search(B,A)
    
    
    print('ingrese salir si dececea salir')
    a= algo1.input_str('Enter to continue')
    if a == 'salir':
        end = True
print ('end')    
    
