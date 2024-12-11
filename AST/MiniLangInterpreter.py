import threading

class MiniLangInterpreter:
    def __init__(self, input_data=None, max_loop_iterations=100, max_execution_time=3):
        self.variables = {}
        self.output_buffer = []
        self.max_loop_iterations = max_loop_iterations
        self.max_execution_time = max_execution_time
        self.execution_complete = False
        self.execution_result = None

        if input_data:
            self.input_variables = input_data
        else:
            self.input_variables = {}

    def reset(self):
        self.variables = {}
        self.output_buffer = []
        self.execution_complete = False
        self.execution_result = None

    def _run_with_timeout(self, node):
        try:
            if node.type == 'program':
                for statement in node.children:
                    result = self.execute_statement(statement)
                    if result is not None:
                        self.execution_result = result
                        break

            self.execution_complete = True
        except Exception as e:
            self.execution_result = None
            self.execution_complete = True

    def execute_program(self, node):

        self.reset()

        thread = threading.Thread(target=self._run_with_timeout, args=(node,))
        thread.start()

        thread.join(timeout=self.max_execution_time)

        if thread.is_alive():
            return None

        return self.execution_result

    def execute_statement(self, node):
        if node.type == 'assignStatement':
            var_name = node.children[0].value
            value = self.evaluate_expression(node.children[1])
            self.variables[var_name] = value

        elif node.type == 'whileStatement':
            condition_node, block_node = node.children

            loop_counter = 0
            while self.evaluate_expression(condition_node) > 0:
                if loop_counter >= self.max_loop_iterations:
                    break

                for stmt in block_node.children:
                    result = self.execute_statement(stmt)
                    if result == 'break':
                        return None
                    elif result == 'continue':
                        break

                loop_counter += 1

        elif node.type == 'ifStatement':
            condition_node = node.children[0]
            if_block_node = node.children[1]

            if self.evaluate_expression(condition_node) > 0:
                for stmt in if_block_node.children:
                    self.execute_statement(stmt)

            if len(node.children) > 2:
                else_block_node = node.children[2]
                for stmt in else_block_node.children:
                    self.execute_statement(stmt)

        elif node.type == 'ioStatement':
            if node.value == 'output':
                output_value = self.evaluate_expression(node.children[0])
                self.output_buffer.append(output_value)
            elif node.value == 'input':
                var_name = node.children[0].value
                self.variables[var_name] = self.input_variables.get(var_name, 0)

        elif node.type == 'breakStatement':
            return 'break'

        elif node.type == 'continueStatement':
            return 'continue'

        return None

    def evaluate_expression(self, node):
        if node.type == 'INT':
            return int(node.value)

        if node.type == 'FLOAT':
            return float(node.value)

        if node.type == 'ID':
            return self.variables.get(node.value, 0)

        if node.type == 'expression':
            if len(node.children) == 2:
                left = self.evaluate_expression(node.children[0])
                right = self.evaluate_expression(node.children[1])

                op = node.value

                if op == '+': return left + right
                if op == '-': return left - right
                if op == '*': return left * right
                if op == '/':
                    return left / right if right != 0 else 0

                if op == '==': return int(left == right)
                if op == '!=': return int(left != right)
                if op == '<': return int(left < right)
                if op == '>': return int(left > right)
                if op == '<=': return int(left <= right)
                if op == '>=': return int(left >= right)

                if op == '&&': return int(bool(left) and bool(right))
                if op == '||': return int(bool(left) or bool(right))

        return 0


def advanced_fitness_function(program, test_data):

    total_error = 0.0
    input_penalty = 0.0

    for input_set, expected_output in zip(test_data['inputs'], test_data['expected_outputs']):
        interpreter = MiniLangInterpreter(input_data=input_set)

        interpreter.execute_program(program)

        if interpreter.output_buffer:
            actual_output = interpreter.output_buffer[-1]
        else:
            actual_output = 0

        try:
            error = abs(float(actual_output) - float(expected_output))
            total_error += error
        except (ValueError, TypeError):
            total_error += 1.0 if str(actual_output) != str(expected_output) else 0.0

        input_penalty += max(0, len(input_set) - len(test_data['expected_outputs']) * 2) * 0.1

    total_error += input_penalty

    return total_error
