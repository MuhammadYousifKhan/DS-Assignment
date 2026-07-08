"""
Task 3: Forecasting Error Risk (Probability)
Urban Resource Intelligence (URI) Consultancy

Problem: Forecast errors follow N(0, σ = 5).
Evaluate likelihood of large deviations for risk management.
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid", palette="muted")

# =============================================================================
# 1. DISTRIBUTION PARAMETERS
# =============================================================================
mu = 0          # Mean forecast error (unbiased)
sigma = 5       # Standard deviation

# =============================================================================
# 2. PROBABILITY CALCULATIONS
# =============================================================================
# P(|error| > threshold) = 2 * (1 - CDF(threshold)) for symmetric normal
thresholds = [5, 10, 15]
probabilities = {}

for t in thresholds:
    # Tail probability beyond ±t
    p = 2 * (1 - stats.norm.cdf(t, loc=mu, scale=sigma))
    probabilities[t] = p
    print(f"P(|error| > {t}) = {p:.6f} ({p*100:.4f}%)")

# Complement: P(|error| <= t) for buffer planning
print("\n--- Buffer Coverage ---")
for t in thresholds:
    p_inside = 1 - probabilities[t]
    print(f"P(|error| <= {t}) = {p_inside:.6f} ({p_inside*100:.4f}%)")

# Z-scores
print("\n--- Z-Scores ---")
for t in thresholds:
    z = (t - mu) / sigma
    print(f"z for threshold {t}: {z:.2f}")

# =============================================================================
# 3. VISUALISATION: NORMAL CURVE WITH SHADED TAILS
# =============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

# x range
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = stats.norm.pdf(x, mu, sigma)

# Plot main curve
ax.plot(x, y, 'b-', linewidth=2.5, label=f'N(0, 5²)')

# Fill regions
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
labels = ['±1σ (68.27%)', '±2σ (95.45%)', '±3σ (99.73%)']

for t, color, label in zip(thresholds, colors, labels):
    # Left tail
    x_left = np.linspace(mu - 4*sigma, mu - t, 200)
    y_left = stats.norm.pdf(x_left, mu, sigma)
    ax.fill_between(x_left, y_left, color=color, alpha=0.6)

    # Right tail
    x_right = np.linspace(mu + t, mu + 4*sigma, 200)
    y_right = stats.norm.pdf(x_right, mu, sigma)
    ax.fill_between(x_right, y_right, color=color, alpha=0.6)

# Vertical lines at thresholds
for t, color in zip(thresholds, colors):
    ax.axvline(x=-t, color=color, linestyle='--', linewidth=1.5, alpha=0.8)
    ax.axvline(x=t, color=color, linestyle='--', linewidth=1.5, alpha=0.8)

# Annotations
ax.annotate(f'±1σ\n{probabilities[5]*100:.2f}% beyond', xy=(5, 0.02),
            fontsize=10, ha='left', color='#FF6B6B', fontweight='bold')
ax.annotate(f'±2σ\n{probabilities[10]*100:.2f}% beyond', xy=(10, 0.005),
            fontsize=10, ha='left', color='#4ECDC4', fontweight='bold')
ax.annotate(f'±3σ\n{probabilities[15]*100:.2f}% beyond', xy=(15, 0.001),
            fontsize=10, ha='left', color='#45B7D1', fontweight='bold')

ax.set_xlabel('Forecast Error (units)', fontsize=12)
ax.set_ylabel('Probability Density', fontsize=12)
ax.set_title('Task 3: Distribution of Forecast Errors (N(0, σ=5))\n'
             'Shaded Tails Show Probability of Large Deviations', fontsize=13)
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig('figures/fig_task3_normal_curve.png', dpi=150, bbox_inches='tight')
plt.close()

print("\nFigure saved: figures/fig_task3_normal_curve.png")

# =============================================================================
# 4. RISK MANAGEMENT INTERPRETATION
# =============================================================================
print("\n--- Risk Management Summary ---")
for t in thresholds:
    coverage = (1 - probabilities[t]) * 100
    print(f"Buffer ±{t}: covers {coverage:.2f}% of days | risk of exceedance: {probabilities[t]*100:.2f}%")