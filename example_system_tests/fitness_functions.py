from cmath import log10

from AST.MiniLangInterpreter import MiniLangInterpreter


def calculate_numeric_similarity(actual, target):
    """
    Oblicza podobieństwo między dwiema liczbami.
    Zwraca wartość w przedziale [0, 1], gdzie 1 oznacza identyczne liczby.
    """
    if actual == target:
        return 1.0

    actual = abs(actual)
    target = abs(target)

    if max(actual, target) > 1000:
        similarity = 1.0 / (1.0 + abs(log10(actual + 1) - log10(target + 1)))
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
        return 0.0

    if target in output:
        if desired_position is None:
            return 1.0
        elif desired_position < len(output) and output[desired_position] == target:
            return 1.0
        else:
            return 0.5

    similarity = calculate_numeric_similarity(output[desired_position], target)

    return similarity * 0.5


def evaluate_output_length(output, desired_length=1):
    """
    Ocenia długość wyjścia.
    """
    if not output:
        return 0.0
    if len(output) == desired_length:
        return 1.0
    return max(0, 1.0 - abs(len(output) - desired_length) * 0.2)


def fitness_1_1_A(program):
    """
    Program powinien wygenerować na wyjściu (na dowolnej pozycji) liczbę 1.
    Inne liczby są dozwolone.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    # position_score = evaluate_output_position(output, 1)

    range_score = 0.0
    if output:
        range_score = max(calculate_numeric_similarity(x, 1) for x in output)

    return range_score


def fitness_1_1_B(program):
    """
    Program powinien wygenerować na wyjściu (na dowolnej pozycji) liczbę 789.
    Inne liczby są dozwolone.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    # position_score = evaluate_output_position(output, 789)

    range_score = 0.0
    if output:
        range_score = max(calculate_numeric_similarity(x, 789) for x in output)

    return range_score


def fitness_1_1_C(program):
    """
    Program powinien wygenerować na wyjściu (na dowolnej pozycji) liczbę 31415.
    Inne liczby są dozwolone.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    # position_score = evaluate_output_position(output, 31415)

    range_score = 0.0
    if output:
        range_score = max(calculate_numeric_similarity(x, 31415) for x in output)

    return range_score


def fitness_1_1_D(program):
    """
    Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1.
    Inne liczby mogą się pojawić.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    position_score = evaluate_output_position(output, 1, desired_position=0)

    range_score = 0.0
    if output:
        range_score = max(calculate_numeric_similarity(x, 1) for x in output)

    return 0.8 * position_score + 0.2 * range_score


def fitness_1_1_E(program):
    """
    Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 789.
    Inne liczby mogą się pojawić.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    position_score = evaluate_output_position(output, 789, desired_position=0)

    range_score = 0.0
    if output:
        range_score = max(calculate_numeric_similarity(x, 789) for x in output)

    return 0.8 * position_score + 0.2 * range_score


def fitness_1_1_F(program):
    """
    Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę 1.
    Nie powinien generować nic poza tą liczbą.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    value_score = 0.0
    if output:
        value_score = calculate_numeric_similarity(output[0], 1)

    length_score = evaluate_output_length(output, 1)

    return 0.7 * value_score + 0.3 * length_score



