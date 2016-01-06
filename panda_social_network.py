

from collections import deque


class PandaSocialNetwork:
    def __init__(self):
        self._soc_network = {}

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise Exception('PandaAlreadyThere')
        else:
            self._soc_network.update({panda: []})

    def has_panda(self, panda):
        if panda in self._soc_network.keys():
            return True
        else:
            return False

    def make_friends(self, panda1, panda2):
        for i in [panda1, panda2]:
            if self.has_panda(i) is False:
                self.add_panda(i)
            else:
                pass
        self._soc_network[panda1].append(panda2)
        self._soc_network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if panda2 in self._soc_network[panda1]:
            return True
        else:
            return False

    def friends_of(self, panda):
        if self.has_panda(panda):
            return self._soc_network[panda]
        else:
            return False

    def connection_level(self, panda1, panda2):
        pass

    def are_connected(self, panda1, panda2):
        pass

    def how_many_gender_in_network(self, level, panda, gender):
        pass
