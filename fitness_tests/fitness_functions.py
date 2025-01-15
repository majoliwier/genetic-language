import random

from AST.MiniLangInterpreter import MiniLangInterpreter
import math


def calculate_numeric_similarity(actual, target):
    """
    Oblicza podobieństwo między dwiema liczbami.
    Zwraca wartość w przedziale [0, 1], gdzie 1 oznacza identyczne liczby.
    """
    if actual == target:
        return 1.0

    actual = abs(actual)
    target = abs(target)

    # Jeśli liczby są duże, używamy logarytmicznego podejścia
    if max(actual, target) > 1000:
        similarity = 1.0 / (1.0 + abs(math.log10(actual + 1) - math.log10(target + 1)))
    else:
        max_diff = max(target * 2, 100)
        diff = abs(actual - target)
        similarity = max(0, 1.0 - (diff / max_diff))

    return similarity


def evaluate_output_position(output, target, desired_position=None):
    """
    Ocenia występowanie liczby target w output z uwzględnieniem pozycji.
    """
    if not output:
        print("evaluate_output_position: Brak wyjścia.")
        return 0.0

    # Debug: wypisanie pierwszej wartości, jeśli desired_position jest 0
    if desired_position == 0:
        print(f"evaluate_output_position: Pierwsza wartość wyjścia: {output[0]}")

    # Sprawdzamy, czy celowa wartość znajduje się na żądanej pozycji
    if desired_position is not None and desired_position < len(output) and output[desired_position] == target:
        print(f"evaluate_output_position: Znaleziono {target} na pozycji {desired_position}.")
        return 1.0

    # Sprawdzamy, czy target występuje gdziekolwiek w wyjściu
    if target in output:
        print(f"evaluate_output_position: Znaleziono {target} gdzieś w wyjściu.")
        return 0.5

    # Jeśli target nie występuje, obliczamy podobieństwo na zadanej pozycji (jeśli dostępne)
    if desired_position is not None and desired_position < len(output):
        similarity = calculate_numeric_similarity(output[desired_position], target)
        print(f"evaluate_output_position: Podobieństwo na pozycji {desired_position}: {similarity}")
        return similarity * 0.5

    return 0.0


def evaluate_output_length(output, desired_length=1):
    """
    Ocenia długość wyjścia w stosunku do oczekiwanej długości.
    """
    if not output:
        return 0.0
    if len(output) == desired_length:
        return 1.0
    return max(0, 1.0 - abs(len(output) - desired_length) * 0.2)


def fitness_1_1A_gradual(program):
    """
    Program powinien wygenerować na wyjściu liczbę 1. Im bliżej wyjść wartość 1, tym wyższa ocena.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    if any(value == 1 for value in output):
        return 1.0
    elif output:
        # Zwróć maksymalne podobieństwo do 1 spośród wszystkich wartości wyjścia
        return max(calculate_numeric_similarity(value, 1) for value in output)
    else:
        return 0.0


def fitness_1_1B_gradual(program):
    """
    Program powinien wygenerować na wyjściu liczbę 789. Funkcja oceni, jak blisko wyjścia są do 789.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    if any(value == 789 for value in output):
        return 1.0
    elif output:
        # Zwróć maksymalne podobieństwo do 789
        return max(calculate_numeric_similarity(value, 789) for value in output)
    else:
        return 0.0


def fitness_1_1C_gradual(program):
    """
    Program powinien wygenerować na wyjściu liczbę 31415. Funkcja oceni, jak blisko wyjścia są do 31415.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    if any(value == 31415 for value in output):
        return 1.0
    elif output:
        # Zwróć maksymalne podobieństwo do 31415
        return max(calculate_numeric_similarity(value, 31415) for value in output)
    else:
        return 0.0


def fitness_1_1D_gradual(program):
    """
    Ocena dla testu 1.1.D: Program powinien wypisać liczbę 1 na pierwszej pozycji.
    Zwraca 1.0, jeśli pierwsza wartość wyjścia to 1, w przeciwnym razie oblicza
    podobieństwo pierwszej wartości do 1.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    # Filtrowanie tylko wartości liczbowych, jeśli to konieczne
    numeric_output = [val for val in output if isinstance(val, (int, float))]

    # Użycie funkcji evaluate_output_position z pozycją 0
    return evaluate_output_position(numeric_output, target=1, desired_position=0)


