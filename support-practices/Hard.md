### مسئله:
- یک ماتریس n × n از اعداد صحیح مثبت داده شده است. شما در خانه‌ی بالا-چپ (0,0) قرار دارید و می‌خواهید به خانه‌ی پایین-راست (n-1,n-1) برسید. می‌توانید فقط به راست یا پایین حرکت کنید. اما یک شرط مهم وجود دارد:

در هر مرحله، مجموع مقادیر خانه‌هایی که از روی آن‌ها عبور کرده‌اید، باید یک عدد اول باشد.

#### 🔹 ورودی:
یک ماتریس n × n شامل اعداد صحیح مثبت (1 ≤ n ≤ 100 و 1 ≤ مقدار هر خانه ≤ 100).
#### 🔹 خروجی:
True اگر مسیر معتبری وجود دارد که شرایط را رعایت کند.
False در غیر این صورت.


### کد نمونه گرفته شده از ChatGPT:

*‍‍‍**اگر شباهت زیاد بود نمره صفر لحاظ شود***


```python
from functools import lru_cache

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

def find_prime_path(matrix):
    n = len(matrix)
    max_sum = sum(sum(row) for row in matrix)
    prime_check = sieve(max_sum)

    @lru_cache(None)
    def dfs(x, y, total):
        if x >= n or y >= n or not prime_check[total]:
            return False
        if x == n - 1 and y == n - 1:
            return True

        return dfs(x + 1, y, total + matrix[x][y]) or dfs(x, y + 1, total + matrix[x][y])

    return dfs(0, 0, 0)

matrix = [
    [3, 7, 2],
    [5, 1, 6],
    [4, 9, 8]
]

print(find_prime_path(matrix))

```

‍‍‍
```python
from collections import deque

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

def find_prime_path_bfs(matrix):
    n = len(matrix)
    max_sum = sum(sum(row) for row in matrix)
    prime_check = sieve(max_sum)

    queue = deque([(0, 0, matrix[0][0])])
    visited = set()

    while queue:
        x, y, total = queue.popleft()
        
        if (x, y) == (n - 1, n - 1):
            return True

        for dx, dy in [(1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx < n and ny < n:
                new_sum = total + matrix[nx][ny]
                if prime_check[new_sum] and (nx, ny, new_sum) not in visited:
                    visited.add((nx, ny, new_sum))
                    queue.append((nx, ny, new_sum))

    return False


matrix = [
    [3, 7, 2],
    [5, 1, 6],
    [4, 9, 8]
]

print(find_prime_path_bfs(matrix))
```



### کدحرفه ای:

```python
from collections import defaultdict

# جهت‌های حرکت به صورت ثابت
DIRECTIONS = [(1, 0), (0, 1)]  # Down, Right

def sieve(limit):
    """تولید اعداد اول تا سقف مشخص شده با روش غربال"""
    if limit < 2:
        return [False] * (limit + 1)
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

def find_prime_path_dp(matrix):
    """پیدا کردن مسیری که در آن مجموع همه اعداد اول هستند"""
    # چک ورودی
    if not matrix or not matrix[0]:
        return False
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        return False  # ماتریس باید مربعی باشه
    if any(not isinstance(val, int) or val <= 0 for row in matrix for val in row):
        return False  # همه مقادیر باید مثبت باشن

    # حداکثر مجموع ممکن
    max_sum = sum(sum(row) for row in matrix)
    prime_check = sieve(max_sum)  # پیش‌محاسبه اعداد اول

    # DP با استفاده از دیکشنری برای حالت‌ها: (x, y, total) -> آیا ممکنه
    dp = defaultdict(lambda: False)
    dp[(0, 0, matrix[0][0])] = prime_check[matrix[0][0]]  # نقطه شروع

    # پر کردن جدول DP
    for x in range(n):
        for y in range(n):
            for total in range(max_sum + 1):
                if not dp[(x, y, total)]:
                    continue
                # بررسی حرکت به راست و پایین
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if nx < n and ny < n:
                        new_sum = total + matrix[nx][ny]
                        if new_sum <= max_sum and prime_check[new_sum]:
                            dp[(nx, ny, new_sum)] = True

    # بررسی مقصد
    for total in range(max_sum + 1):
        if dp[(n - 1, n - 1, total)]:
            return True
    return False

# مثال ورودی
matrix = [
    [3, 7, 2],
    [5, 1, 6],
    [4, 9, 8]
]

print(find_prime_path_dp(matrix))  # خروجی: True یا False

```


### امتیاز دهی: 100 نمره
- کد اصلی برای [هوش مصنوعی Grok](www.grok.com) ارسال کرده و از آن بخواهید مبنای اصلی این کدرا قرار دهد و بر اساس ملاک های تعیین شده در فایل Code evaluation criteria کد های متقاضیان را امتیاز دهی کند.