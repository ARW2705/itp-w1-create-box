"""This is the entry point of the program."""

# Original objective

def create_box(height, width, char):
    count = 0
    end_str = ''
    while count < height:
        end_str += char * width + '\n'
        count += 1
    return end_str   


if __name__ == '__main__':
    create_box(3, 4, '*')
