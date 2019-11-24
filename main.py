from user.user import UserClass

global method_dict
method_dict = {
    1: 'Login',
    2 : 'Create User'
    
} 

def main():
    global method_dict
    for key, value in method_dict.items():
            print('{}:{}'.format(key,value))
    while True:
        try:
            user_input = int(input('Enter you choice 1 and 2 only\n'))
            if user_input ==1 or user_input==2:
                if user_input ==1:
                    UserClass.adding_user()
                else:
                    print('testing')
                break
            else:
                print('Invalid input')
                continue
        except:
            print('Invalid input')
            continue
                    

if __name__ == "__main__":
    main()