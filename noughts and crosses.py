field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
play = True 
count = 0
main_diag, sec_diag, columns = None, None, None


def show_field () -> None:
    if count % 2 == 0:
        print ("Crosses's turn!")
    else: print ("Noughts's turn")
    print (f'   {field[0][0]}  |  {field[0][1]}  |  {field[0][2]} ')
    print ('  ----+-----+----')
    print (f'   {field[1][0]}  |  {field[1][1]}  |  {field[1][2]} ')
    print ('  ----+-----+----')
    print (f'   {field[2][0]}  |  {field[2][1]}  |  {field[2][2]} ')


def check() -> None:
    for j ,i in enumerate(field):
        if (all(map(lambda x: x == 'X', i)) or all(map(lambda x: x == 'O', i))) or (all(map(lambda x: x == 'X', columns[j])) or all(map(lambda x: x == 'O', columns[j]))):
            show_field ()
            print ("GAME OVER!")
            global play
            play = False
    if (all(map(lambda x: x == 'X', main_diag)) or all(map(lambda x: x == 'O', main_diag))) or (all(map(lambda x: x == 'X', sec_diag)) or all(map(lambda x: x == 'O', sec_diag))):
        show_field ()
        print ("GAME OVER!")
        play = False 


def turn () -> int: 
    turn_input = int(input('where do you wanna put? '))
    if turn_input > 9 or turn_input < 0:
        return 'range'
    return turn_input
        
        
def noughts(num) -> None:
    for i, x in enumerate(field):
        for k, y in enumerate(x):
            if y == num and type(y) == int:
                field[i][k] = 'O'
            else:
                global count 
                count -= 1
    
    
def crosses(num) -> None:
    for i, x in enumerate(field):
        for k, y in enumerate(x):
            if y == num and type(y) == int:
                field[i][k]= 'X'            
            else: 
                global count 
                count -= 1


while play:
    show_field()
    a = turn()
    if a == 'range':
        print ('OUT OF RANGE OF FIELD')
        continue
    if count % 2 == 0:
        crosses(a)
    else:
        noughts(a)
    main_diag = [field[i][i] for i in range(3)]            
    sec_diag = [field[i][2 - i] for i in range(3)]         
    columns = [[field[k][i] for k in range(3)] for i in range(3)]
    check ()   
        
    if a == 0:
        play = False
    count += 1
    
    
