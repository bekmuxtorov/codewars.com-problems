# Asadbek Muxtorov
# bekmuxtorov.me

# <========================================> 1-masala <========================================>


def define_status(voters: list, name: str) -> str:
    for voter in voters:
        if voter['name'] == name:
            if voter['is_voted']:
                return "Siz avval ovoz bergansiz."
            else:
                voter.setdefault('is_voted', True)
                return "Siz ovoz berishingiz mumkin."

    voters.append({'name': name, 'is_voted': True})
    return "Siz ro’yxatda yo’q ekansiz. Ro’yxatga qo’shildingiz. Ovoz berishingiz mumkin."


voters = [
    {'name': 'Asadbek', 'is_voted': True},
    {'name': 'Pistonchi', 'is_voted': False},
    {'name': 'Palonchi', 'is_voted': False},
]
name = 'Kimsanboy'


# <========================================> 2-masala <========================================>


def delete_dublicate(data: list) -> list:
    new_list = []
    for data_item in data:
        if not data_item in new_list:
            new_list.append(data_item)
    return new_list


# <========================================> 3-masala <========================================>


def bubble_sort(arr_items: list[int]) -> list[int]:
    for _ in range(len(arr_items) - 1):
        for i in range(len(arr_items) - 1):
            if arr_items[i] > arr_items[i + 1]:
                arr_items[i], arr_items[i + 1] = arr_items[i + 1], arr_items[i]
    return arr_items


def binary_search(arr: list[int], low: int, high: int, x: int):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def main(arr: list[int], search_num: int) -> int:
    sorted_arr = bubble_sort(arr)
    return binary_search(sorted_arr, 0, len(arr)-1, search_num)


# <========================================> 4-masala <========================================>


def is_palindrom(word: str) -> bool:
    word = word.lower()
    for i in range(0, len(word)):
        if word[i] != word[-(i+1)]:
            return False
    return True


# <========================================> 😎 Bajarildi <========================================>
