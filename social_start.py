from panda import Panda
from panda_social_network import PandaSocialNetwork


def main():
    mitko = Panda('Mitko', 'mitko@pandamail.com', 'male')
    alex = Panda('Alex', 'alex@pandamail.com', 'female')
    viki = Panda('Viki', 'viki@pandamail.com', 'female')
    viktor = Panda('Viktor', 'viktor@pandamail.com', 'male')
    sasho = Panda('Sasho', 'sasho@pandamail.com', 'male')
    sandy = Panda('Sandy', 'sandy@pandamail.com', 'female')

    pandi = [mitko, alex, viki, viktor, sasho, sandy]

    network = PandaSocialNetwork()

    for i in pandi:
        network.add_panda(i)

    network.make_friends(mitko, alex)
    network.make_friends(viktor, alex)
    network.make_friends(viki, alex)
    network.make_friends(sasho, alex)
    network.make_friends(viki, sandy)
    #print(network._soc_network)
    #print(network.friends_of(alex))


    print(network.how_many_gender_in_network(2, mitko, 'male'))
    print(network.how_many_gender_in_network(2, mitko, 'female'))

if __name__ == '__main__':
    main()
