# Write your solution here
def who_won(game_board: list):
    count_a = 0
    count_b = 0
    for row in game_board:
        for value in row:
            if value == 1:
                count_a += 1
            elif value == 2:
                count_b += 1
    if count_a > count_b:
       return 1
    elif count_b > count_a:
       return 2    
    elif count_a == count_b:
       return 0  
               
if __name__ == "__main__":
   game_board = [[1,0,2],[2,0,0],[1,1,1]]
   who_won(game_board)