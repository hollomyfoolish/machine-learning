import numpy as np

np.random.seed(1)
debug = False


def create_data(shape=(1, 100)):
    _X = (0.5 - np.random.random(shape)) * 10
    # _y1 = (0.5 - np.random.random(shape)) * 4
    if debug:
        print _X
        print np.sin(_X)
        # print _y1
    _y = _X - np.sin(_X)
    _y = np.abs((_y + np.abs(_y)) / (2 * _y))
    _Z = [1 for e in range(shape[1])]
    _Z = np.asarray(_Z).reshape((1, shape[1]))
    _X = np.concatenate((_X, _Z), 0)
    return _X, _y


def sigmoid(in_x, syn):
    return 1 / (1 + np.exp(-(np.dot(in_x, syn))))

X, y = create_data((1, 100))
X = X.T
y = y.T

syn0 = 2 * np.random.random((2, 10)) - 1
syn1 = 2 * np.random.random((10, 1)) - 1

for j in xrange(60000):
    l1 = 1 / (1 + np.exp(-(np.dot(X, syn0))))
    l2 = 1 / (1 + np.exp(-(np.dot(l1, syn1))))

    l2_delta = (y - l2) * (l2 * (1 - l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1 - l1))

    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)

# print l2_delta
# print l1_delta

print l2 - y


def predict(_x):
    _l1 = 1 / (1 + np.exp(-(np.dot(_x, syn0))))
    _l2 = 1 / (1 + np.exp(-(np.dot(_l1, syn1))))
    print np.concatenate((_l2, _l2 - np.round(_l2)), 1)
    return np.round(_l2)

print 'predict'
testX, targetY = create_data((1, 10))
predictY = predict(testX.T)
print predictY
print targetY.T - predictY

