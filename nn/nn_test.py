import numpy as np

X = (0.5 - np.random.random((1, 100))) * 10

y1 = (0.5 - np.random.random((1, 100))) * 4
y2 = y1 - np.sin(X)
y2 = np.abs((y2 + np.abs(y2))/(2 * y2))

Z = [1 for e in range(100)]
Z = np.asarray(Z).reshape((1, 100))
X = np.concatenate((X, Z), 0)
# print X
#print X

print X.shape
print y1.shape
print y2.shape

X = X.T
y2 = y2.T
y = y2

# syn0 = 2 * np.random.random((3, 4)) - 1
syn0 = 2 * np.random.random((2, 8)) - 1
syn1 = 2 * np.random.random((8, 1)) - 1
# syn1 = np.zeros((4, 1))
# print syn0
# print '======================='
# print syn1
# print '==========end syn1============='

for j in xrange(90000):
    l1 = 1 / (1 + np.exp(-(np.dot(X, syn0))))
    l2 = 1 / (1 + np.exp(-(np.dot(l1, syn1))))

    l2_delta = (y - l2) * (l2 * (1 - l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1 - l1))

    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)

print l2_delta
print l1_delta

# print X
# print l1
# print l2

def predict(_X):
    _l1 = 1 / (1 + np.exp(-(np.dot(_X, syn0))))
    _l2 = 1 / (1 + np.exp(-(np.dot(_l1, syn1))))
    return np.round(_l2)

#predict
# pX = (0.5 - np.random.random((1, 10))) * 10
# pY = np.sin(pX)
'''
X = (0.5 - np.random.random((1, 10))) * 10

y1 = (0.5 - np.random.random((1, 10))) * 4
y2 = y1 - np.sin(X)
y2 = np.abs((y2 + np.abs(y2))/(2 * y2))

Z = [1 for e in range(10)]
Z = np.asarray(Z).reshape((1, 10))
X = np.concatenate((X, Z), 0)

# Z = [1 for e in range(10)]
# Z = np.asarray(Z).reshape((1, 10))
# pX = np.concatenate((pX, Z), 0)
'''
print '====predict===='
print y.shape
print (predict(X) - y).shape
print (predict(X) - y).T
#print y2