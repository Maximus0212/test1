k =18
m =22
n =21

tot = k + m +n
to = tot - 1

k_1 = k/tot
m_1 = m/tot
n_1 = n/tot

#1=>k 2=>k, m, n
K1 = (k_1) * ((k-1)/to)
K2 = (k_1) * (m/to)
K3 = (k_1) * (n/to)
print(K1)

#1=>m 2=>k,m,n
M1 = m_1*(k/to)
M2 = m_1*((m-1)/to)*(3/4)
M3 = m_1*(n/to)*(1/2)

#1=>m 2=>k,m,n
N1 = n_1*(k/to)
N2 = n_1*(m/to)*(1/2)
N3 = n_1*((n-1)/to)*0


result = K1+K2+K3+M1+M2+M3+N1+N2+N3

print(round(result,5))
