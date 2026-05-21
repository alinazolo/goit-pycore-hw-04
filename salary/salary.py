from pathlib import Path


def total_salary(path):
    try:
        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError

        total = 0
        count = 0

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, salary = line.split(",")
                salary = int(salary)

                total += salary
                count += 1

        if count == 0:
            return 0, 0

        average = total / count
        return total, average

    except FileNotFoundError:
        print("There is no file here")
        return 0, 0

    except ValueError:
        print("Error in data format in file")
        return 0, 0


total, average = total_salary("./salary/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


