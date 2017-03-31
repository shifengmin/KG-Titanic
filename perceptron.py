import csv


TRAIN_SET_CSV_NAME = "train.csv"
TEST_SET_CSV_NAME = "test.csv"
LEARNING_RATE = 1.0
MAX_ITERATIONS = 1000
w = []
X = []
Y = []


def vec_inner_product(x, y):
    assert len(x) == len(y)
    ret = 0.0
    for i in range(len(x)):
        ret += x[i]*y[i]
    return ret


def vec_add(x, y):
    assert len(x) == len(y)
    for i in range(len(x)):
        x[i] += y[i]
    return x


def vec_mul(x, k):
    for i in range(len(x)):
        x[i] = x[i]*k
    return x


def perceptron_learning(w, x, y):
    p = vec_inner_product(w, x)
    if p*y < 0:
        w = vec_add(w, vec_mul(x,LEARNING_RATE*y))
    return w


def get_mistake_num(w):
    ret = 0
    for i in range(len(Y)):
        p = vec_inner_product(X[i], w)
        if p*Y[i] < 0:
            ret += 1
    return ret


def pocket_algorithm(w, maxIterations):
    optmz_w = w
    mistakes = len(Y)
    assert maxIterations > 0
    for iter in range(maxIterations):
        for i in range(len(Y)):
            w = perceptron_learning(w, X[i], Y[i])
            curMistakes = get_mistake_num(w)
            if curMistakes < mistakes:
                mistakes = curMistakes
                optmz_w = w
    return optmz_w



def data_preprocess():
    pass


def init():
    pass


def classify(x):
    pass


def get_output(x):
    pass


if __name__ == "__main__":
    pass
