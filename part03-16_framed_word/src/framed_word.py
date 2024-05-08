# Write your solution here
def print_frame(word):
    frame_width = 30
    word_width = len(word)
    side_width = (frame_width - word_width - 2) // 2  # Calculate side width

    # Print top frame
    print("*" * frame_width)
    
    # Print middle frame with word
    if word_width % 2 == 0:
       print("*" + " " * side_width + word + " " * side_width + "*")
    elif word_width % 2 != 0:
       print("*" + " " * side_width + word + " " * side_width + " " "*")

    # Print bottom frame
    print("*" * frame_width)

# Get input from the user
user_input = input("Word: ")

# Print the framed word
print_frame(user_input)
