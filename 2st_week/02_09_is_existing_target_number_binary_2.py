finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    # 이 부분을 채워보세요!
    # 정렬 : 이진탐색하려면 정렬 필수
    array.sort()
    print(array)

    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while(current_min <= current_max):
        if (array[current_guess] == target):
            return True
        elif (array[current_guess] < target):
            current_min = current_guess + 1
        elif (array[current_guess] > target):
            current_max = current_guess - 1
        
        
        current_guess = (current_min + current_max) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)