def fitness_1_1E_gradual(program):
    """
    Ocena dla 1.1.E: Program powinien wygenerować liczbę 789 na pierwszej pozycji wyjścia.
    Jeśli pierwsza wartość to dokładnie 789, zwraca 1.0.
    W przeciwnym wypadku ocenia, jak blisko jest ona do 789.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    if output and len(output) > 0:
        if output[0] == 789:
            return 1.0
        else:
            return calculate_numeric_similarity(output[0], 789)
    else:
        return 0.0


def fitness_1_1F_gradual(program):
    """
    Ocena dla 1.1.F: Program powinien na wyjściu zwrócić jedynie liczbę 1.
    Jeśli wynik składa się z dokładnie jednej liczby będącej 1, zwraca 1.0.
    W przeciwnym razie zwraca podobieństwo tej jedynej liczby do 1,
    o ile wyjście zawiera dokładnie jedną liczbę.
    Jeżeli wyjście zawiera więcej niż jedną liczbę lub jest puste,
    funkcja zwraca 0.0.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    if output and len(output) == 1:
        if output[0] == 1:
            return 1.0
        else:
            return calculate_numeric_similarity(output[0], 1)
    else:
        return 0.0


def fitness_1_2A(program):
    total_error = 0.0
    num_tests = 100

    for _ in range(num_tests):
        # Generujemy losowe liczby z zakresu [0, 9]
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        input_data = {"var_0": a, "var_1": b}  # Założenie: program odczytuje pierwsze dwie liczby

        interpreter = MiniLangInterpreter(
            input_data=input_data,
            max_loop_iterations=1000,
            max_execution_time=3
        )
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        expected = float(a + b)

        # Sprawdzenie, czy wyjście zawiera dokładnie jedną liczbę
        if output and len(output) == 1:
            try:
                result = float(output[0])
                total_error += abs(result - expected)
            except (ValueError, TypeError):
                total_error += 1e6  # kara za błąd konwersji
        else:
            # Kara, jeśli wyjście nie zawiera dokładnie jednej wartości lub jest puste
            total_error += 1e6

    average_error = total_error / num_tests
    return 1.0 / (1.0 + average_error)


