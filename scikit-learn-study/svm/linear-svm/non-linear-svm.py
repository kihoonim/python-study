import numpy as np


def scikit_impl():
    from sklearn.datasets import make_moons
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import PolynomialFeatures, StandardScaler
    from sklearn.svm import LinearSVC

    X, y = make_moons(n_samples=100, noise=0.15, random_state=42)

    polynomial_svm_clf = Pipeline([
        ('poly_features', PolynomialFeatures(degree=3)),
        ('scaler', StandardScaler()),
        ('svm_clf', LinearSVC(C=10, loss='hinge', max_iter=2000))
    ])

    polynomial_svm_clf.fit(X, y)

    result = polynomial_svm_clf.predict([[10,10]])
    
    print(result)


def main():
    scikit_impl()


if __name__ == '__main__':
    main()