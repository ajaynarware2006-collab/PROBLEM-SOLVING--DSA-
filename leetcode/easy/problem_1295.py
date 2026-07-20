
def findNumbers( nums):
    even_num=0
    for i in nums:
        i=str(i)
        i=len(i)
        if i % 2 == 0:
            even_num += 1

    return even_num