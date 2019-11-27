count = 0
while True:
    print('count-{}'.format(count))
    while True:
        print('count-{}'.format(count))
        if count ==4:
            print('count-{}'.format(count))
            print('going to break inner loop ')
            break
        else:
            count+=1
            print('count-{}'.format(count))
            continue
    print('count-{}'.format(count))
    if count ==7:
        print('count-{}'.format(count))
        print('going to break outer lopp')
        break
    else:
        count +1
        print('count-{}'.format(count))
        continue
    
            
    
    