def evaluate_arithmetic_operation(program, test_data, operation="sum"):
    """
    Wspólna funkcja przystosowania dla operacji arytmetycznych (suma, różnica, iloczyn).
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    total_score = 0.0
    test_count = len(test_data['inputs'])

    for input_set, expected in zip(test_data['inputs'], test_data['expected_outputs']):
        interpreter.reset()
        interpreter.input_variables = input_set
        interpreter.execute_program(program)

        if not interpreter.output_buffer:
            continue

        actual = interpreter.output_buffer[-1]
        try:
            actual = float(actual)
            expected = float(expected)

            accuracy_score = calculate_numeric_similarity(actual, expected)

            length_score = evaluate_output_length(interpreter.output_buffer, 1)

            sign_score = 1.0
            if operation in ["sum", "difference"]:
                if (actual < 0 and expected < 0) or (actual >= 0 and expected >= 0):
                    sign_score = 1.0
                else:
                    sign_score = 0.5

            test_score = (0.6 * accuracy_score + 0.2 * length_score + 0.2 * sign_score)
            total_score += test_score

        except (ValueError, TypeError):
            continue

    return total_score / test_count




def fitness_1_2_A(program):
    """
    Zadanie 1.2.A:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
    Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9].
    """
    test_data = {
        "inputs": [
            {"var_0": 0, "var_1": 0},
            {"var_0": 5, "var_1": 3},
            {"var_0": 9, "var_1": 9},
            {"var_0": 2, "var_1": 7},
            {"var_0": 4, "var_1": 6}
        ],
        "expected_outputs": [0, 8, 18, 9, 10]
    }
    return evaluate_arithmetic_operation(program, test_data, operation="sum")


def fitness_1_2_B(program):
    """
    Zadanie 1.2.B:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
    Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9].
    """
    test_data = {
        "inputs": [
            {"var_0": -9, "var_1": -9},
            {"var_0": -5, "var_1": 5},
            {"var_0": 0, "var_1": 0},
            {"var_0": 7, "var_1": -3},
            {"var_0": 9, "var_1": -9}
        ],
        "expected_outputs": [-18, 0, 0, 4, 0]
    }
    return evaluate_arithmetic_operation(program, test_data, operation="sum")


def fitness_1_2_C(program):
    """
    Zadanie 1.2.C:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
    Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999].
    """
    test_data = {
        "inputs": [
            {"var_0": -9999, "var_1": -9999},
            {"var_0": 1234, "var_1": 5678},
            {"var_0": -5000, "var_1": 5000},
            {"var_0": 9999, "var_1": -9999},
            {"var_0": 0, "var_1": 0}
        ],
        "expected_outputs": [-19998, 6912, 0, 0, 0]
    }
    return evaluate_arithmetic_operation(program, test_data, operation="sum")


def fitness_1_2_D(program):
    """
    Zadanie 1.2.D:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) ich różnicę.
    Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999].
    """
    test_data = {
        "inputs": [
            {"var_0": 10, "var_1": 5},
            {"var_0": -5, "var_1": -5},
            {"var_0": 1000, "var_1": 999},
            {"var_0": -100, "var_1": 50},
            {"var_0": 0, "var_1": 0}
        ],
        "expected_outputs": [5, 0, 1, -150, 0]
    }
    return evaluate_arithmetic_operation(program, test_data, operation="difference")


def fitness_1_2_E(program):
    """
    Zadanie 1.2.E:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) ich iloczyn.
    Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999].
    """
    test_data = {
        "inputs": [
            {"var_0": 2, "var_1": 3},
            {"var_0": -4, "var_1": 5},
            {"var_0": 0, "var_1": 100},
            {"var_0": -7, "var_1": -8},
            {"var_0": 9999, "var_1": 1}
        ],
        "expected_outputs": [6, -20, 0, 56, 9999]
    }
    return evaluate_arithmetic_operation(program, test_data, operation="product")

def evaluate_max_operation(program, test_data):
    """
    Wspólna funkcja przystosowania dla operacji wyboru większej z dwóch liczb.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    total_score = 0.0
    test_count = len(test_data['inputs'])

    for input_set, expected in zip(test_data['inputs'], test_data['expected_outputs']):
        interpreter.reset()
        interpreter.input_variables = input_set
        interpreter.execute_program(program)

        if not interpreter.output_buffer:
            continue

        actual = interpreter.output_buffer[-1]
        try:
            actual = float(actual)
            expected = float(expected)

            accuracy_score = calculate_numeric_similarity(actual, expected)

            input_values = [float(v) for v in input_set.values()]
            if actual >= max(input_values):
                accuracy_score *= 1.2

            length_score = evaluate_output_length(interpreter.output_buffer, 1)

            test_score = 0.7 * accuracy_score + 0.3 * length_score
            total_score += test_score

        except (ValueError, TypeError):
            continue

    return total_score / test_count

def fitness_1_3_A(program):
    """
    Zadanie 1.3.A:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) większą z nich.
    Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9].
    """
    test_data = {
        "inputs": [
            {"var_0": 0, "var_1": 0},
            {"var_0": 1, "var_1": 2},
            {"var_0": 3, "var_1": 4},
            {"var_0": 5, "var_1": 6},
            {"var_0": 7, "var_1": 8},
            {"var_0": 9, "var_1": 9}
        ],
        "expected_outputs": [0, 2, 4, 6, 8, 9]
    }
    return evaluate_max_operation(program, test_data)


