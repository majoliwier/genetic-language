from dataclasses import dataclass
from typing import List, Tuple, Callable, Optional
import random
import json
import copy

@dataclass
class Node:
    type: str
    value: str
    children: List['Node'] = None

    def __post_init__(self):
        if self.children is None:
            self.children = []

class MiniLangGP:
    def __init__(self, max_depth: int = 5):
        self.max_depth = max_depth + 1
        self.operators = {
            'arithmetic': ['*', '/', '+', '-'],
            'comparison': ['==', '!=', '<', '>', '<=', '>='],
            'logical': ['&&', '||']
        }
        self.statement_types = ['assign', 'while', 'if', 'io']
        self.loop_if_statement_types = self.statement_types + ['break', 'continue']
        self.variables = [f'var_{i}' for i in range(10)]

    def required_depth_for_statement(self, statement_type: str) -> int:
        if statement_type == 'assign':
            return 0
        elif statement_type in ['if', 'while']:
            return 2
        elif statement_type == 'block':
            return 1
        elif statement_type == 'io':
            return 0
        elif statement_type in ['break', 'continue']:
            return 0
        else:
            return 1

    def generate_initial_population(self, population_size: int):

        population = []
        half_pop = population_size // 2

        for _ in range(half_pop):
            population.append(self.generate_random_program())

        for _ in range(population_size - half_pop):
            population.append(self.generate_random_program_full())

        return population

    # grow tree generation

    def generate_random_program(self, depth: int = 0) -> Node:
        program = Node('program', '')
        num_statements = random.randint(3, 6)
        for _ in range(num_statements):
            program.children.append(self.generate_random_statement(depth + 1))
        return program

    def generate_random_statement(self, depth: int) -> Node:
        possible_statements = []
        for st in self.statement_types:
            required_depth = self.required_depth_for_statement(st)
            if depth + required_depth < self.max_depth:
                possible_statements.append(st)

        if not possible_statements:
            return self.generate_assignment(depth)

        statement_type = random.choice(possible_statements)

        if statement_type == 'assign':
            return self.generate_assignment(depth)
        elif statement_type == 'while':
            return self.generate_while(depth)
        elif statement_type == 'if':
            return self.generate_if(depth)
        elif statement_type == 'io':
            return self.generate_io(depth)

    def generate_loop_if_statement(self, depth: int) -> Node:
        possible_statements = []
        for st in self.loop_if_statement_types:
            required_depth = self.required_depth_for_statement(st)
            if depth + required_depth < self.max_depth:
                possible_statements.append(st)

        if not possible_statements:
            return self.generate_assignment(depth)

        statement_type = random.choice(possible_statements)

        if statement_type == 'assign':
            return self.generate_assignment(depth)
        elif statement_type == 'while':
            return self.generate_while(depth)
        elif statement_type == 'if':
            return self.generate_if(depth)
        elif statement_type == 'io':
            return self.generate_io(depth)
        elif statement_type == 'break':
            return Node('breakStatement', 'break')
        elif statement_type == 'continue':
            return Node('continueStatement', 'continue')

    def generate_assignment(self, depth: int) -> Node:
        node = Node('assignStatement', '=')
        node.children = [
            Node('ID', random.choice(self.variables)),
            self.generate_expression(depth + 1)
        ]
        return node

    def generate_while(self, depth: int) -> Node:
        node = Node('whileStatement', 'while')
        node.children = [
            self.generate_expression(depth + 1),
            self.generate_block(depth + 1)
        ]
        return node

    def generate_block(self, depth: int) -> Node:
        block = Node('block', '{')
        num_statements = random.randint(1, 3)
        for _ in range(num_statements):
            block.children.append(self.generate_loop_if_statement(depth + 1))
        return block

    def generate_if(self, depth: int) -> Node:
        node = Node('ifStatement', 'if')
        node.children = [
            self.generate_expression(depth + 1),
            self.generate_block(depth + 1)
        ]

        if random.random() < 0.5:
            else_block = self.generate_block(depth + 1)
            node.children.append(else_block)

        return node

    def generate_io(self, depth: int) -> Node:
        io_type = random.choice(['input', 'output'])
        node = Node('ioStatement', io_type)
        if io_type == 'input':
            node.children = [Node('ID', random.choice(self.variables))]
        else:
            node.children = [self.generate_expression(depth + 1)]
        return node

    def generate_expression(self, depth: int) -> Node:
        if depth >= self.max_depth or (random.random() < 0.5):
            return self.generate_terminal_node()
        else:
            expr_type = random.choice(['arithmetic', 'comparison', 'logical'])
            node = Node('expression', random.choice(self.operators[expr_type]))
            node.children = [
                self.generate_expression(depth + 1),
                self.generate_expression(depth + 1)
            ]
            return node

    # full tree generation

    def generate_random_program_full(self, depth: int = 0):
        if depth >= self.max_depth:
            return self.generate_terminal_node()

        program = Node('program', '')
        num_statements = random.randint(3, 6)

        for _ in range(num_statements):
            program.children.append(self.generate_random_statement_full(depth + 1))

        return program

    def generate_while_full(self, depth: int):
        node = Node('whileStatement', 'while')
        node.children = [
            self.generate_expression_full(depth + 1),
            self.generate_block_full(depth + 1)
        ]
        return node

    def generate_block_full(self, depth: int):
        block = Node('block', '{')

        num_statements = random.randint(1, 3) if depth + 1 < self.max_depth else 1
        for _ in range(num_statements):
            block.children.append(self.generate_random_statement_full(depth + 1))

        return block

    def generate_if_full(self, depth: int):
        node = Node('ifStatement', 'if')
        node.children = [
            self.generate_expression_full(depth + 1),
            self.generate_block_full(depth + 1)
        ]

        node.children.append(self.generate_block_full(depth + 1))
        return node

    def generate_io_full(self, depth: int):
        io_type = random.choice(['input', 'output'])
        node = Node('ioStatement', io_type)
        if io_type == 'input':
            node.children = [Node('ID', random.choice(self.variables))]
        else:
            node.children = [self.generate_expression_full(depth + 1)]
        return node

    def generate_expression_full(self, depth: int):
        if depth >= self.max_depth:
            return self.generate_terminal_node()

        expr_type = random.choice(['arithmetic', 'comparison', 'logical'])
        node = Node('expression', random.choice(self.operators[expr_type]))

        if depth + 1 < self.max_depth:
            node.children = [
                self.generate_expression_full(depth + 1),
                self.generate_expression_full(depth + 1)
            ]
        else:
            node.children = [
                self.generate_terminal_node(),
                self.generate_terminal_node()
            ]

        return node

    def generate_terminal_node(self):
        choice = random.random()
        if choice < 0.33:
            return Node('INT', str(random.randint(0, 100)))
        elif choice < 0.66:
            return Node('FLOAT', f"{random.uniform(0, 100):.2f}")
        else:
            return Node('ID', random.choice(self.variables))

    def generate_random_statement_full(self, depth: int):
        if depth >= self.max_depth:
            return self.generate_assignment_full(depth)

        possible_statements = []
        for st in self.statement_types:
            required_depth = self.required_depth_for_statement(st)
            if depth + required_depth < self.max_depth:
                possible_statements.append(st)

        if depth == 1:
            possible_statements.append('io')

        if not possible_statements:
            return self.generate_assignment_full(depth)

        deeper_statements = [st for st in possible_statements if self.required_depth_for_statement(st) > 0]
        statement_type = random.choice(deeper_statements if deeper_statements else possible_statements)

        if statement_type == 'assign':
            return self.generate_assignment_full(depth)
        elif statement_type == 'while':
            return self.generate_while_full(depth)
        elif statement_type == 'if':
            return self.generate_if_full(depth)
        elif statement_type == 'io':
            return self.generate_io_full(depth)

    def generate_assignment_full(self, depth: int) -> Node:
        node = Node('assignStatement', '=')
        node.children = [
            Node('ID', random.choice(self.variables)),
            self.generate_expression_full(depth + 1)
        ]
        return node

    # genetic operations

    def crossover(self, parent1: Node, parent2: Node) -> Tuple[Node, Node]:
        offspring1 = copy.deepcopy(parent1)
        offspring2 = copy.deepcopy(parent2)

        nodes1_by_depth = self._get_nodes_by_depth(offspring1)
        nodes2_by_depth = self._get_nodes_by_depth(offspring2)

        for depth in sorted(nodes1_by_depth.keys()):
            if depth in nodes2_by_depth:
                nodes1 = nodes1_by_depth[depth]
                nodes2 = nodes2_by_depth[depth]

                nodes1 = [node for node in nodes1 if node.type != 'program']
                nodes2 = [node for node in nodes2 if node.type != 'program']

                if nodes1 and nodes2:
                    node1 = random.choice(nodes1)
                    node2 = random.choice(nodes2)

                    parent1_node, index1 = self._find_parent(offspring1, node1)
                    parent2_node, index2 = self._find_parent(offspring2, node2)

                    if parent1_node is not None and parent2_node is not None:
                        parent1_node.children[index1], parent2_node.children[index2] = \
                            parent2_node.children[index2], parent1_node.children[index1]
                    break

        return offspring1, offspring2

    def _get_nodes_by_depth(self, node: Node, depth: int = 0, nodes_by_depth: Optional[dict] = None) -> dict:
        if nodes_by_depth is None:
            nodes_by_depth = {}

        if depth not in nodes_by_depth:
            nodes_by_depth[depth] = []

        nodes_by_depth[depth].append(node)

        for child in node.children:
            self._get_nodes_by_depth(child, depth + 1, nodes_by_depth)

        return nodes_by_depth

    def _find_parent(self, node: Node, target: Node) -> Tuple[Optional[Node], int]:
        for i, child in enumerate(node.children):
            if child is target:
                return node, i
            result = self._find_parent(child, target)
            if result[0] is not None:
                return result
        return None, -1

    def mutate(self, program: Node) -> Node:
        mutated = copy.deepcopy(program)

        all_nodes = [n for n in self._get_all_nodes(mutated) if n.type != 'program']
        if not all_nodes:
            return mutated

        node_to_mutate = random.choice(all_nodes)

        parent, index = self._find_parent(mutated, node_to_mutate)
        if parent is None:

            return mutated
        if node_to_mutate.type in ['ifStatement', 'whileStatement',
                                   'assignStatement', 'ioStatement',
                                   'breakStatement', 'continueStatement']:
            new_subtree = self.generate_random_statement(depth=0)

        elif node_to_mutate.type == 'block':
            new_subtree = self.generate_block(depth=0)

        elif node_to_mutate.type == 'expression':
            new_subtree = self.generate_expression(depth=0)

        elif node_to_mutate.type in ['INT', 'FLOAT', 'ID']:
            new_subtree = self.generate_expression(depth=0)

        else:
            new_subtree = self.generate_expression(depth=0)

        parent.children[index] = new_subtree

        return mutated

    def tournament_selection(self, population: List[Node],fitness_func: Callable[[Node], float], tournament_size: int) -> Node:
        tournament = random.sample(population, tournament_size)
        return max(tournament, key=fitness_func)


    # serialization & utilities

    def _get_all_nodes(self, node: Node) -> List[Node]:
        nodes = [node]
        for child in node.children:
            nodes.extend(self._get_all_nodes(child))
        return nodes

    def _to_dict(self, node: Node) -> dict:
        return {
            'type': node.type,
            'value': node.value,
            'children': [self._to_dict(child) for child in node.children]
        }

    def _from_dict(self, data: dict) -> Node:
        node = Node(data['type'], data['value'])
        node.children = [self._from_dict(child) for child in data.get('children', [])]
        return node

    def serialize(self, program: Node) -> str:
        return json.dumps(self._to_dict(program))

    def deserialize(self, serial_data: str) -> Node:
        data = json.loads(serial_data)
        return self._from_dict(data)

    # printing code

