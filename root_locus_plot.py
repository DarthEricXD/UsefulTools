import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# G(s) = (s + 5) / (s + 1)
G_num = [1, 5]
G_den = [1, 1]

# H(s) = (s + 6) / (s + 0.5)
H_num = [1, 6]
H_den = [1, 0.5]

# L(s) = G(s) * H(s)
L_num = np.convolve(G_num, H_num)
L_den = np.convolve(G_den, H_den)

L = ctl.TransferFunction(L_num, L_den)

plt.figure(figsize=(8, 6))
ctl.root_locus(L, grid=True)
plt.title("Root Locus of the Closed-Loop System")
plt.show()