def fitness_1_2B(program):
    total_error = 0.0
    num_tests = 100

    for _ in range(num_tests):
        # Losowe liczby w zakresie [-9, 9]
        a = random.randint(-9, 9)
        b = random.randint(-9, 9)
        input_data = {"var_0": a, "var_1": b}  # Założenie: program odczytuje pierwsze dwie liczby

        interpreter = MiniLangInterpreter(input_data=input_data, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        # Porównanie ostatniego elementu wyjścia z sumą
        if output:
            try:
                result = float(output[-1])
                expected = float(a + b)
                total_error += abs(result - expected)
            except (ValueError, TypeError):
                total_error += 1e6
        else:
            total_error += 1e6

    average_error = total_error / num_tests
    return 1.0 / (1.0 + average_error)


def fitness_1_2C(program):
    """
    1.2.C Program powinien odczytać dwie pierwsze liczby z wejścia
    i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być
    tylko całkowite liczby w zakresie [-9999, 9999].
    """
    total_error = 0.0
    num_tests = 100

    for _ in range(num_tests):
        # Losowe liczby w zakresie [-9999, 9999]
        a = random.randint(-9999, 9999)
        b = random.randint(-9999, 9999)
        input_data = {"var_0": a, "var_1": b}  # Zakładamy, że program odczytuje pierwsze dwie liczby

        interpreter = MiniLangInterpreter(input_data=input_data, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        # Porównanie ostatniego elementu wyjścia z sumą
        if output:
            try:
                result = float(output[-1])
                expected = float(a + b)
                total_error += abs(result - expected)
            except (ValueError, TypeError):
                total_error += 1e6
        else:
            total_error += 1e6

    average_error = total_error / num_tests
    return 1.0 / (1.0 + average_error)


def fitness_1_2D(program):
    """
    1.2.D Program powinien odczytać dwie pierwsze liczby z wejścia
    i zwrócić na wyjściu (jedynie) ich różnicę. Na wejściu mogą być
    tylko całkowite liczby w zakresie [-9999, 9999].
    """
    total_error = 0.0
    num_tests = 100

    for _ in range(num_tests):
        a = random.randint(-9999, 9999)
        b = random.randint(-9999, 9999)
        input_data = {"var_0": a, "var_1": b}

        interpreter = MiniLangInterpreter(input_data=input_data, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        if output:
            try:
                result = float(output[-1])
                expected = float(a - b)
                total_error += abs(result - expected)
            except (ValueError, TypeError):
                total_error += 1e6
        else:
            total_error += 1e6

    average_error = total_error / num_tests
    return 1.0 / (1.0 + average_error)


def fitness_1_2E(program):
    """
    1.2.E Program powinien odczytać dwie pierwsze liczby z wejścia
    i zwrócić na wyjściu (jedynie) ich iloczyn. Na wejściu mogą być
    tylko całkowite liczby w zakresie [-9999, 9999].
    """
    total_error = 0.0
    num_tests = 100

    for _ in range(num_tests):
        a = random.randint(-9999, 9999)
        b = random.randint(-9999, 9999)
        input_data = {"var_0": a, "var_1": b}

        interpreter = MiniLangInterpreter(input_data=input_data, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        if output:
            try:
                result = float(output[-1])
                expected = float(a * b)
                total_error += abs(result - expected)
            except (ValueError, TypeError):
                total_error += 1e6
        else:
            total_error += 1e6

    average_error = total_error / num_tests
    return 1.0 / (1.0 + average_error)


def fitness_1_3A(program):
    """
    1.3.A Program powinien odczytać dwie pierwsze liczby z wejścia
    i zwrócić na wyjściu (jedynie) większą z nich.
    Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0, 9].
    """
    total_error = 0.0
    num_tests = 100

    for _ in range(num_tests):
        # Losowe liczby w zakresie [0, 9]
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        input_data = {"var_0": a, "var_1": b}  # Zakładamy odczyt dwóch pierwszych liczb

        interpreter = MiniLangInterpreter(input_data=input_data, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        # Porównanie wyniku wyjścia z oczekiwaną wartością (maksimum z a i b)
        if output:
            try:
                result = float(output[-1])
                expected = float(max(a, b))
                total_error += abs(result - expected)
            except (ValueError, TypeError):
                total_error += 1e6
        else:
            total_error += 1e6

    average_error = total_error / num_tests
    return 1.0 / (1.0 + average_error)


def fitness_1_3B(program):
    """
    1.3.B Program powinien odczytać dwie pierwsze liczby z wejścia
    i zwrócić na wyjściu (jedynie) większą z nich.
    Na wejściu mogą być tylko całkowite liczby w zakresie [-9999, 9999].
    """
    total_error = 0.0
    num_tests = 100

    for _ in range(num_tests):
        # Losowe liczby w zakresie [-9999, 9999]
        a = random.randint(-9999, 9999)
        b = random.randint(-9999, 9999)
        input_data = {"var_0": a, "var_1": b}

        interpreter = MiniLangInterpreter(input_data=input_data, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        if output:
            try:
                result = float(output[-1])
                expected = float(max(a, b))
                total_error += abs(result - expected)
            except (ValueError, TypeError):
                total_error += 1e6
        else:
            total_error += 1e6

    average_error = total_error / num_tests
    return 1.0 / (1.0 + average_error)
