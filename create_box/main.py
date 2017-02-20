"""This is the entry point of the program."""

def create_box(height, width, char):
    if height < 1 or width < 1:
        return 'Invalid dimensions, height and/or width must be at least 1.'
    else:
        end_str = ''
        for h in range(height):
            end_str += char * width + '\n'
        return end_str

def create_empty_box(height, width, char):
    if height < 1 or width < 1:
        return 'Invalid dimensions, height and/or width must be at least 1.'
    else:
        end_str = ''
        for h in range(height):
            if h == 0 or h == (height - 1):
                end_str += char * width + '\n'
            else:
                end_str += char + (' ' * (width - 2)) + char + '\n'
        return end_str 


if __name__ == '__main__':
    create_box(3, 4, '*')
    create_empty_box(5, 5, '$')
