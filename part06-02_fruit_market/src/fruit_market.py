# write your solution here
#Please write a function named read_fruits, which reads the file and returns a dictionary 
# based on the contents. In the dictionary, the name of the fruit should be the key, and the 
# value should be its price. Prices should be of type float.
def read_fruits():
    fruit_dict = {}
    with open("fruits.csv") as file:
        for line in file:
            fruit, price = line.strip().split(";")
            fruit_dict[fruit] = float(price)
    return fruit_dict    

if __name__ == "__main__":
    print(read_fruits())