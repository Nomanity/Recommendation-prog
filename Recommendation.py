

import logging
from Questions import start_program, \
                      show_example,\
                      data_computations



logger = logging.getLogger(__name__)
logging.basicConfig(filename = 'Training_Graph.log',
                    level = logging.INFO, 
                    format = '%(levelname)s - %(name)s - #%(lineno)d: %(message)s',
                    encoding = 'UTF-8')


# Идея этого класса состоит в том, чтобы превратить вопросы для пользователя
# в объекты, которые можно будет соединять в цепочки и дополнять эти цепочки
# новыми объектами, если такие появятся, без переделывания структуры приложения
class GraphVertex:
    def __init__(self, func, *child_nodes):
        self.func = func
        self.children = []
        for child in child_nodes:
            self.add_children(child)

   
    def add_children(self, child_node):
        if child_node not in self.children:
            self.children.append(child_node)
        else:
            logger.warning('Ссылка {0} {1} уже существует'.format(self.children, child_node))
            print('Ссылка {0} {1} уже существует'.format(self.children, child_node))



# Этот класс нужен для создания цепочек вопросов
class QuestionGraph:

    def __init__(self, root):
        self.nodes = []
        self.root = root

    
    def __str__(self):
        return f'\nThis tree is actually a series of questions and inputs\n{self.nodes}, root node is {self.root.value}'

    def add_nodes(self, *nodes):
        for node in nodes:
            if node not in self.nodes:
                logger.info (f'Add \'{node.func.__name__}\' function to the tree!')
                self.nodes.append(node)

    
    def traverse(self):
        for item in self.nodes:
            item.func()
        


data_comp_node = GraphVertex(data_computations)
show_example_node = GraphVertex(show_example, data_comp_node)
start_program_node = GraphVertex(start_program, show_example_node)


program_graph = QuestionGraph(root = start_program_node)
program_graph.add_nodes(start_program_node, show_example_node, data_comp_node)
program_graph.traverse()
