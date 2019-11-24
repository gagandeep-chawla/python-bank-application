import datetime

from user.generic_methods import input_name,input_dob,input_gender,input_phone,input_married

class UserClass:
    
    def __init__(self,firtmname,lastname,dob,gender,phone,married):
        self.firtmname = firtmname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.phone = phone
        self.married = married
    
    @classmethod
    def adding_user(cls): 
        cls.__init__(
            input_name('first'),
            input_name('last'),
            input_dob(),
            input_gender(),
            input_phone()
            )
        
                  
            
            