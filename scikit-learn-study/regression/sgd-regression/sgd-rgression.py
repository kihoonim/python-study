import numpy as np


def scikit_impl():
    from sklearn.linear_model import SGDRegressor

    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)

    sgd_reg = SGDRegressor()
    sgd_reg.fit(X, y.ravel())

    print(sgd_reg.intercept_)
    print(sgd_reg.coef_)

    X_new = np.array([[0], [2]])
    result = sgd_reg.predict(X_new)
    
    print(result)


def main():
    scikit_impl()


if __name__ == '__main__':
    main()