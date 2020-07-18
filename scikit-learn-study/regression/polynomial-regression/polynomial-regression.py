import numpy as np


def scikit_impl():
    from sklearn.preprocessing import PolynomialFeatures

    m = 100
    X = 6 * np.random.rand(m, 1) - 3
    y = 0.5 * X**2 + X + 2 + np.random.randn(m, 1)
    
    poly_features = PolynomialFeatures(degree=2, include_bias=False)    
    X_poly = poly_features.fit_transform(X)
    
    #print(X)
    #print(X_poly)

    from sklearn.linear_model import LinearRegression

    lin_reg = LinearRegression()
    lin_reg.fit(X_poly, y)
    
    print(lin_reg.intercept_)
    print(lin_reg.coef_)


def main():
    scikit_impl()


if __name__ == '__main__':
    main()