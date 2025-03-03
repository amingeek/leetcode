def is_prime(n):
    x = 0
    if n <= 1:
        return False
    
    for i in range(1, n + 1):
        if n % i == 0:
            x += 1
    if x == 2:
        return True
    
    return False

def find_path(matrix):
    if not matrix or not matrix[0]:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # شروع از خانه اول
    queue = [(0, 0, matrix[0][0])]
    visited = set()
    
    # جهت‌های حرکت: راست و پایین
    directions = [(0, 1), (1, 0)]
    
    while queue:
        x, y, current_sum = queue.pop(0)
        
        # بررسی رسیدن به مقصد
        if x == rows-1 and y == cols-1:
            return True
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_sum = current_sum + matrix[nx][ny]
                if is_prime(new_sum) and (nx, ny, new_sum) not in visited:
                    visited.add((nx, ny, new_sum))
                    queue.append((nx, ny, new_sum))
    
    return False

matrix = [
    [3, 2, 2],
    [5, 2, 6],
    [4, 4, 2]
]


print(find_path(matrix)) 