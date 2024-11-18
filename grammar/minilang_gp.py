from dataclasses import dataclass
from typing import List, Tuple, Callable
import random
import json
import copy

from gen.MiniLangLexer import MiniLangLexer
from gen.MiniLangParser import MiniLangParser


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
        self.statement_types = ['assign', 'while', 'if', 'io']

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
        else:  # io
            return self.generate_io(depth)

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

        # Optionally add else block
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

    def generate_expression(self, depth: int) -> Node:
        if depth >= self.max_depth or random.random() < 0.3:
            if random.random() < 0.5:
                return Node('number', str(random.randint(0, 100)))
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

        node1.children, node2.children = node2.children, node1.children

        return offspring1, offspring2

    def mutate(self, program: Node) -> Node:
        mutated = copy.deepcopy(program)
        nodes = self._get_all_nodes(mutated)

        if not nodes:
            return mutated

        node = random.choice(nodes)

        if node.type == 'number':
            node.value = str(random.randint(0, 100))
        elif node.type == 'id':
            node.value = f'var_{random.randint(0, 5)}'
        elif node.type == 'expression':
            expr_type = random.choice(['arithmetic', 'comparison', 'logical'])
            node.value = random.choice(self.operators[expr_type])

        return mutated

    def tournament_selection(self, population: List[Node],
                             fitness_func: Callable[[Node], float],
                             tournament_size: int) -> Node:
        tournament = random.sample(population, tournament_size)
        return max(tournament, key=fitness_func)

    def replace_worst_individual(self, population: List[Node],
                                 new_individual: Node,
                                 fitness_func: Callable[[Node], float]) -> List[Node]:
        # Find and replace the worst individual with the new one if it's better
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
        node.children = [self._from_dict(child) for child in data['children']]
        return node