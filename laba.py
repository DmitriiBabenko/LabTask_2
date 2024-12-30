import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return np.full_like(x, 3/4 + np.sqrt(3)*x/2) # раз тейлор

def f2(x):
    return f1(x) - (x**2)/2  #два тейлор

def f3(x):
    return f2(x) - (2*np.sqrt(3)*(x**3))/6 # три тейлор

def f4(x):
    return f3(x) + (4*(x**4))/24  # четыре тейлор

def f5(x):
    return f4(x) +  (8*np.sqrt(3)*(x**5))/120  # пять тейлор ZzZzZz

def f(x):
    return (np.sin(x + np.pi / 3))**2
# О.x
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Диапазон от -2π до 2π

# O.y
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)
y4 = f4(x)
y5 = f5(x)
y = f(x)
# все 5 тейлоров
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r'$First\, Taylor$', color='red')
plt.plot(x, y2, label=r'$Second\, Taylor$', color='orange')
plt.plot(x, y3, label=r'$Third\, Taylor$', color='yellow')
plt.plot(x, y4, label=r'$Fourth\, Taylor$', color='green')
plt.plot(x, y5, label=r'$Fifth\, Taylor$', color='blue')
plt.plot(x, y5, label=r'$Origin$', color='purple')
# косметика
plt.title("Teylor difference", fontsize=14)
plt.xlabel("x", fontsize=20)
plt.ylabel("y", fontsize=20)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(fontsize=12)
print(-0.1, f2(-0.1), "Приближённое значение для n1")
print(-0.1, f5(-0.1), "Приближённое значение для n2")
print(-0.1, f(-0.1), "точное(для E > 0) значение")
print("ошибка для n1 (нужно 10^(-3)) ", abs(f2(-0.1) - f(-0.1)))
print("ошибка для n2 (нужно 10^(-6)) ", abs(f5(-0.1) - f(-0.1)))
plt.show()
plt.savefig("test.png")