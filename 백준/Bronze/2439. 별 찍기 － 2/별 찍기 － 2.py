N = int(input())
print('\n'.join(' ' * (N - i) + '*' * i for i in range(1,N+1)))