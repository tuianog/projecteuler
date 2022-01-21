
def build_multi_dimensional_matrix(l,c):
    matrix = [[0 for j in range(c)] for i in range(l)]
    return matrix

def make_move(matrix, l, c, stop_position, path=''):
    if l == stop_position[0] and c == stop_position[1]:
        #print('Found', path)
        return 1
    
    counter = 0
    # move right
    if c+1 <= stop_position[1]:
        counter_right = make_move(matrix=matrix, l=l, c=c+1, stop_position=stop_position, path=f'{path} right')
        counter += counter_right
    # move down
    if l+1 <= stop_position[0]:
        counter_down = make_move(matrix=matrix, l=l+1, c=c, stop_position=stop_position, path=f'{path} down')
        counter += counter_down    

    return counter

mappings = []

def make_move_dynamic(matrix, l, c, stop_position, path=''):
    if mappings[l][c]:
        return mappings[l][c]
    
    if l == stop_position[0] and c == stop_position[1]:
        #print('Found', path)
        return 1
    
    counter = 0
    # move right
    if c+1 <= stop_position[1]:
        counter_right = make_move_dynamic(matrix=matrix, l=l, c=c+1, stop_position=stop_position, path=f'{path} right')
        counter += counter_right
    
    # move down
    if l+1 <= stop_position[0]:
        counter_down = make_move_dynamic(matrix=matrix, l=l+1, c=c, stop_position=stop_position, path=f'{path} down')
        counter += counter_down    

    mappings[l][c] = counter
    return counter

if __name__ == "__main__":
    for i in range(2, 22):
        mappings = build_multi_dimensional_matrix(i, i)
        matrix = build_multi_dimensional_matrix(i, i)
        c = make_move_dynamic(matrix=matrix, l=0, c=0, stop_position=(i-1, i-1))
        print(i, c)
