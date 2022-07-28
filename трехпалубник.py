third_paluba = perm[randint(0, len(perm) - 1)]

if third_paluba == 'top':
    ship_row2 = ship_row - 2
    ship_col2 = ship_col - 1
if third_paluba == 'bot':
    ship_row2 = ship_row + 2
    ship_col2 = ship_col + 1
if third_paluba == 'left':
    ship_row2 = ship_row - 1
    ship_col2 = ship_col - 2
if third_paluba == 'right':
    ship_row2 = ship_row + 1
    ship_col2 = ship_col + 2
