from dataclasses import dataclass
from typing import List, Tuple, Callable
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
    def __init__(self, max_depth: int = 5, min_depth: int = 2):
        self.max_depth = max_depth
        self.min_depth = min_depth
        self.operators = {
            'arithmetic': ['+', '-', '*', '/'],
            'comparison': ['==', '!=', '<', '>', '<=', '>='],
            'logical': ['&&', '||']
        }
        self.statement_types = ['assign', 'while', 'if', 'io', 'break', 'continue']

    def generate_random_program(self, depth: int = 0) -> Node:
        block = Node('block', '{')
        num_statements = random.randint(1, 4)
        for _ in range(num_statements):
            block.children.append(self.generate_random_statement(depth + 1))
        return block

    def generate_random_statement(self, depth: int) -> Node:
        if depth >= self.max_depth:
            return self.generate_assignment(depth)

        statement_type = random.choice(self.statement_types)

        if statement_type == 'assign':
            return self.generate_assignment(depth)
        elif statement_type == 'while':
            return self.generate_while(depth)
        elif statement_type == 'if':
            return self.generate_if(depth)
        elif statement_type == 'io':
            return self.generate_io(depth)
        elif statement_type == 'break':
            return self.generate_break(depth)
        elif statement_type == 'continue':
            return self.generate_continue(depth)
        else:
            return self.generate_assignment(depth)

    def generate_assignment(self, depth: int) -> Node:
        node = Node('assign', '=')
        node.children = [
            Node('id', f'var_{random.randint(0, 5)}'),
            self.generate_expression(depth + 1)
        ]
        return node

    def generate_while(self, depth: int) -> Node:
        node = Node('while', 'while')
        node.children = [
            self.generate_expression(depth + 1),
            self.generate_random_program(depth + 1)
        ]
        return node

    def generate_if(self, depth: int) -> Node:
        node = Node('if', 'if')
        node.children = [
            self.generate_expression(depth + 1),
            self.generate_random_program(depth + 1)
        ]

        if random.random() < 0.5:
            else_block = self.generate_random_program(depth + 1)
            node.children.append(else_block)

        return node

    def generate_io(self, depth: int) -> Node:
        io_type = random.choice(['input', 'output'])
        node = Node('io', io_type)
        if io_type == 'input':
            node.children = [Node('id', f'var_{random.randint(0, 5)}')]
        else:
            node.children = [self.generate_expression(depth + 1)]
        return node

    def generate_break(self, depth: int) -> Node:
        return Node('break', 'break')

    def generate_continue(self, depth: int) -> Node:
        return Node('continue', 'continue')

    def generate_expression(self, depth: int) -> Node:
        if depth >= self.max_depth or random.random() < 0.3:
            choice = random.random()
            if choice < 0.33:
                return Node('int', str(random.randint(0, 100)))
            elif choice < 0.66:
                return Node('float', f"{random.uniform(0, 100):.2f}")
            else:
                return Node('id', f'var_{random.randint(0, 5)}')

        expr_type = random.choice(['arithmetic', 'comparison', 'logical'])
        node = Node('expression', random.choice(self.operators[expr_type]))
        node.children = [
            self.generate_expression(depth + 1),
            self.generate_expression(depth + 1)
        ]
        return node

    def crossover(self, parent1: Node, parent2: Node) -> Tuple[Node, Node]:
        offspring1 = copy.deepcopy(parent1)
        offspring2 = copy.deepcopy(parent2)

        nodes1 = self._get_all_nodes(offspring1)
        nodes2 = self._get_all_nodes(offspring2)

        if not nodes1 or not nodes2:
            return offspring1, offspring2

        node1 = random.choice(nodes1)
        node2 = random.choice(nodes2)

        node1_children_backup = node1.children
        node1.type, node1.value, node1.children = node2.type, node2.value, node2.children
        node2.type, node2.value, node2.children = node1.type, node1.value, node1_children_backup

        return offspring1, offspring2

    def mutate(self, program: Node) -> Node:
        mutated = copy.deepcopy(program)
        nodes = self._get_all_nodes(mutated)

        if not nodes:
            return mutated

        node = random.choice(nodes)

        if node.type == 'int':
            node.value = str(random.randint(0, 100))
        elif node.type == 'float':
            node.value = f"{random.uniform(0, 100):.2f}"
        elif node.type == 'id':
            node.value = f'var_{random.randint(0, 5)}'
        elif node.type == 'expression':
            expr_type = random.choice(['arithmetic', 'comparison', 'logical'])
            node.value = random.choice(self.operators[expr_type])
        elif node.type == 'assign':
            node.children[1] = self.generate_expression(0)
        elif node.type in ['break', 'continue']:
            node.type = 'break' if node.type == 'continue' else 'continue'
            node.value = node.type

        return mutated

    def tournament_selection(self, population: List[Node],
                             fitness_func: Callable[[Node], float],
                             tournament_size: int) -> Node:
        tournament = random.sample(population, tournament_size)
        return max(tournament, key=fitness_func)

    def replace_worst_individual(self, population: List[Node],
                                 new_individual: Node,
                                 fitness_func: Callable[[Node], float]) -> List[Node]:
        fitness_scores = [fitness_func(prog) for prog in population]
        worst_index = fitness_scores.index(min(fitness_scores))
        new_fitness = fitness_func(new_individual)

        if new_fitness > fitness_scores[worst_index]:
            population[worst_index] = new_individual

        return population

    def serialize(self, program: Node) -> str:
        return json.dumps(self._to_dict(program))

    def deserialize(self, serial_data: str) -> Node:
        data = json.loads(serial_data)
        return self._from_dict(data)

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
