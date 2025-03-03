### مسئله:

استفاده از NumPy در برنامه پایتون  

در برنامه پایتونی ما، قصد داریم از NumPy استفاده کنیم. متدهای مورد استفاده در این برنامه شامل: mean (میانگین)، max (بیشترین مقدار)، min (کمترین مقدار) و sort (مرتب‌سازی) هستند.  

کد ما دارای ۴ متد است که هرکدام وظیفه خاصی را انجام می‌دهند:  

1. Method1(shape) – تحلیل و تغییر شکل آرایه  
   این متد ابتدا ویژگی‌های آماری آرایه (میانگین، بیشترین مقدار، کمترین مقدار و اندازه) را محاسبه می‌کند. سپس آرایه را بر اساس شکل ورودی تغییر داده و مقادیر آن را نرمالایز می‌کند. در نهایت، نسخه‌ی فلت (یک‌بعدی) آرایه را بازمی‌گرداند.  

2. Method2() – پردازش داده و اعمال تابع ورودی  
   این متد ابتدا آرایه را مرتب می‌کند، سپس مقدارهای آن را نرمالایز کرده و ترتیبشان را معکوس می‌کند. در نهایت، تابعی که کاربر داده را روی آرایه پردازش‌شده اعمال می‌کند و خروجی را برمی‌گرداند.  

3. Method3() – تحلیل عمیق و استخراج اطلاعات مهم  
   این متد ابتدا اعداد اول موجود در آرایه را جدا می‌کند. سپس آرایه را نرمالایز کرده و در نهایت تابع ورودی را روی داده پردازش‌شده اجرا کرده و نتیجه را برمی‌گرداند.  

4. Method4() – مقیاس‌بندی داده‌ها بین ۰ و ۱  
   این متد مقدارهای آرایه را در بازه ۰ تا ۱ تغییر می‌دهد تا مقایسه آن‌ها آسان‌تر شود. اگر تمام مقدارهای آرایه یکسان باشند، بدون تغییر باقی می‌مانند.  

تذکر: نام متدها و متغیرها بسته به سلیقه و خواست خودتان تنظیم شود.  

مشکل اصلی  
ممکن است در آینده توسعه‌دهندگان قصد استفاده از ماژول دیگری داشته باشند و یا بعضی از متدهای موجود در ماژول NumPy مورد ویرایش قرار گیرند.  

راهکار شما برای حل این مشکل چیست؟
آنرا به صورت کدی پایتونی در بیاورید


### کد نمونه حرفه ای:

```python
from abc import ABC, abstractmethod
import numpy as np

# رابط برای عملیات آرایه
class ArrayProcessor(ABC):
    @abstractmethod
    def mean(self, arr):
        pass

    @abstractmethod
    def max(self, arr):
        pass

    @abstractmethod
    def min(self, arr):
        pass

    @abstractmethod
    def sort(self, arr):
        pass

    @abstractmethod
    def reshape(self, arr, shape):
        pass

    @abstractmethod
    def flatten(self, arr):
        pass

# پیاده‌سازی با NumPy
class NumPyProcessor(ArrayProcessor):
    def mean(self, arr):
        return np.mean(arr)

    def max(self, arr):
        return np.max(arr)

    def min(self, arr):
        return np.min(arr)

    def sort(self, arr):
        return np.sort(arr)

    def reshape(self, arr, shape):
        return np.reshape(arr, shape)

    def flatten(self, arr):
        return np.ravel(arr)

# کلاس اصلی با وابستگی به رابط
class ArrayAdapter:
    def init(self, array, processor: ArrayProcessor):
        if not array or not isinstance(array, (list, tuple)):
            raise ValueError("Input must be a non-empty list or tuple")
        self.array = array
        self.processor = processor

    def mean(self):
        return self.processor.mean(self.array)

    def max(self):
        return self.processor.max(self.array)

    def min(self):
        return self.processor.min(self.array)

    def sort(self):
        return self.processor.sort(self.array)

    def normalize(self):
        min_val = self.min()
        max_val = self.max()
        if max_val == min_val:
            return self.array
        return [(x - min_val) / (max_val - min_val) for x in self.array]

    def analyze_and_transform(self, shape):
        stats = {
            "mean": self.mean(),
            "max": self.max(),
            "min": self.min(),
            "size": len(self.array)
        }
        reshaped = self.processor.reshape(self.array, shape)
        normalized = self.normalize()
        flattened = self.processor.flatten(reshaped)
        return {"stats": stats, "reshaped": reshaped, "normalized": normalized, "flattened": flattened}

    def process_and_apply(self, func):
        sorted_arr = self.sort()
        normalized = self.normalize()
        reversed_arr = sorted_arr[::-1]
        processed = func(sorted_arr)
        return {"sorted": sorted_arr, "normalized": normalized, "reversed": reversed_arr, "processed": processed}

    def deep_analysis(self, func):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        primes = [x for x in self.array if is_prime(x)]
        normalized = self.normalize()
        processed = func(self.array)
        return {"primes": primes, "normalized": normalized, "processed": processed}

# مثال استفاده
data = ArrayAdapter([1, 2, 3, 4, 5, 6, 7, 8, 9], NumPyProcessor())
print(data.analyze_and_transform((3, 3)))
print(data.process_and_apply(lambda x: sum(x)))
print(data.deep_analysis(lambda x: sum(x)))
```



### امتیاز دهی: 100 نمره
- کد اصلی برای [هوش مصنوعی Grok](www.grok.com) ارسال کرده و از آن بخواهید مبنای اصلی این کدرا قرار دهد و بر اساس ملاک های تعیین شده در فایل Code evaluation criteria کد های متقاضیان را امتیاز دهی کند.