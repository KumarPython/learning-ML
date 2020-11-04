import numpy as np


def gradient_descent(x, y):
    m_current = b_current = 0
    n=len(x)
    iterations = 100
    learning_rate = 0.084
    for i in range(iterations):
        y_predicted = m_current * x + b_current
        cost = (1/n) * sum((y-y_predicted)**2)
        md = (-2/n) * sum(x * (y - y_predicted))
        bd = (-2 / n) * sum(y - y_predicted)
        m_current = m_current - learning_rate * md
        b_current = b_current - learning_rate * bd
        print(f"Iteration: {i} slope: {m_current} and intercept: {b_current} and the cost is: {cost}")


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])
gradient_descent(x, y)

