### ملاک‌های ارزیابی کد (مجموع: ۱۰۰ نمره)

1. صحت عملکرد (Correctness) - ۳۰ نمره  
   - آیا کد مسئله رو درست حل می‌کنه و خروجی مورد انتظار رو می‌ده؟  
   - وجود باگ، خطا در منطق یا عدم تطابق با خواسته‌های مسئله باعث کسر نمره می‌شه.  
   - مثال: اگه خروجی همیشه False برگردونه وقتی باید True باشه، نمره کم می‌شه.

2. بهینه‌سازی (Optimization) - ۲۵ نمره  
   - آیا کد از نظر پیچیدگی زمانی و فضایی بهینه‌ست؟  
   - استفاده از الگوریتم‌ها یا ساختارهای غیرضروری و ناکارآمد (مثل حلقه‌های اضافی) نمره کم می‌کنه.  
   - مثال: استفاده از جستجوی خطی به جای باینری سرچ توی یه آرایه مرتب، نمره رو کاهش می‌ده.

3. خوانایی و ساختار (Readability & Structure) - ۲۰ نمره  
   - آیا کد تمیز، مرتب و قابل فهمه؟  
   - نام‌گذاری معنی‌دار متغیرها، کامنت‌های مفید، فاصله‌گذاری مناسب و ماژولاریتی (تقسیم به توابع) بررسی می‌شه.  
   - مثال: اگه متغیرها اسمای گنگ مثل a و b داشته باشن یا کد یه بلوک بزرگ بدون تابع باشه، نمره کم می‌شه.

4. رعایت اصول برنامه‌نویسی (Coding Principles) - ۱۵ نمره  
   - آیا از بهترین شیوه‌ها مثل DRY (عدم تکرار)، ماژولاریتی، یا اصول طراحی (مثل SOLID اگه مرتبط باشه) پیروی شده؟  
   - کدهای تکراری یا ساختارهای پیچیده غیرضروری نمره رو پایین می‌بره.  
   - مثال: اگه یه تابع ۵ بار کپی‌پست شده باشه به جای اینکه یه بار تعریف بشه، نمره کم می‌شه.

5. مدیریت خطا (Error Handling) - ۱۰ نمره  
   - آیا کد برای ورودی‌های نامعتبر یا شرایط خاص پیش‌بینی‌هایی داره؟  
   - عدم چک ورودی یا بی‌توجهی به خطاهای احتمالی (مثل تقسیم بر صفر) باعث کسر نمره می‌شه.  
   - مثال: اگه کد فرض کنه ورودی همیشه valide و هیچ شرطی برای خالی بودن لیست نذاره، نمره کم می‌گیره.