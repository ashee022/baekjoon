import sys

S = sys.stdin.readline().strip()

alphabet_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]

positions = [-1] * 26

for index, char in enumerate(S):
    pos = alphabet_list.index(char)
    if positions[pos] == -1:
        positions[pos] = index

print(' '.join(map(str, positions)))

#개인적으로 enumerate가 생각이 안나서 구글링한 문제. ㅠㅠ