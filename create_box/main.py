"""This is the entry point of the program."""

def create_box(height, width, char):
    if height < 1 or width < 1:
        return 'Invalid dimensions, height and/or width must be at least 1.'
    else:
        return height * (width * char + '\n')

def create_empty_box(height, width, char):
    if height < 1 or width < 1:
        return 'Invalid dimensions, height and/or width must be at least 1.'
    else:
        row_ends = width * char + '\n'
        row_inner = char + (' ' * (width - 2)) + char + '\n'
        return row_ends + row_inner * (height - 2) + row_ends


if __name__ == '__main__':
    create_box(3, 4, '*')
    create_empty_box(5, 5, '$')
