#https://programmers.co.kr/learn/courses/30/lessons/77484#

def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    A = len(list(set(win_nums) - set(lottos))) + 1
    I = A - zero
    answer = [min(I, 6), min([A, 6])]
    return answer
