# write your solution here
#def largest():
    # Open the file for reading
def largest():
    with open("numbers.txt") as file: # Read all lines
        numbers = []  # Initialize list to store numbers
        
        numbers = [int(line.replace("\n", "")) for line in file]
        # Iterate over each line in the content
        #for line in content:
        #    number_str = line.strip()  # Remove leading/trailing whitespace
         #   number = int(number_str)  # Convert string to integer
         #   numbers.append(number)  # Append number to list
              # Ignore lines that can't be converted to integers
        
        return(max(numbers))

        
    # Convert each line to an integer and store in a list
    #numbers = [int(line.strip()) for line in lines]

        
        # Return the largest number
        #return max(numbers)

if __name__ == "__main__":
    print(largest())
    