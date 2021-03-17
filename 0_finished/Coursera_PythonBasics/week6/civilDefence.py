def tup_input(a):
    global i
    i += 1
    return int(a), i


def civil_defense(n_list, m_list):
    k = 0
    j = 0
    answ = []
    if len(m_list) >= 2:
        while j < len(m_list) - 1 and k < len(n_list):
            if distance(n_list[k][0], m_list[j][0]) <= \
                    distance(n_list[k][0], m_list[j + 1][0]):
                answ.append([n_list[k][1], m_list[j][1]])
                k += 1
            else:
                j += 1
        for j in range(k, len(n_list)):
            answ.append([n_list[j][1], m_list[-1][1]])
    else:
        for j in range(len(n_list)):
            answ.append([n_list[j][1], 1])
    return answ


def distance(a, b):
    return ((a - b) ** 2) ** (1 / 2)


n = int(input())
i = 0
n_list = list(map(tup_input, input().split()))
i = 0
m = int(input())
m_list = list(map(tup_input, input().split()))
n_list.sort()
m_list.sort()
a = civil_defense(n_list, m_list)
a.sort()
for i in range(len(a)):
    print(a[i][1], end=" ")
