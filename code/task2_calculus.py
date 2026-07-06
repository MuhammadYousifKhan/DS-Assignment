"""
Task 2 - Demand Over Time (Calculus)
COM7023 Maths for Data Science - Urban Resource Intelligence

Analyse D(t) = 4t^3 - 18t^2 + 24t + 90, where t is in hours.
- Find critical points (t=1, t=2) via D'(t) = 12t^2 - 36t + 24
- Classify via D''(t) = 24t - 36: t=1 local max, t=2 local min, t=1.5 inflection
- Interpret intervals of increase/decrease and peak-demand management.
"""

import numpy as np
import sympy as sp
import seaborn as sns
import matplotlib.pyplot as plt

# ============================================================
# 1. DEFINE THE FUNCTION
# ============================================================

# Symbolic definition for verification
t_sym = sp.Symbol('t')
D_sym = 4*t_sym**3 - 18*t_sym**2 + 24*t_sym + 90

print("=" * 60)
print("TASK 2 - DEMAND OVER TIME (CALCULUS)")
print("=" * 60)
print(f"\nDemand function: D(t) = 4t^3 - 18t^2 + 24t + 90")
print(f"Domain: t >= 0 (t in hours)")

# ============================================================
# 2. DERIVATIVES
# ============================================================

print("\n" + "-" * 50)
print("DERIVATIVES")
print("-" * 50)

# First derivative (symbolic)
D_prime_sym = sp.diff(D_sym, t_sym)
print(f"\nD'(t) = {D_prime_sym}")
print("  = 12t^2 - 36t + 24")

# Second derivative (symbolic)
D_double_sym = sp.diff(D_prime_sym, t_sym)
print(f"\nD''(t) = {D_double_sym}")
print("  = 24t - 36")

# Numerical evaluation
print("\nEvaluating at key time points:")
t_vals = [0, 0.5, 1, 1.5, 2, 2.5, 3, 4]
for t in t_vals:
    D_val = 4*t**3 - 18*t**2 + 24*t + 90
    Dp_val = 12*t**2 - 36*t + 24
    Dpp_val = 24*t - 36
    print(f"  t={t:.1f}: D={D_val:.2f}, D'={Dp_val:.2f}, D''={Dpp_val:.2f}")

# ============================================================
# 3. CRITICAL POINTS
# ============================================================

print("\n" + "-" * 50)
print("CRITICAL POINTS")
print("-" * 50)

# Set D'(t) = 0 -> 12t^2 - 36t + 24 = 0 -> divide by 12: t^2 - 3t + 2 = 0
# Factor: (t-1)(t-2) = 0
critical_points = [1, 2]

print(f"\nSetting D'(t) = 0:")
print(f"  12t^2 - 36t + 24 = 0")
print(f"  Divide by 12: t^2 - 3t + 2 = 0")
print(f"  Factor: (t-1)(t-2) = 0")
print(f"  Critical points: t = {critical_points[0]}, t = {critical_points[1]}")

# Classify using second derivative test
print("\nClassification using D''(t):")
for t in critical_points:
    Dpp = 24*t - 36
    D_val = 4*t**3 - 18*t**2 + 24*t + 90
    if Dpp > 0:
        classification = "LOCAL MINIMUM (D'' > 0)"
    elif Dpp < 0:
        classification = "LOCAL MAXIMUM (D'' < 0)"
    else:
        classification = "Inflection point (D'' = 0)"
    print(f"  t = {t}: D''({t}) = {Dpp:.0f} -> {classification}")
    print(f"     D({t}) = {D_val:.2f}")

# ============================================================
# 4. INFLECTION POINT
# ============================================================

print("\n" + "-" * 50)
print("INFLECTION POINT")
print("-" * 50)

# Set D''(t) = 0 -> 24t - 36 = 0 -> t = 1.5
t_inflect = 36 / 24
D_inflect = 4*t_inflect**3 - 18*t_inflect**2 + 24*t_inflect + 90
print(f"\nSetting D''(t) = 0:")
print(f"  24t - 36 = 0")
print(f"  t = {t_inflect}")
print(f"  D({t_inflect}) = {D_inflect:.2f}")
print(f"  At t = {t_inflect}, the rate of change switches from")
print(f"  decreasing to increasing (concavity changes).")

# ============================================================
# 5. INTERVALS OF INCREASE / DECREASE
# ============================================================

