import json
import matplotlib.pyplot as plt
import os

# Ścieżka do pliku JSON z historią ewolucji
json_file = '/Users/amika/Documents/projects-uni/genetic-language/fitness_tests/results/evolution_history_1_1B.json'  # Zmień ścieżkę/plik w zależności od potrzeb

# Wczytanie danych z pliku JSON
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Wyodrębnienie historii ewolucji z wczytanych danych
history = data.get('evolution_history', [])

# Wyodrębnienie list z pokoleniami, najlepszym i średnim przystosowaniem
generations = [entry['generation'] for entry in history]
best_fitness = [entry['best_fitness'] for entry in history]
avg_fitness = [entry['avg_fitness'] for entry in history]

# Tworzenie wykresu
plt.figure(figsize=(10, 6))
plt.plot(generations, best_fitness, label='Najlepsze przystosowanie', marker='o')
plt.plot(generations, avg_fitness, label='Średnie przystosowanie', marker='x')

# Dodanie tytułu i etykiet osi
test_name = data.get('test_name', 'Nieznany test')
plt.title(f"Przystosowanie w zależności od pokolenia dla testu {test_name}")
plt.xlabel('Pokolenie')
plt.ylabel('Przystosowanie')
plt.legend()
plt.grid(True)

# Zapisanie wykresu do pliku PNG
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)  # Utwórz katalog, jeśli nie istnieje
plot_filename = os.path.join(output_dir, f"{test_name}_fitness_plot.png")
plt.savefig(plot_filename, dpi=300)  # Zapisz wykres z rozdzielczością 300 dpi
print(f"Wykres zapisano jako: {plot_filename}")

# Wyświetlenie wykresu
plt.show()
