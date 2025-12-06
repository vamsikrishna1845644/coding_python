import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Time vector
t = np.linspace(0, 1.5, 500)

# System 1: Without PD Control
# G(s) = 100 / (s^2 + 12s) -> CLTF = 100 / (s^2 + 12s + 100)
num1 = [100]
den1 = [1, 12, 100]
sys1 = signal.TransferFunction(num1, den1)
t1, y1 = signal.step(sys1, T=t)

# System 2: With PD Control
# G(s) = (3.33s + 100) / (s^2 + 12s) -> CLTF = (3.33s + 100) / (s^2 + 15.33s + 100)
# Note: The Zero at -30 is included in the numerator
num2 = [3.333, 100]
den2 = [1, 15.333, 100]
sys2 = signal.TransferFunction(num2, den2)
t2, y2 = signal.step(sys2, T=t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t1, y1, label='Without PD Control (M_p ~9.5%)', linewidth=2)
plt.plot(t2, y2, label='With PD Control (M_p ~2.4%)', linewidth=2)
plt.axhline(1, color='k', linestyle='--', alpha=0.5, label='Steady State')
plt.title('Step Response Comparison: With vs Without PD Control')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()
plt.show()




