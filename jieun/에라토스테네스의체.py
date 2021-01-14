def prime_list_ver1(n):
    # 리스트 초기화 (전부 소수로 간주)
    sieve = [True] * n
    # n의 최대약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True: # i 가 소수인 경우
            # i 이후의 i의 배수를 모두 False로 판정
            for j in range(i+1, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]


def prime_list_ver2(n):
