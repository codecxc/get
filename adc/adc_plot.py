from matplotlib import pyplot as plt

def plot_voltage_vs_time(time,voltage,max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.title("График зависимости U(t)")
    plt.xlabel("Время,с")
    plt.ylabel("Напряжение, В")

    plt.grid(True,alpha=0.3)

    plt.show()
