import unittest
from panda import Panda
from panda_social_network import PandaSocialNetwork


class TestPanda(unittest.TestCase):
    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_panda_init(self):
        self.assertEqual(self.ivo.name(), "Ivo")
        self.assertEqual(self.ivo.gender(), "male")
        self.assertEqual(self.ivo.email(), "ivo@pandamail.com")

    # def test_panda_mail_is_not_valid(self):
    #     with self.assertRaises(ValueError):
    #         Panda("Rado", "rado@gmail.com", "male")

    def test_panda_str(self):
        self.assertEqual(str(self.ivo), "Ivo is a male panda with email: ivo@pandamail.com")

    # def test_panda_repr(self):
    #     pass

    def test_panda_eq(self):
        ivo2 = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        self.assertEqual(self.ivo, ivo2)
        self.assertNotEqual(self.ivo, rado)

    # def test_hash(self):
    #     pass

    def test_name(self):
        self.assertEqual(self.ivo.name(), "Ivo")
        self.assertNotEqual(self.ivo.name(), "Rado")

    def test_mail(self):
        self.assertEqual(self.ivo.email(), "ivo@pandamail.com")
        self.assertNotEqual(self.ivo.email(), "ivo@gmail.com")

    def test_gender(self):
        self.assertEqual(self.ivo.gender(), "male")
        self.assertNotEqual(self.ivo.gender(), "female")

    def test_isMale(self):
        mimi = Panda("Mimi", "mimi@pandamail.com", "female")
        self.assertTrue(self.ivo.isMale())
        self.assertFalse(mimi.isMale())

    def test_isFemale(self):
        mimi = Panda("Mimi", "mimi@pandamail.com", "female")
        self.assertFalse(self.ivo.isFemale())
        self.assertTrue(mimi.isFemale())


class TestSocialNetwork(unittest.TestCase):
    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.network = PandaSocialNetwork()

    def test_has_and_add_panda_in_network(self):
        self.network.add_panda(self.ivo)

        self.assertTrue(self.network.has_panda(self.ivo))

    def test_has_panda_when_panda_not_in_network(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        self.assertFalse(self.network.has_panda(rado))

    def test_make_and_are_friends(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        mimi = Panda("Mimi", "mimi@pandamail.com", "female")
        self.network.make_friends(self.ivo, rado)

        self.assertTrue(self.network.are_friends(self.ivo, rado))
        self.assertFalse(self.network.are_friends(self.ivo, mimi))

    def test_friends_of(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        tony = Panda("Tony", "tony@pandamail.com", "female")
        mimi = Panda("Mimi", "mimi@pandamail.com", "female")
        self.network.make_friends(self.ivo, rado)
        self.network.make_friends(self.ivo, tony)
        self.network.make_friends(self.ivo, mimi)

        self.assertEqual(self.network.friends_of(self.ivo), [rado, tony, mimi])

    def test_friends_of_when_panda_not_in_network(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")

        self.assertFalse(self.network.friends_of(rado))

    def test_connection_level(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        tony = Panda("Tony", "tony@pandamail.com", "female")
        self.network.make_friends(self.ivo, rado)
        self.network.make_friends(rado, tony)

        self.assertEqual(self.network.connection_level(self.ivo, self.ivo), 0)
        self.assertEqual(self.network.connection_level(self.ivo, rado), 1)
        self.assertEqual(self.network.connection_level(self.ivo, tony), 2)

    def test_connection_level_when_not_connected_at_all(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        tony = Panda("Tony", "tony@pandamail.com", "female")
        mimi = Panda("Mimi", "mimi@pandamail.com", "female")
        self.network.make_friends(self.ivo, rado)
        self.network.make_friends(rado, tony)

        self.assertEqual(self.network.connection_level(self.ivo, mimi), -1)

    def test_connection_level_when_panda_not_in_network(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        tony = Panda("Tony", "tony@pandamail.com", "female")

        self.assertFalse(self.network.connection_level(self.ivo, rado))
        self.assertFalse(self.network.connection_level(rado, self.ivo))
        self.assertFalse(self.network.connection_level(rado, tony))

    def test_are_connected(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        tony = Panda("Tony", "tony@pandamail.com", "female")
        mimi = Panda("Mimi", "mimi@pandamail.com", "female")
        viki = Panda("Viki", "viki@pandamail.com", "female")
        self.network.make_friends(self.ivo, rado)
        self.network.make_friends(rado, tony)
        self.network.add_panda(mimi)

        self.assertTrue(self.network.are_connected(self.ivo, self.ivo))
        self.assertTrue(self.network.are_connected(self.ivo, rado))
        self.assertTrue(self.network.are_connected(self.ivo, tony))
        self.assertFalse(self.network.are_connected(self.ivo, mimi))
        self.assertFalse(self.network.are_connected(self.ivo, viki))

    def test_how_many_gender_in_network(self):
        pass

if __name__ == '__main__':
    unittest.main()
