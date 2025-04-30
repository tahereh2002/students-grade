try:
    # دریافت تعداد دانش‌آموزان
    n = int(input("تعداد دانش‌آموزان کلاس را وارد کنید: "))
    if n <= 0:
        raise ValueError("تعداد دانش‌آموزان باید مثبت باشد")

    # متغیرها برای ذخیره معدل‌ها و آمار
    total = 0
    grades = []
    excellent = 0  # معدل بالای 17
    good = 0       # معدل بین 14 تا 17
    weak = 0       # معدل زیر 14

    # دریافت معدل‌ها
    for i in range(n):
        grade = float(input(f"معدل دانش‌آموز {i+1} (0-20): "))
        if not 0 <= grade <= 20:
            raise ValueError(f"معدل {grade} خارج از محدوده 0 تا 20 است")
        grades.append(grade)
        total += grade

        # دسته‌بندی دانش‌آموزان
        if grade >= 17:
            excellent += 1
        elif grade >= 14:
            good += 1
        else:
            weak += 1

    # محاسبه میانگین، بالاترین و پایین‌ترین معدل
    average = total / n
    max_grade = max(grades)
    min_grade = min(grades)

    # نمایش نتایج
    print("\n--- گزارش معدل کلاس ---")
    print(f"میانگین معدل: {average:.2f}")
    print(f"بالاترین معدل: {max_grade:.2f}")
    print(f"پایین‌ترین معدل: {min_grade:.2f}")
    print("\nدسته‌بندی دانش‌آموزان:")
    print(f"عالی (معدل ≥ 17): {excellent} نفر")
    print(f"خوب (14 ≤ معدل < 17): {good} نفر")
    print(f"ضعیف (معدل < 14): {weak} نفر")

    # ذخیره نتایج در فایل
    save = input("\nآیا می‌خواهید نتایج را در فایل ذخیره کنید؟ (بله/خیر): ").strip().lower()
    if save == "بله":
        with open("class_grades_report.txt", "w", encoding="utf-8") as f:
            f.write("گزارش معدل کلاس\n")
            f.write("=" * 20 + "\n")
            f.write(f"تعداد دانش‌آموزان: {n}\n")
            f.write(f"میانگین معدل: {average:.2f}\n")
            f.write(f"بالاترین معدل: {max_grade:.2f}\n")
            f.write(f"پایین‌ترین معدل: {min_grade:.2f}\n")
            f.write("\nدسته‌بندی دانش‌آموزان:\n")
            f.write(f"عالی (معدل ≥ 17): {excellent} نفر\n")
            f.write(f"خوب (14 ≤ معدل < 17): {good} نفر\n")
            f.write(f"ضعیف (معدل < 14): {weak} نفر\n")
        print("نتایج در فایل 'class_grades_report.txt' ذخیره شد.")

except ValueError as e:
    print(f"خطا: {e}")
except Exception as e:
    print(f"خطای غیرمنتظره: {e}")ز