import json

def validate_movies(data):
    if not isinstance(data, dict) or set(data) != {"list1", "list2"}:
        raise ValueError
    for movies in data.values():
        if not isinstance(movies, list):
            raise ValueError
        previous_year = None
        for movie in movies:
            if (not isinstance(movie, dict) or set(movie) != {"title", "year"}
                    or not isinstance(movie["title"], str)
                    or isinstance(movie["year"], bool)
                    or not isinstance(movie["year"], int)):
                raise ValueError
            if previous_year is not None and movie["year"] < previous_year:
                raise ValueError
            previous_year = movie["year"]


def merge(first, second):
    result = []
    left = right = 0
    while left < len(first) and right < len(second):
        if first[left]["year"] <= second[right]["year"]:
            result.append(first[left])
            left += 1
        else:
            result.append(second[right])
            right += 1
    return result + first[left:] + second[right:]


def main():
    try:
        with open("input.txt", encoding="utf-8") as source:
            content = source.read()
        if not content.strip():
            print("Empty file")
            return
        data = json.loads(content)
        validate_movies(data)
        result = {"list0": merge(data["list1"], data["list2"])}
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, json.JSONDecodeError, ValueError):
        print("Invalid input")

if __name__ == "__main__":
    main()