def fitness_1_3_B(program):
    """
    Zadanie 1.3.B:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) większą z nich.
    Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999].
    """
    test_data = {
        "inputs": [
            {"var_0": -9999, "var_1": -9999},
            {"var_0": -5000, "var_1": 5000},
            {"var_0": 1234, "var_1": 5678},
            {"var_0": -100, "var_1": 50},
            {"var_0": 0, "var_1": 0},
            {"var_0": 9999, "var_1": -9999},
            {"var_0": 2500, "var_1": 7500}
        ],
        "expected_outputs": [-9999, 5000, 5678, 50, 0, 9999, 7500]
    }
    return evaluate_max_operation(program, test_data)

def evaluate_average_operation(program, test_data, count=None, variable_count=False):
    """
    Wspólna funkcja przystosowania dla operacji obliczania średniej arytmetycznej.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    total_score = 0.0
    test_count = len(test_data['inputs'])

    for input_set, expected in zip(test_data['inputs'], test_data['expected_outputs']):
        interpreter.reset()
        interpreter.input_variables = input_set
        interpreter.execute_program(program)

        if not interpreter.output_buffer:
            continue

        actual = interpreter.output_buffer[-1]
        try:
            actual = float(actual)
            expected = float(expected)

            accuracy_score = calculate_numeric_similarity(actual, expected)

            if variable_count:
                n = input_set.get("var_0", 0)
                used_inputs = len(interpreter.input_variables) - 1  # Odejmuje "var_0"
                if used_inputs != n:
                    accuracy_score *= 0.5

            if abs(round(actual) - expected) < 0.1:
                accuracy_score *= 1.2

            length_score = evaluate_output_length(interpreter.output_buffer, 1)

            test_score = (0.7 * accuracy_score + 0.3 * length_score)
            total_score += test_score

        except (ValueError, TypeError):
            continue

    return total_score / test_count



def fitness_1_4_A(program):
    """
    Zadanie 1.4.A:
    Program powinien odczytać dziesięć pierwszych liczb z wejścia i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną (zaokrągloną do pełnej liczby całkowitej).
    Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99].
    """
    test_data = {
        "inputs": [
            {"var_0": 0, "var_1": 0, "var_2": 0, "var_3": 0, "var_4": 0,
             "var_5": 0, "var_6": 0, "var_7": 0, "var_8": 0, "var_9": 0},
            {"var_0": 1, "var_1": 2, "var_2": 3, "var_3": 4, "var_4": 5,
             "var_5": 6, "var_6": 7, "var_7": 8, "var_8": 9, "var_9": 10},
            {"var_0": -10, "var_1": 20, "var_2": -30, "var_3": 40, "var_4": -50,
             "var_5": 60, "var_6": -70, "var_7": 80, "var_8": -90, "var_9": 100},
            {"var_0": 99, "var_1": -99, "var_2": 99, "var_3": -99, "var_4": 99,
             "var_5": -99, "var_6": 99, "var_7": -99, "var_8": 99, "var_9": -99},
            {"var_0": 50, "var_1": 50, "var_2": 50, "var_3": 50, "var_4": 50,
             "var_5": 50, "var_6": 50, "var_7": 50, "var_8": 50, "var_9": 50}
        ],
        "expected_outputs": [0, 5, 5, 0, 50]
    }
    return evaluate_average_operation(program, test_data, count=10)


def fitness_1_4_B(program):
    """
    Zadanie 1.4.B:
    Program powinien odczytać na początek z wejścia pierwszą liczbę (ma być to wartość nieujemna) a następnie tyle liczb (całkowitych) jaka jest wartość pierwszej odczytanej liczby i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną zaokrągloną do pełnej liczby całkowitej (do średniej nie jest wliczana pierwsza odczytana liczba, która mówi z ilu liczb chcemy obliczyć średnią).
    Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99], pierwsza liczba może być tylko w zakresie [0,99].
    """
    test_data = {
        "inputs": [
            {"var_0": 0},
            {"var_0": 1, "var_1": 100},
            {"var_0": 3, "var_1": 10, "var_2": 20, "var_3": 30},
            {"var_0": 5, "var_1": -10, "var_2": 20, "var_3": -30, "var_4": 40, "var_5": -50},
            {"var_0": 2, "var_1": 99, "var_2": -99},
            {"var_0": 5, "var_1": 25, "var_2": 75, "var_3": -25, "var_4": 50, "var_5": -50}
        ],
        "expected_outputs": [0, 100, 20, -6, 0, 18]
    }
    return evaluate_average_operation(program, test_data, variable_count=True)