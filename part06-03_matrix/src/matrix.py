# write your solution here
def matrix_sum():
    with open ("matrix.txt") as file:
        numbers = []
        for line in file:
            line = line.replace("\n", "")
            items = line.split(",")
            
            #numbers = [int(item) foritem in items]
            for item in items:
                numbers.append(int(item))
            
    return sum(numbers)   

def matrix_max():
    with open ("matrix.txt") as file:
        numbers = []
        for line in file:
            line = line.replace("\n", "")
            items = line.split(",")
            
            #numbers = [int(item) for item in items]
            for item in items:
                numbers.append(int(item))
    return max(numbers)


def row_sums(): 
    with open ("matrix.txt") as file:
        sum_list = []
        for line in file:
            line = line.replace("\n", "")
            items = line.split(",")  
            sum = 0
            for item in items:
                item = int(item)
                sum += item
            sum_list.append(sum)
    
    return sum_list  

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
          

                

