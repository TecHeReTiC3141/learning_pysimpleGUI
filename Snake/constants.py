field_size = 500
cell_num = 10
cell_size = field_size // cell_num

def pos_to_pixel(x, y) -> tuple[tuple, tuple]:
    return (x * cell_size, y * cell_size), \
           ((x + 1) * cell_size, (y + 1) * cell_size)