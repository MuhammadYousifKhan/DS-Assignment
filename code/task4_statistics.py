"""Task 4 — Consumption by Building Type: ANOVA + Tukey HSD"""

import numpy as np, scipy.stats as stats, matplotlib.pyplot as plt
import seaborn as sns, pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

sns.set_theme(style="whitegrid", palette="muted")

# Data
apartments = np.array([16.8, 17.2, 16.5, 17.9, 18.1, 17.4, 16.9, 17.6])
terraced   = np.array([18.4, 18.9, 19.1, 18.7, 19.3, 18.6, 19.0, 18.8, 19.2, 18.5])
detached   = np.array([20.1, 19.7, 20.4, 19.9, 20.6, 20.2])
groups = {'Apartments': apartments, 'Terraced': terraced, 'Detached': detached}

print("=" * 60)
print("TASK 4 - CONSUMPTION BY BUILDING TYPE (ANOVA)")
print("=" * 60)

# 1. Descriptive Statistics
print("\n1. DESCRIPTIVE STATISTICS")
print(f"{'Group':<12} {'n':<4} {'Mean':<8} {'SD':<8} {'Min':<7} {'Max':<7}")
for name, d in groups.items():
    print(f"{name:<12} {len(d):<4} {d.mean():<8.4f} {d.std(ddof=1):<8.4f} {d.min():<7.2f} {d.max():<7.2f}")

# 2. Assumption Checks
print("\n2. ASSUMPTION CHECKS")
print("  Shapiro-Wilk (H0: normal distribution):")
for name, d in groups.items():
    w, p = stats.shapiro(d)
    print(f"    {name:<12} W={w:.4f}, p={p:.4f} -> {'Normal' if p > 0.05 else 'Not normal'}")

lev_stat, lev_p = stats.levene(apartments, terraced, detached)
print(f"  Levene's test: stat={lev_stat:.4f}, p={lev_p:.4f} -> {'Equal variances' if lev_p > 0.05 else 'Unequal variances'}")

# 3. One-Way ANOVA
print("\n3. ONE-WAY ANOVA")
print("  H0: All group means are equal | H1: At least one differs | alpha=0.05")
f_stat, anova_p = stats.f_oneway(apartments, terraced, detached)
print(f"  F = {f_stat:.4f}, p = {anova_p:.6f}")
print(f"  -> {'REJECT H0: significant difference exists' if anova_p < 0.05 else 'Fail to reject H0'}")

# 4. Tukey HSD Post-Hoc
print("\n4. TUKEY HSD POST-HOC")
all_vals = np.concatenate([apartments, terraced, detached])
all_lbls = ['Apartments']*len(apartments) + ['Terraced']*len(terraced) + ['Detached']*len(detached)
tukey = pairwise_tukeyhsd(all_vals, all_lbls, alpha=0.05)
print(tukey)

# 5. Visualisation
fig, ax = plt.subplots(figsize=(10, 6))
df = pd.DataFrame({'Building Type': all_lbls, 'Daily Consumption (units)': all_vals})
sns.boxplot(data=df, x='Building Type', y='Daily Consumption (units)', palette='muted', width=0.6, ax=ax)
sns.stripplot(data=df, x='Building Type', y='Daily Consumption (units)', color='black', alpha=0.5, size=6, ax=ax)
for i, m in enumerate([apartments.mean(), terraced.mean(), detached.mean()]):
    ax.plot(i, m, 'D', color='red', markersize=8, zorder=5)
ax.set_title('Task 4: Daily Consumption by Building Type\n(Red diamonds = means)', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('figures/fig_task4_boxplot.png', dpi=150, bbox_inches='tight')
plt.close()
print("\nFigure saved: figures/fig_task4_boxplot.png")

# 6. Summary
print(f"\n5. SUMMARY")
for name, d in groups.items():
    print(f"  {name}: mean={d.mean():.2f}, n={len(d)}")
n = len(all_vals)
print(f"  ANOVA: F({2},{n-3}) = {f_stat:.2f}, p = {anova_p:.6f}")
print("  Detached = highest consumption (priority for efficiency interventions)")
print("  Apartments = lowest (shared infrastructure); Terraced = in-between")
print("=" * 60)