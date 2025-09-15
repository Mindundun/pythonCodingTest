input = 20

# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다.
def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    arr = []
    # 방법 1 (for-else) 
    # for n in range(2, number + 1): # 2 ~ number까지 반복     
    #     for i in range(2, n):
    #         if( n % i == 0 ):
    #             break
    #     else:
    #         arr.append(n)  
             
    # return arr
    # => 이 방법은 2 ~ 해당 수까지 n % i 계산을 하기에 비효율적임.
    # => 왜냐, 2와 3으로 나눠떨어지지않는 경우 4, 6, 8, 10 ... 과 같이 배수의 경우도 나누어 떨어지지 않기 때문
    # => 소수들만 비교하면 된다.
    

    # 방법 2
    # for n in range(2, number + 1): # 2 ~ number까지 반복     
    #     for i in arr:
    #         if( n % i == 0 ):
    #             break
    #     else:
    #         arr.append(n)  
             
    # return arr

    # 방법 3 : N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
    # i * i <= n
    for n in range(2, number + 1):
        for i in arr:
            if i * i <= n and n % i == 0:
                break
        else:
            arr.append(n)

    return arr
result = find_prime_list_under_number(input)
print(result)