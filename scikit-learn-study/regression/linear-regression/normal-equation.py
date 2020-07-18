import numpy as np


def normal_equation():
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)

    X_b = np.c_[np.ones((100, 1)), X]

    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

    print(theta_best)

    X_new = np.array([[0], [2]])
    X_new_b = np.c_[np.ones((2, 1)), X_new]

    y_predict = X_new_b.dot(theta_best)
    print(y_predict)

    import matplotlib.pyplot as plt

    plt.plot(X_new, y_predict, 'r-')
    plt.plot(X, y, 'b.')
    plt.axis([0, 2, 0, 15])
    plt.show()


def scikit_impl():
    from sklearn.linear_model import LinearRegression

    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)

    lin_reg = LinearRegression()
    lin_reg.fit(X, y)

    print(lin_reg.intercept_)
    print(lin_reg.coef_)

    X_new = np.array([[0], [2]])
    result = lin_reg.predict(X_new)
    
    print(result)


def main():
    normal_equation()
    scikit_impl()


if __name__ == '__main__':
    main()