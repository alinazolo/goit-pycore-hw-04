from pathlib import Path


def get_cats_info(path):
    try:
        file_path = Path(path)
        cats = []

        if not file_path.exists():
            raise FileNotFoundError



        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                if not line:
                    continue

                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
            return cats

    except FileNotFoundError:
        print("There is no file here")
        return []

    except ValueError:
        print("Error in data format in file")
        return []


cats_info = get_cats_info("./cats_info/cats_file.txt")
print(cats_info)



