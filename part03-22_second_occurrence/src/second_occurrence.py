# Write your solution here

def find_second_occurrence(string, substring):
    first_index = string.find(substring)
    if first_index != -1:
        second_index = string.find(substring, first_index + len(substring))
        if second_index != -1:
            return second_index
    return -1

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

second_occurrence_index = find_second_occurrence(string, substring)

if second_occurrence_index != -1:
    print(f"The second occurrence of the substring is at index {second_occurrence_index}.")
else:
    print(f"The substring does not occur twice in the string.")