print("\n" + "-" * 50)
print("INTERVALS OF INCREASE / DECREASE")
print("-" * 50)
print("""
  Interval          D'(t) sign    Behaviour
  ----------        ----------    ---------
  t < 1             positive (+)  D is INCREASING (ramp-up)
  1 < t < 2         negative (-)  D is DECREASING (mid-period dip)
  t > 2             positive (+)  D is INCREASING (renewed growth)
""")

# ============================================================
# 6. INTERPRETATION
# ============================================================

print("-" * 50)
print("INTERPRETATION")
print("-" * 50)
print("""
- Demand starts at D(0) = 90, rises to a peak at t=1 hour (D=100),
  then dips to a trough at t=2 hours (D=98), before rising again.
- The local maximum at t=1 represents a morning peak-demand period.
- The local minimum at t=2 represents a midday lull, useful for
  scheduling maintenance or storage.
- After t=2, demand rises again (afternoon/evening ramp-up).
- The inflection point at t=1.5 is where the rate of decrease
  itself starts to slow down, signalling recovery before the
  actual upturn at t=2.
- For planners: schedule system maintenance during the dip
  (1-2 hours); prepare for peak at t=1 and sustained rise
  after t=2.
""")

# ============================================================
# 7. VISUALISATION - D(t) curve with critical points
# ============================================================

print("-" * 50)
print("GENERATING FIGURE...")
print("-" * 50)

sns.set_theme(style="whitegrid", palette="muted")

# Create a figure with two subplots (D(t) on top, D'(t) on bottom)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)

# --- Time range ---
t_plot = np.linspace(0, 4, 200)
D_plot = 4*t_plot**3 - 18*t_plot**2 + 24*t_plot + 90
Dp_plot = 12*t_plot**2 - 36*t_plot + 24

# --- Top plot: D(t) ---
ax1.plot(t_plot, D_plot, color='#2c7bb6', linewidth=2, label='D(t)')

# Mark critical points
ax1.scatter(1, 100, color='#d7191c', s=80, zorder=5, label=f'Local max (t=1, D=100)')
ax1.scatter(2, 98, color='#fdae61', s=80, zorder=5, label=f'Local min (t=2, D=98)')
ax1.axvline(1.5, color='gray', linestyle=':', alpha=0.5, label=f'Inflection (t=1.5)')

ax1.set_ylabel('Demand D(t) (units/hour)', fontsize=11)
ax1.set_title('Demand Over Time - D(t) with Critical Points', fontsize=13, fontweight='bold')
ax1.legend(fontsize=9, loc='lower right')
ax1.set_ylim(88, 105)

# --- Bottom plot: D'(t) ---
ax2.plot(t_plot, Dp_plot, color='#d7191c', linewidth=2, label="D'(t)")
ax2.axhline(0, color='black', linewidth=0.5, linestyle='-', alpha=0.5)

# Mark where D'(t)=0
ax2.scatter(1, 0, color='#d7191c', s=80, zorder=5)
ax2.scatter(2, 0, color='#fdae61', s=80, zorder=5)
ax2.axvline(1.5, color='gray', linestyle=':', alpha=0.5)

# Shade increasing/decreasing regions on D'(t) plot
ax2.fill_between(t_plot, 0, Dp_plot, where=(Dp_plot > 0),
                  color='green', alpha=0.15, label='D increasing')
ax2.fill_between(t_plot, 0, Dp_plot, where=(Dp_plot < 0),
                  color='red', alpha=0.15, label='D decreasing')

ax2.set_xlabel('Time t (hours)', fontsize=11)
ax2.set_ylabel("D'(t) (units/hour^2)", fontsize=11)
ax2.set_title("D'(t) - Rate of Change of Demand", fontsize=13, fontweight='bold')
ax2.legend(fontsize=9, loc='upper right')

plt.tight_layout()

# Save figure
fig_path = 'figures/fig_task2_demand_curve.png'
plt.savefig(fig_path, dpi=150)
print(f"Figure saved to '{fig_path}'")

# Verification using sympy - confirm critical points numerically
print("\n" + "-" * 50)
print("SYMPY VERIFICATION")
print("-" * 50)
critical_solutions = sp.solve(D_prime_sym, t_sym)
print(f"Critical points from sympy: {critical_solutions}")
inflection_solution = sp.solve(D_double_sym, t_sym)
print(f"Inflection point from sympy: {inflection_solution}")

print("\n" + "=" * 60)
print("TASK 2 COMPLETE")
print("=" * 60)