import datetime

def input_name(name):
    instance = ''
    while True:
        while True:
            instance = input('Enter your {} name ?'.format(name))
            if instance.isalpha():
                break
            else:
                print('invalid {} name'.format(instance))
                continue
            
    return instance


def input_dob():
    date = ''
    while True:
        try: 
            date_entry = input('Enter a date in yyyy-mm-dd format ')
            year,month,day = map(int,date_entry.split('-'))
            if  len(year) !=4:
                print('invalid year\n please Enter the valid year')
                continue
            if  len(month) !=2:
                print('invalid month\n please Enter the valid year')
                continue
            if  len(day) !=2:
                print('invalid day\n please Enter the valid year')
                continue    
            date = datetime.date(year,month,day)
            break
        except:
            print('invalid date')
            continue
            
    return date

def input_gender():
    gender = ''
    while True:
        try:
            gender = input('Please choose Gender Male or Female')
            if gender.lower() in ('female',male):
                gender =  'male' if gender == 'male' else 'female'
            else:
                print('invalid input')
        except:
            print('invalid input')
            continue


def input_phone():
    number = ''
    while True:
        try:
            number = int(input('Please enter the moblie number'))
            if  len(str(number)) != 10:
                pinrt('invalid number')
                continue
            break
        except:
            print('invalid number')
            continue
    return number
    
                    
            
        