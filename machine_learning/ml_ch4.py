import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# ---------------------------The Normal Equation---------------------
# X = 2 * np.random.rand(100, 1)
# y = 4 + 3 * X + np.random.randn(100, 1)
#
# X_b = np.c_[np.ones((100, 1)), X]  # add x0 = 1 to each instance
# theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
# X_new = np.array([[0], [2]])
# X_new_b = np.c_[np.ones((2, 1)), X_new]  # add x0 = 1 to each instance
# y_predict = X_new_b.dot(theta_best)
# plt.plot(X_new, y_predict, "r-", linewidth=2, label="Predictions")
# plt.plot(X, y, "b.")
# plt.xlabel("$x_1$", fontsize=18)
# plt.ylabel("$y$", rotation=0, fontsize=18)
# plt.legend(loc="upper left", fontsize=14)
# plt.axis([0, 2, 0, 15])
# plt.show()
# lin_reg = LinearRegression()
# lin_reg.fit(X, y)
# print(lin_reg.intercept_, lin_reg.coef_)
# print(lin_reg.predict(X_new))


# -------------------------Gradient Descent---------------------
# def plot_gradient_descent(theta, eta, theta_path=None):
#     m = len(X_b)
#     plt.plot(X, y, "b.")
#     n_iterations = 1000
#     for iteration in range(n_iterations):
#         if iteration < 10:
#             y_predict = X_new_b.dot(theta)
#             style = "b-" if iteration > 0 else "r--"
#             plt.plot(X_new, y_predict, style)
#         gradients = 2 / m * X_b.T.dot(X_b.dot(theta) - y)
#         theta = theta - eta * gradients
#         if theta_path is not None:
#             theta_path.append(theta)
#     plt.xlabel("$x_1$", fontsize=18)
#     plt.axis([0, 2, 0, 15])
#     plt.title(r"$\eta = {}$".format(eta), fontsize=16)


# theta_path_bgd = []
# np.random.seed(42)
# theta = np.random.randn(2, 1)  # random initialization
# plt.figure(figsize=(10, 4))
# plt.subplot(131);plot_gradient_descent(theta, eta=0.02)
# plt.ylabel("$y$", rotation=0, fontsize=18)
# plt.subplot(132);plot_gradient_descent(theta, eta=0.1, theta_path=theta_path_bgd)
# plt.subplot(133);plot_gradient_descent(theta, eta=0.5)
# plt.show()


# -------------------------Stochastic Gradient Descent-------------------------
# theta_path_sgd = []
# m = len(X_b)
# np.random.seed(42)

# n_epochs = 50
# t0, t1 = 5, 50  # learning schedule hyperparameters


# def learning_schedule(t):
#     return t0 / (t + t1)


# theta = np.random.randn(2,1)  # random initialization
# for epoch in range(n_epochs):
#     for i in range(m):
#         if epoch == 0 and i < 20:                    # not shown in the book
#             y_predict = X_new_b.dot(theta)           # not shown
#             style = "b-" if i > 0 else "r--"         # not shown
#             plt.plot(X_new, y_predict, style)        # not shown
#         random_index = np.random.randint(m)
#         xi = X_b[random_index:random_index+1]
#         yi = y[random_index:random_index+1]
#         gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
#         eta = learning_schedule(epoch * m + i)
#         theta = theta - eta * gradients
#         theta_path_sgd.append(theta)                 # not shown

# plt.plot(X, y, "b.")                                 # not shown
# plt.xlabel("$x_1$", fontsize=18)                     # not shown
# plt.ylabel("$y$", rotation=0, fontsize=18)           # not shown
# plt.axis([0, 2, 0, 15])                              # not shown
# plt.show()
# print(theta)

# -------------------------Polynomial Regression-------------------------


