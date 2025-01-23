import json
import matplotlib.pyplot as plt

json_path = 'example_system_tests/test_results/1_3_A1.json'

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

if 'generations' not in data:
    print("Brak danych dotyczących generacji w pliku JSON.")
    exit(1)

generations = data['generations']

x = [gen_data['generation'] for gen_data in generations]
best_fitness = [gen_data['best_fitness'] for gen_data in generations]
average_fitness = [gen_data['average_fitness'] for gen_data in generations]

x.insert(0, 0)
if best_fitness:  # sprawdź, czy lista nie jest pusta
    best_fitness.insert(0, best_fitness[0])
    average_fitness.insert(0, average_fitness[0])
else:
    best_fitness.insert(0, 0)
    average_fitness.insert(0, 0)

plt.figure(figsize=(10, 6))
plt.plot(x, best_fitness, label='Best Fitness', marker='o')
plt.plot(x, average_fitness, label='Average Fitness', marker='x')
plt.title(f"Fitness w kolejnych generacjach dla zadania {data.get('task_name', '')}")
plt.xlabel('Generacja')
plt.ylabel('Fitness')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('example_system_tests/test_results/plots/1_3_A_fitness.png')

plt.show()
