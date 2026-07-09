import numpy as np, scipy.stats as stats, matplotlib.pyplot as plt, seaborn as sns
sns.set_theme(style="whitegrid", palette="muted")
mu, sigma, th = 0, 5, [5, 10, 15]
prob = {t: 2*(1 - stats.norm.cdf(t, mu, sigma)) for t in th}
for t in th: print(f"P(|error| > {t}) = {prob[t]:.6f} ({prob[t]*100:.4f}%)")
print("\n--- Buffer Coverage ---")
for t in th: print(f"P(|error| <= {t}) = {1-prob[t]:.6f} ({(1-prob[t])*100:.4f}%)")
print("\n--- Z-Scores ---")
for t in th: print(f"z for threshold {t}: {t/sigma:.2f}")
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(-4*sigma, 4*sigma, 1000)
ax.plot(x, stats.norm.pdf(x, mu, sigma), 'b-', lw=2.5, label='N(0, 5²)')
clr = ['#FF6B6B', '#4ECDC4', '#45B7D1']
for t, c in zip(th, clr):
    for s in [-1, 1]:
        xr = np.linspace(s*t if s==1 else -4*sigma, 4*sigma if s==1 else -t, 200)
        ax.fill_between(xr, stats.norm.pdf(xr, mu, sigma), color=c, alpha=0.6)
    ax.axvline(-t, color=c, ls='--', lw=1.5, alpha=.8)
    ax.axvline(t, color=c, ls='--', lw=1.5, alpha=.8)
for t, c, y in zip(th, clr, [.02, .005, .001]):
    ax.annotate(f'±{t//5}σ\n{prob[t]*100:.2f}% beyond', xy=(t, y), fontsize=10, ha='left', color=c, fontweight='bold')
ax.set(xlabel='Forecast Error (units)', ylabel='Probability Density')
ax.set_title('Task 3: Distribution of Forecast Errors (N(0, σ=5))\nShaded Tails Show Probability of Large Deviations', fontsize=13)
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('figures/fig_task3_normal_curve.png', dpi=150, bbox_inches='tight')
plt.close()
print("\nFigure saved: figures/fig_task3_normal_curve.png")
print("\n--- Risk Management Summary ---")
for t in th: print(f"Buffer ±{t}: covers {(1-prob[t])*100:.2f}% | risk: {prob[t]*100:.2f}%")