import random
 

guide = '''
KEY       CHOICE       GESTURE
 
 R         Rock          ✊
 P         Paper         🖐️
 S        Scissors       ✌️ 
'''

print (guide)
option = ['r', 'p', 's']
character = ['✊', '🖐️', '✌️']


def game():
    player1 = ''
    player2 = random.choice(option)
    player1 = input('Enter Key = ').lower() 
    
    #when a wrong command is inputed
    while player1 not in option:   
        if True:
            print ('error: Key not recognized')
            player1 = input('Enter Key = ').lower() 
            
    
    # When a tie occurs 
    
    while player1 == player2:
        if True:
            if player1 and player2 == 'r' :
                print(f'Player({character[0]} ) : CPU({character[0]} )')
                print("It's a tie!!")
                player1 = input('Enter Key = ').lower() 
                player2 = random.choice(option)
                
            if player1 and player2 == 'p':
                print(f'Player({character[1]} ) : CPU({character[1]} )')
                print("It's a tie!!")
                player1 = input('Enter Key = ').lower() 
                player2 = random.choice(option)
            # continue   

            if player1 and player2 == 's':
                print(f'Player({character[2]} ) : CPU({character[2]} )')     
                print("It's a tie!!")
                player1 = input('Enter Key = ').lower() 
                player2 = random.choice(option)
   
    
    #conditions
    if player1 =='r':
        if player2 == 'p':
            print(f'Player({character[0]} ) : CPU({character[1]} )')
            print ('You Lose!!!')
            
        if player2 == 's':
            print(f'Player({character[0]} ) : CPU({character[2]} )')
            print('You Win!!!')

    elif player1 =='p':
        if player2 == 's':
            print(f'Player({character[1]} ) : CPU({character[2]} )')
            print ('You Lose!!!')
        if player2 == 'r':
            print(f'Player({character[1]} ) : CPU({character[0]} )')
            print('You Win!!!')

    elif player1 =='s':
        if player2 == 'p':
            print(f'Player({character[2]} ) : CPU({character[1]} )')
            print ('You Win!!!')
        if player2 == 'r':
            print(f'Player({character[2]} ) : CPU({character[0]} )')
            print('You Lose!!!')


game()  
       
      

                
            
        
        
    




