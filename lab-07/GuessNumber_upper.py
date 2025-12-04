from random import randint 
N =randint (0 ,99 )
COUNT =0 


while True :
    S =input ("输入一个整数(0-99): ")
    try :
        N =int (S )
    except ValueError :
        print ("你输入了非整型数")
        continue 

    COUNT +=1 
    if N >N :
        print ("遗憾，太大了")
    elif N <N :
        print ("遗憾，太小了")
    else :
        print (f"猜了{COUNT }次，你猜中了!")
        break 
