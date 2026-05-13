import numpy as np
import matplotlib.pyplot as plt

def free_space_path_loss(distance_m, frequency_hz):
    c = 3e8
    fspl_db = (20 * np.log10(distance_m) +
               20 * np.log10(frequency_hz) +
               20 * np.log10(4 * np.pi / c))
    return -fspl_db

frequencies = {
    "4G (800 MHz)":   800e6,
    "5G (3.5 GHz)":  3500e6,
    "5G mmWave (28 GHz)": 28e9,
}

distances = np.linspace(10, 2000, 500)
transmit_power_dbm = 43

plt.figure(figsize=(10, 6))
colors = ["#2196F3", "#4CAF50", "#FF5722"]

for (label, freq), color in zip(frequencies.items(), colors):
    path_loss = free_space_path_loss(distances, freq)
    received_power = transmit_power_dbm + path_loss
    plt.plot(distances, received_power, label=label,
             color=color, linewidth=2.5)

plt.axhline(y=-90, color="red", linestyle="--",
            linewidth=1.5, label="Receiver sensitivity (-90 dBm)")
plt.fill_between(distances, -120, -90,
                 alpha=0.08, color="red", label="Dead zone")
plt.title("5G / 4G Signal Strength vs Distance\nFree-Space Path Loss Model",
          fontsize=14, fontweight="bold")
plt.xlabel("Distance from Tower (metres)", fontsize=12)
plt.ylabel("Received Signal Strength (dBm)", fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.ylim(-120, 10)
plt.tight_layout()
plt.savefig("signal_strength.png", dpi=150)
plt.show()
print("✅ Plot saved as signal_strength.png")

print("\n📊 Signal Strength at key distances:")
print(f"{'Distance':<12} {'4G 800MHz':<15} {'5G 3.5GHz':<15} {'5G 28GHz':<15}")
print("-" * 55)
for d in [100, 500, 1000, 2000]:
    row = f"{d}m{'':<9}"
    for freq in frequencies.values():
        power = transmit_power_dbm + free_space_path_loss(d, freq)
        row += f"{power:.1f} dBm{'':<6}"
    print(row)