# np.random.seed(42)
# m = 100
# X = 6 * np.random.rand(m, 1) - 3
# y = 0.5 * X**2 + X + 2 + np.random.randn(m, 1)
#
# poly_features = PolynomialFeatures(degree=2, include_bias=False)
# X_poly = poly_features.fit_transform(X)
# lin_reg = LinearRegression()
# lin_reg.fit(X_poly, y)
#
# X_new=np.linspace(-3, 3, 100).reshape(100, 1)
# X_new_poly = poly_features.transform(X_new)
# y_new = lin_reg.predict(X_new_poly)

# for style, width, degree in (("g-", 1, 300), ("b--", 2, 2), ("r-+", 2, 1)):
#     polybig_features = PolynomialFeatures(degree=degree, include_bias=False)
#     std_scaler = StandardScaler()
#     lin_reg = LinearRegression()
#     polynomial_regression = Pipeline([
#         ("poly_features", polybig_features),
#         ("std_scaler", std_scaler),
#         ("lin_reg", lin_reg),
#     ])
#     polynomial_regression.fit(X, y)
#     y_newbig = polynomial_regression.predict(X_new)
#     plt.plot(X_new, y_newbig, style, label=str(degree), linewidth=width)
#
# plt.plot(X, y, "b.", linewidth=3)
# plt.legend(loc="upper left")
# plt.xlabel("$x_1$", fontsize=18)
# plt.ylabel("$y$", rotation=0, fontsize=18)
# plt.axis([-3, 3, 0, 10])
# plt.show()


# -------------------------Learning Curves-------------------------
# def plot_learning_curves(model, X, y):
#     X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
#     train_errors, val_errors = [], []
#     for m in range(1, len(X_train)):
#         model.fit(X_train[:m], y_train[:m])
#         y_train_predict = model.predict(X_train[:m])
#         y_val_predict = model.predict(X_val)
#         train_errors.append(mean_squared_error(y_train_predict, y_train[:m]))
#         val_errors.append(mean_squared_error(y_val_predict, y_val))
#         plt.plot(np.sqrt(train_errors), "r-+", linewidth=2, label="train")
#         plt.plot(np.sqrt(val_errors), "b-", linewidth=3, label="val")
#
#
# polynomial_regression = Pipeline([
#     ("poly_features", PolynomialFeatures(degree=10, include_bias=False)),
#     ("lin_reg", LinearRegression()),
# ])
# plot_learning_curves(polynomial_regression, X, y)
# plt.axis([0, 80, 0, 3])                         # not shown in the book
# plt.show()


# -------------------------Regularized Linear Model-------------------------
np.random.seed(42)
m = 20
X = 3 * np.random.rand(m, 1)
y = 1 + 0.5 * X + np.random.randn(m, 1) / 1.5
X_new = np.linspace(0, 3, 100).reshape(100, 1)

def plot_model(model_class, polynomial, alphas, **model_kargs):
    for alpha, style in zip(alphas, ("b-", "g--", "r:")):
        model = model_class(alpha, **model_kargs) if alpha > 0 else LinearRegression()
        if polynomial:
            model = Pipeline([
                ("poly_features", PolynomialFeatures(degree=10, include_bias=False)),
                ("std_scaler", StandardScaler()),
                ("regul_reg", model),
            ])
        model.fit(X, y)
        y_new_regul = model.predict(X_new)
        lw = 2 if alpha > 0 else 1
        plt.plot(X_new, y_new_regul, style, linewidth=lw, label=r"$\alpha = {}$".format(alpha))
    plt.plot(X, y, "b.", linewidth=3)
    plt.legend(loc="upper left", fontsize=15)
    plt.xlabel("$x_1$", fontsize=18)
    plt.axis([0, 3, 0, 4])

plt.figure(figsize=(8,4))
plt.subplot(121)
plot_model(Ridge, polynomial=False, alphas=(0, 10, 100), random_state=42)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.subplot(122)
plot_model(Ridge, polynomial=True, alphas=(0, 10**-5, 1), random_state=42)

plt.show()
