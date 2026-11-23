
import matplotlib.pyplot as plt
import numpy as np

# Freundlich isotherm parameters: q_e = k * P^(1/n)
P = np.linspace(1, 100, 300)  # Equilibrium pressure (kPa)

cases = [
    {"k": 1.5, "inv_n": 0.4, "label": "k = 1.5, 1/n = 0.40"},
    {"k": 2.0, "inv_n": 0.5, "label": "k = 2.0, 1/n = 0.50"},
    {"k": 3.0, "inv_n": 0.65, "label": "k = 3.0, 1/n = 0.65"},
]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 1. Nonlinear Freundlich adsorption isotherm: q_e vs. P
for c in cases:
    q_e = c["k"] * (P ** c["inv_n"])
    ax1.plot(P, q_e, linewidth=2, label=c["label"])

ax1.set_title("Freundlich Adsorption Isotherm (q_e vs. P)")
ax1.set_xlabel("Equilibrium Pressure P (kPa)")
ax1.set_ylabel("Adsorbed Amount q_e = x/m (mmol/g)")
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.legend()

# 2. Linearized Freundlich plot: log10(q_e) vs. log10(P)
log_P = np.log10(P)
for c in cases:
    q_e = c["k"] * (P ** c["inv_n"])
    ax2.plot(log_P, np.log10(q_e), linewidth=2, label=f"Slope={c['inv_n']:.2f}, int={np.log10(c['k']):.2f}")

ax2.set_title("Linearized Freundlich Plot (log10 q_e vs. log10 P)")
ax2.set_xlabel("log10(P)")
ax2.set_ylabel("log10(q_e)")
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.legend()

plt.tight_layout()
plt.savefig("freundlich_adsorption_isotherm.png", dpi=300)
plt.show()

### Optional Python Code for MQ-135 Log-Log Calibration Curves

import matplotlib.pyplot as plt
import numpy as np

# Example power-law calibration curves: Rs/R0 = A * (ppm ** b)
ppm = np.logspace(1, 3, 200)  # 10 ppm to 1000 ppm

curves = [
    {"A": 116.60, "b": -0.68, "label": "NH3 (illustrative)"},
    {"A": 77.25, "b": -0.58, "label": "Alcohol (illustrative)"},
    {"A": 100.00, "b": -0.52, "label": "Benzene (illustrative)"},
]

plt.figure(figsize=(7, 5))
for item in curves:
    rs_r0 = item["A"] * (ppm ** item["b"])
    plt.loglog(ppm, rs_r0, linewidth=2, label=item["label"])

plt.title("MQ-135 Log-Log Calibration Curves (Rs/R0 vs. ppm)")
plt.xlabel("Gas Concentration (ppm)")
plt.ylabel("Resistance Ratio (Rs / R0)")
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig("mq135_calibration_curves.png", dpi=300)
plt.show()
