### شرح مسئله:
در این مسئله، شما باید لیستی از اعداد را دریافت کنید و عملیات‌های زیر را انجام دهید:

1. برای هر عدد در لیست، جدول ضرب آن عدد را از 1 تا 10 چاپ کنید.
2. سپس بررسی کنید که آیا هر عدد شبه‌اول است یا خیر. یک عدد شبه‌اول عددی است که حاصل ضرب دو عدد اول باشد (مثلاً 6 = 2 * 3).
3. اعداد شبه‌اول را جدا کنید و اعداد غیر شبه‌اول را در لیست دیگری ذخیره کنید.
4. پس از پردازش تمام اعداد، لیست نهایی را به‌گونه‌ای نمایش دهید که ابتدا اعداد شبه‌اول بیایند و سپس اعداد غیر شبه‌اول.

ورودی: یک لیست از اعداد مختلف.
خروجی: نمایش جدول ضرب برای هر عدد، سپس نمایش اعداد شبه‌اول و غیر شبه‌اول و در نهایت یک لیست مرتب‌شده که در آن ابتدا اعداد شبه‌اول آمده باشد.

### کدنمونه گرفته شده از ChatGPT:
*‍‍‍**اگر شباهت زیاد بود نمره صفر لحاظ شود***

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_semiprime(n):
    factors = 0
    for i in range(2, n + 1):
        while n % i == 0 and is_prime(i):
            factors += 1
            n //= i
        if factors > 2:
            return False
    return factors == 2

def print_multiplication_table(n):
    n = abs(n)
    print(f"جدول ضرب برای {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def process_numbers(numbers):
    semiprimes = []
    non_semiprimes = []
    
    for num in numbers:
        print_multiplication_table(num)
        
        if is_semiprime(abs(num)):
            semiprimes.append(num)
        else:
            non_semiprimes.append(num)
    
    print("\nاعداد شبه‌اول:", semiprimes)
    print("اعداد غیر شبه‌اول:", non_semiprimes)
    
    sorted_numbers = semiprimes + non_semiprimes
    print("\nلیست مرتب شده (شبه‌اول‌ها اول):", sorted_numbers)

numbers = [-2, 3, 5, 10, 15, 6, 7, 8]
process_numbers(numbers)

```


### کدنمونه حرفه ای:
‍‍‍
```python
TABLE_SIZE = 10

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

def is_semiprime(n, prime_sieve):
    n = abs(n)
    prime_factors = 0
    i = 2
    while i * i <= n and i < len(prime_sieve):
        while n % i == 0 and prime_sieve[i]:
            prime_factors += 1
            n //= i
        i += 1
    if n > 1 and n < len(prime_sieve) and prime_sieve[n]:
        prime_factors += 1
    return prime_factors == 2

def print_multiplication_table(n):
    n = abs(n)
    print(f"جدول ضرب برای {n}:")
    for i in range(1, TABLE_SIZE + 1):
        print(f"{n} × {i} = {n * i}")

def process_numbers(numbers):
    if not isinstance(numbers, (list, tuple)) or not numbers:
        raise ValueError("ورودی باید لیست یا تاپل غیرخالی باشد")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("همه عناصر باید عدد باشند")

    max_num = max(abs(num) for num in numbers)
    prime_sieve = sieve(max_num)

    semiprimes = []
    non_semiprimes = []
    for num in numbers:
        print_multiplication_table(num)
        if is_semiprime(num, prime_sieve):
            semiprimes.append(num)
        else:
            non_semiprimes.append(num)

    print("\nاعداد شبه‌اول:", semiprimes)
    print("اعداد غیر شبه‌اول:", non_semiprimes)
    print("\nلیست مرتب شده (شبه‌اول‌ها اول):", semiprimes + non_semiprimes)

numbers = [-2, 3, 5, 10, 15, 6, 7, 8]
process_numbers(numbers)

```


### امتیاز دهی: 100 نمره
- کد اصلی برای [هوش مصنوعی Grok](www.grok.com) ارسال کرده و از آن بخواهید مبنای اصلی این کدرا قرار دهد و بر اساس ملاک های تعیین شده در فایل Code evaluation criteria کد های متقاضیان را امتیاز دهی کند.