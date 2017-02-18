"""This is the entry point of the program."""

# Original objective

def create_box(height, width, char):
    if height < 1 or width < 1:
        return 'Invalid dimensions, height and/or width must be at least equal to 1.'
    count = 0
    end_str = '\n'
    while count < height:
        if count == 0 or count == height - 1:
            end_str += char * width + '\n'
            count += 1
        else:
            end_str += char + (' ' * (width - 2)) + char + '\n'
            count += 1
    print end_str        
    return end_str


if __name__ == '__main__':
    create_box(5, 5, '*')
