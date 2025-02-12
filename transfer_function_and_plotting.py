import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define  variables
s, t = sp.symbols('s t')

"""
F_s = sp.symbols('F_s')  # symbolic expression

V_s = sp.Function('V_s')(s) # symbolic function

Kb = sp.symbols('Kb')
T_s = sp.Function('T_s')(s)
Kt = sp.symbols('Kt')
"""

# Define the original matrix A
A = sp.Matrix([
    [-24*s**2 - 49*s - 24,       5*s + 5,           0],
    [             5*s + 5, -s**2 - s - 1,           s],
    [                   0,             s, s**2 + s +1]
])

# Define the column vector B
B = sp.Matrix([100/(s + 0.45), 0, 0])

# Calculate det(A)
det_A = A.det()

# Replace the first column to calculate A1
A1 = A.copy()
A1[:, 0] = B
det_A1 = A1.det()

# Replace the second column to calculate A2
A2 = A.copy()
A2[:, 1] = B
det_A2 = A2.det()

# Replace the third column to calculate A3
A3 = A.copy()
A3[:, 2] = B
det_A3 = A3.det()

# Calculate X1(s), X2(s), X3(s)
X1_s = (det_A1 / det_A).simplify()
X2_s = (det_A2 / det_A).simplify()
X3_s = (det_A3 / det_A).simplify()

# Output X3(s)
print("\nX3(s):")
sp.pprint(X3_s)

# Perform the inverse Laplace transform
X3_t = sp.inverse_laplace_transform(X3_s, s, t)
print(f"Inverse Laplace transform: {X3_t}")

# If X3_t is a simple expression, you can use lambdify to convert it to a numerical function
X3_t_func = sp.lambdify(t, X3_t, 'numpy')

# Generate a time series
t_vals = np.linspace(0, 60, 500)  # Time from 0 to 60 seconds, divided into 500 points
X3_vals = X3_t_func(t_vals)  # Calculate X3(t) at these time points

# Plot
plt.figure(figsize=(8, 6))
plt.plot(t_vals, X3_vals, label="q(t)")
plt.title("q(t) vs t")
plt.xlabel("t (s)")
plt.ylabel("q(t)")
plt.grid(True)
plt.legend()
plt.show()