def generate_code(node: 'Node', indent: int = 0) -> str:
    if node is None:
        return ""

    indent_str = " " * indent
    code = ""

    all_operators = {'*', '/', '%', '+', '-', '==', '!=', '<', '>', '<=', '>=', '&&', '||'}

    if node.type == 'program':
        for child in node.children:
            code += generate_code(child, indent)
    elif node.type == 'block':
        code += indent_str + "{\n"
        for child in node.children:
            code += generate_code(child, indent + 2)
        code += indent_str + "}\n"
    elif node.type == 'assignStatement':
        if len(node.children) >= 2:
            lhs = generate_code(node.children[0])
            rhs = generate_code(node.children[1])
            code += indent_str + f"{lhs} = {rhs};\n"
    elif node.type == 'whileStatement':
        if len(node.children) >= 2:
            condition = generate_code(node.children[0])
            body = generate_code(node.children[1], indent)
            code += indent_str + f"while ({condition}) {body}\n"
    elif node.type == 'ifStatement':
        if len(node.children) >= 2:
            condition = generate_code(node.children[0])
            if_body = generate_code(node.children[1], indent)
            code += indent_str + f"if ({condition}) {if_body}"
            if len(node.children) > 2:
                else_body = generate_code(node.children[2], indent)
                code += indent_str + f"else {else_body}"
    elif node.type == 'ioStatement':
        if node.value == 'input' and node.children:
            var_name = generate_code(node.children[0])
            code += indent_str + f"input({var_name});\n"
        elif node.value == 'output' and node.children:
            expr = generate_code(node.children[0])
            code += indent_str + f"output({expr});\n"
    elif node.type == 'breakStatement':
        code += indent_str + "break;\n"
    elif node.type == 'continueStatement':
        code += indent_str + "continue;\n"
    elif node.type == 'expression':
        if len(node.children) == 2:
            left = generate_code(node.children[0])
            right = generate_code(node.children[1])
            code += f"({left} {node.value} {right})"
        elif len(node.children) == 1:
            child_code = generate_code(node.children[0])
            code += f"({node.value}{child_code})"
        else:
            code += node.value if node.value not in all_operators else "0"
    elif node.type in ['INT', 'FLOAT', 'ID']:
        code += node.value

    return code

def example_fitness_function(program: 'Node') -> float:
    return random.random()