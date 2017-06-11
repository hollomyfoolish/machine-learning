import numpy as np

X = np.array(np.random.ranf(100)*4-2)
X = X.reshape(100,1)
print X.shape
y = np.array(np.random.ranf(100))
y = y.reshape(100, 1)
for i in range(100):
    if np.sin(X[i]) > X[i]:
        y[i] = 1
    else:
        y[i] = 0

syn0 = 2*np.random.random((1,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
for j in xrange(60000):
    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))

    l2_delta = (y - l2)*(l2*(1-l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))

    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)

print l2 - y
# print 'syn1'
# print syn1
# print 'syn0'
# print syn0
#
# testX = np.array(np.random.ranf(100)*4-2)
# testX = testX.reshape(100,1)
#
# testy = np.array(np.random.ranf(100))
# testy = testy.reshape(100, 1)
# for i in range(100):
#     if np.sin(testX[i]) > testX[i]:
#         testy[i] = 1
#     else:
#         testy[i] = 0
#
# testl1 = 1 / (1 + np.exp(-(np.dot(testX, syn0))))
# testl2 = 1 / (1 + np.exp(-(np.dot(testl1, syn1))))
#
# print '------'
# for i in range(100):
#     print testl2[i], testy[i], testl2[i] - testy[i]