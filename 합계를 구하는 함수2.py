start=int(input("시작값을 입력하시오:"))
end = int(input("끝 값을 입력하시오:"))
baesu = int(input("배수를 입력하시오:"))


def baesu_sum2(start, end, baesu):
    sum = 0
    i = start
    for i in range(start, end, 1):
        if i%baesu == 0:
            sum += i
        i = i + 1
    return sum
print(baesu_sum2(start, end, baesu))
