import numpy as np, sympy as sp, matplotlib.pyplot as plt, seaborn as sns

t_sym = sp.Symbol('t')
D_sym = 4*t_sym**3 - 18*t_sym**2 + 24*t_sym + 90
D_prime_sym, D_double_sym = sp.diff(D_sym, t_sym), sp.diff(D_sym, t_sym, 2)

print(f"D(t) = {D_sym}\nD'(t) = {D_prime_sym}\nD''(t) = {D_double_sym}\n")
for t in [0, 0.5, 1, 1.5, 2, 2.5, 3, 4]:
    print(f"  t={t:.1f}: D={4*t**3-18*t**2+24*t+90:.2f}, D'={12*t**2-36*t+24:.2f}, D''={24*t-36:.2f}")

print(f"\nCritical: t=1 (max, D=100), t=2 (min, D=98)")
print(f"Inflection: t=1.5, D=99.00")
print("t<1: increasing | 1<t<2: decreasing | t>2: increasing")

sns.set_theme(style="whitegrid", palette="muted")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)
tp = np.linspace(0, 4, 200)
D, Dp = 4*tp**3 - 18*tp**2 + 24*tp + 90, 12*tp**2 - 36*tp + 24

ax1.plot(tp, D, color='#2c7bb6', lw=2, label='D(t)')
ax1.scatter([1, 2], [100, 98], color=['#d7191c', '#fdae61'], s=80, zorder=5)
ax1.axvline(1.5, color='gray', ls=':', alpha=.5)
ax1.set_ylabel('Demand D(t)', fontsize=11)
ax1.set_title('D(t) with Critical Points', fontsize=13, fontweight='bold')
ax1.legend(fontsize=9, loc='lower right')

ax2.plot(tp, Dp, color='#d7191c', lw=2, label="D'(t)")
ax2.axhline(0, color='black', lw=.5, alpha=.5)
ax2.fill_between(tp, 0, Dp, where=(Dp > 0), color='green', alpha=.15, label='Increasing')
ax2.fill_between(tp, 0, Dp, where=(Dp < 0), color='red', alpha=.15, label='Decreasing')
ax2.set_xlabel('Time t (hours)', fontsize=11)
ax2.set_ylabel("D'(t)", fontsize=11)
ax2.legend(fontsize=9, loc='upper right')

plt.tight_layout()
plt.savefig('figures/fig_task2_demand_curve.png', dpi=150)
plt.close()
print(f"\nFigure saved | Sympy: Critical={sp.solve(D_prime_sym, t_sym)}, Inflection={sp.solve(D_double_sym, t_sym)}")