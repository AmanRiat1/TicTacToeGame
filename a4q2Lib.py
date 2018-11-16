def eraseTable (tab):
   '''
   (list) -> None
   This function prepares the game table (array) 
   by putting '-' in all the elements.
   It does not create a new array
   Preconditions: tab is a reference to an nxn array matrice n x n that contains '-', 'X' or 'O'
   '''
      
   tab = [['-','-','-'],['-','-','-'],['-','-','-']]
      
    # to complete
    
    # returns nothing

      
def verifyWin(tab):  
    '''(list) ->  bool
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    * Verify if there is a winner.
    * Look for 3 X's and O's in a row, column, and diagonal.
    * If we find one, we display the winner (the message "Player X has won" 
    * or "Player O has won!") and returns True.
    * If there is a draw (verify it with the function testdraw),
    * display "It is a draw" and returns True.
    * If the game is not over, returns False.
    * The function call the functions testrows, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Those functions returns the winner 'X' or 'O', or '-' if there is no winner.
    '''
    w = testDraw(tab)
    x = testLignes(tab)
    y = testCols(tab)
    z = testDiags(tab)
    if (x or y or z) == 'X':
       print ("Player X has won")
       return True 
    elif (x or y or z) == 'O':
       print ("Player O has won")
       return True
    elif (w) == '-':
       print ("It is a draw")
    else:
       return False

 
def testLignes(tab):
    '''
    * verify if there is a winning row.
    * Look for three 'X' or three 'O' in a row.  
    * If they are found, the character 'X' or 'O' is returned, otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''
    
    y = '-'
    for x in range(len(tab)):
        if tab[x][0] == tab[x][1]:
            if tab[x][1] == tab[x][2]:
                y = tab[x][0]

  
               
    return y # to be modified so that it returns the winner, or '-' if there is no winner  

def testCols(tab):
   '''(list) ->  str
   * verify a winning column.
   * look for three 'X' or three 'O' in a column.  
   * If it is the case the character 'X' or 'O' is returned, otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
       
   i = 0

   for j in range(len(tab)):
       if tab[i][j] == tab[i+1][j]:
           if tab[i+1][j] == tab[i+2][j]:
               return tab[i][j]
           else:
               return "-"
   
def testDiags(tab):
   ''' (list) ->  str
   * Look for three 'X' or three 'O' in a diagonal.  
   * If it is the case, the character 'X' or 'O' is returned
   * otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   z = '-'
   if tab[0][0] == tab[1][1]:
      if tab[1][1] == tab[2][2]:
         z = tab[2][2]
   elif tab[0][2] == tab[1][1]:
      if tab[1][1] == tab[2][0]:
         z = tab[2][0]
   # to complete
    
   return z  # #to be modified so that it returns the winner, or '-' if there is no winner

  
  
def testDraw(tab):
   ''' (list) ->  bool
   * verify if there is a draw
   * check if all the array elements have X or O, not '-'.  
   * If we do not find find any '-' in the array, return True. 
   * If there is any '-', return false.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   ''' 
   z = True
   q = 0
   while z == True:
      if q <= 2:
         for y in tab[q]:
            if y == 'X' or y == 'O':
               z = True
            else:
               z = False
               return False
         q += 1
      else:
         return True 

   # to complete
   return z
   #return False  # to BE modiffied

x =[['X','O','X'],['O','X','O'],['X','X','X']]
print (testDraw(x))

