import statistics

def calculate_class_grades():
    try:
        n = int(input("تعداد دانش‌آموزان کلاس را وارد کنید: "))
        if n <= 0:
            raise ValueError("تعداد دانش‌آموزان باید مثبت باشد")

        total = 0
        students = []
        excellent = 0
        good = 0
        weak = 0

        for i in range(n):
            name = input(f"نام دانش‌آموز {i+1}: ").strip()
            if not name:
                raise ValueError("نام نمی‌تواند خالی باشد")
            student_id = input(f"شماره دانش‌آموزی {name}: ").strip()
            if not student_id:
                raise ValueError("شماره دانش‌آموزی نمی‌تواند خالی باشد")
            grade = float(input(f"معدل دانش‌آموز {name} (0-20): "))
            if not 0 <= grade <= 20:
                raise ValueError(f"معدل {grade} خارج از محدوده 0 تا 20 است")
            
            students.append({"name": name, "id": student_id, "grade": grade})
            total += grade

            if grade >= 17:
                excellent += 1
            elif grade >= 14:
                good += 1
            else:
                weak += 1

        grades = [s["grade"] for s in students]
        average = total / n
        max_grade = max(grades)
        min_grade = min(grades)
        std_dev = statistics.stdev(grades) if n > 1 else 0

        sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)

        print("\n--- گزارش معدل کلاس ---")
        print(f"تعداد دانش‌آموزان: {n}")
        print(f"میانگین معدل: {average:.2f}")
        print(f"بالاترین معدل: {max_grade:.2f}")
        print(f"پایین‌ترین معدل: {min_grade:.2f}")
        print(f"انحراف معیار معدل‌ها: {std_dev:.2f}")
        print("\nدسته‌بندی دانش‌آموزان:")
        print(f"عالی (معدل ≥ 17): {excellent} نفر ({excellent/n*100:.1f}%)")
        print(f"خوب (14 ≤ معدل < 17): {good} نفر ({good/n*100:.1f}%)")
        print(f"ضعیف (معدل < 14): {weak} نفر ({weak/n*100:.1f}%)")
        print("\nلیست دانش‌آموزان (مرتب‌شده بر اساس معدل):")
        for s in sorted_students:
            print(f"{s['name']} (ID: {s['id']}): {s['grade']:.2f}")

        save = input("\nآیا می‌خواهید نتایج را در فایل ذخیره کنید؟ (بله/خیر): ").strip().lower()
        while save not in ["بله", "خیر"]:
            print("لطفاً 'بله' یا 'خیر' وارد کنید.")
            save = input("آیا می‌خواهید نتایج را در فایل ذخیره کنید؟ (بله/خیر): ").strip().lower()
        
        if save == "بله":
            with open("class_grades_report.txt", "w", encoding="utf-8") as f:
                f.write("گزارش معدل کلاس\n")
                f.write("=" * 20 + "\n")
                f.write(f"تعداد دانش‌آموزان: {n}\n")
                f.write(f"میانگین معدل: {average:.2f}\n")
                f.write(f"بالاترین معدل: {max_grade:.2f}\n")
                f.write(f"پایین‌ترین معدل: {min_grade:.2f}\n")
                f.write(f"انحراف معیار معدل‌ها: {std_dev:.2f}\n")
                f.write("\nدسته‌بندی دانش‌آموزان:\n")
                f.write(f"عالی (معدل ≥ 17): {excellent} نفر ({excellent/n*100:.1f}%)\n")
                f.write(f"خوب (14 ≤ معدل < 17): {good} نفر ({good/n*100:.1f}%)\n")
                f.write(f"ضعیف (معدل < 14): {weak} نفر ({weak/n*100:.1f}%)\n")
                f.write("\nلیست دانش‌آموزان (مرتب‌شده بر اساس معدل):\n")
                for s in sorted_students:
                    f.write(f"{s['name']} (ID: {s['id']}): {s['grade']:.2f}\n")
            print("نتایج در فایل 'class_grades_report.txt' ذخیره شد.")

    except ValueError as e:
        print(f"خطا: {e}")
    except Exception as e:
        print(f"خطای غیرمنتظره: {e}")

while True:
    calculate_class_grades()
    again = input("\nآیا می‌خواهید دوباره اجرا کنید؟ (بله/خیر): ").strip().lower()
    while again not in ["بله", "خیر"]:
        print("لطفاً 'بله' یا 'خیر' وارد کنید.")
        again = input("آیا می‌خواهید دوباره اجرا کنید؟ (بله/خیر): ").strip().lower()
    if again == "خیر":
        print("برنامه پایان یافت.")
        break