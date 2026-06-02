def find_duplicates(arr):
    seen = set()
    duplicates = []
    for item in arr:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates


if __name__ == "__main__":
    sample = [1, 2, 3, 2, 4, 5, 3, 6, 1]
    print("Array:", sample)
    print("Duplicates:", find_duplicates(sample))
