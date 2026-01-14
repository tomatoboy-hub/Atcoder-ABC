

def normalized(pieces):
    if not pieces:
        return []
    min_r = min(r for r,c in pieces)
    min_c = min(c for r,c in pieces)
    return [(r - min_r, c - min_c) for r,c in pieces]
    

def rotate(pieces):
    rotated_shape = [(c, -r) for r,c in pieces]
    return normalized(rotated_shape)

def solve():
    first_empty = None
    for r_idx in range(N):
        for c_idx in range(N):
            if board[r_idx][c_idx] == 0:
                first_empty = (r_idx, c_idx)
    if first_empty is None:
        return True
    
    r,c = first_empty
    for i in range(M):
        if not used_pieces[i]:
            for shape in pieces[i]:
                for block_r, block_c in shape:
                    start_r, start_c = r - block_r, c - block_c

                    can_place = True
                    placement_coords = []
                    for dr, dc in shape:
                        cur_r, cur_c = start_r + dr, start_c + dc
                        if not (0 <= cur_r < N and 0 <= cur_c < N and board[cur_r][cur_c] == 0):
                            can_place = False
                            break
                        placement_coords.append((cur_r, cur_c))
                    if can_place:
                        used_pieces[i] = True
                        for pr,pc in placement_coords:
                            board[pr][pc] = i + 1
                        if solve():
                            return True
                        used_pieces[i] = False
                        for pr,pc in placement_coords:
                            board[pr][pc] = 0
    return False


if __name__ == "__main__":
    N,M = map(int,input().split())
    pieces = [[] for _ in range(M)]
    used_pieces = [] * M
    board = [[0] * N for _ in range(N)]
    total_area = 0
    for k in range(M):
        current_piece = []
        for r in range(N):
            row_col = input()
            for c, char in enumerate(row_col):
                if char == "#":
                    current_piece.append((r,c))
        
        total_area += len(current_piece)
        if not current_piece:
            continue

        normalized_piece = normalized(current_piece)
        unique_rotations = set()

        temp_piece = normalized_piece
        for _ in range(4):
            shape_as_tuple = tuple(temp_piece)
            if shape_as_tuple not in unique_rotations:
                unique_rotations.add(shape_as_tuple)
                pieces[k].append(temp_piece)
            temp_piece = rotate(temp_piece)

