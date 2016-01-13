import json
from panda import Panda
from collections import deque


class PandaSocialNetwork:
    def __init__(self):
        self._soc_network = {}
        # self._soc_network_loaded = {}
        self.queue = deque()
        self.visited = set()
        # self.people = {'People': []}
        self.people = {}
        self.people2 = {}

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise Exception('PandaAlreadyThere')
        else:
            self._soc_network.update({panda: []})

    def has_panda(self, panda):
        return panda in self._soc_network.keys()

    def make_friends(self, panda1, panda2):
        for i in [panda1, panda2]:
            if not self.has_panda(i):
                self.add_panda(i)
            else:
                pass
        self._soc_network[panda1].append(panda2)
        self._soc_network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda2 in self._soc_network[panda1]

    def friends_of(self, panda):
        if self.has_panda(panda):
            return self._soc_network[panda]
        else:
            return False

    def connection_level(self, start_node, end_node):
        if not (self.has_panda(start_node) or self.has_panda(end_node)):
            return False
        visited = set()
        queue = deque()

        visited.add(start_node)
        queue.append((0, start_node))

        while len(queue) != 0:
            node_with_level = queue.popleft()
            node = node_with_level[1]
            level = node_with_level[0]

            if node == end_node:
                return level

            for neighbour in self._soc_network[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((level + 1, neighbour))

        return -1

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) != -1

    def how_many_gender_in_network(self, level, panda, gender):
        visited = set()
        queue = deque()
        counter = 0
        if panda.gender() == gender:
            gender_count = -1
        else:
            gender_count = 0

        visited.add(panda)
        queue.append((0, panda))

        while len(queue) != 0 and level != counter:
            node_with_level = queue.popleft()
            node = node_with_level[1]
            counter = node_with_level[0]

            for neightbour in self._soc_network[node]:
                if neightbour not in visited:
                    visited.add(neightbour)
                    queue.append((counter + 1, neightbour))

        for panda in visited:
            if panda.gender() == gender:
                gender_count += 1
        return gender_count

    def gen_json(self):
        for i in self._soc_network.keys():
            people_prop = '{},{},{}'.format(i._name, i._email, i._gender)
            people_friends = [x._name for x in self._soc_network[i]]
            # self.people['People'].append({people_prop: people_friends})
            self.people.update({people_prop: people_friends})

    def load_json(self):
        for key, value in self.people.items():
            people_prop = Panda(*key.split(','))
            people_friends = [x for x in value]
            self.people2.update({people_prop: people_friends})

    def gen_soc_network(self):
        for i in self.people2.keys():
            self._soc_network.update({i: []})

        for k1, v1 in self.people2.items():
            for i in self.people2[k1]:
                for j in [key for key in self.people2.keys()]:
                    if i == j._name:
                        self._soc_network[k1].append(j)
                    else:
                        pass

    def print_json(self):
        return self.people

    def print_soc_network(self):
        return self._soc_network

    def print_people2(self):
        return self.people2

    def load(self):
        with open('./social_db.json', 'r') as socdbin:
            self.people = json.load(socdbin)

        self.load_json()

    def save(self):
        self.gen_json()

        with open('./social_db.json', 'w') as socdbout:
            json.dump(self.people, socdbout)
