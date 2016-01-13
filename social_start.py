from panda import Panda
from panda_social_network import PandaSocialNetwork


def main():
    '''
    mitko = Panda('Mitko', 'mitko@pandamail.com', 'male')
    alex = Panda('Alex', 'alex@pandamail.com', 'female')
    viki = Panda('Viki', 'viki@pandamail.com', 'female')
    viktor = Panda('Viktor', 'viktor@pandamail.com', 'male')
    sasho = Panda('Sasho', 'sasho@pandamail.com', 'male')
    sandy = Panda('Sandy', 'sandy@pandamail.com', 'female')
    gosho = Panda('Gosho', 'gosho@pandamail.com', 'male')
    pandi = [mitko, alex, viki, viktor, sasho, sandy]
    '''
    network = PandaSocialNetwork()
    '''
    for i in pandi:
        network.add_panda(i)

    network.make_friends(mitko, alex)
    network.make_friends(viktor, alex)
    network.make_friends(viki, alex)
    network.make_friends(sasho, alex)
    network.make_friends(viki, sandy)

    network.save()
    '
    print('\n')
    print('This is json for save {}'.format(network.print_json()))
    print('\n')
    '''
    network.load()
    network.gen_soc_network()
    print('This is soc_network {}'.format(network._soc_network))
    print('This is people {}'.format(network.people))
    print('\n')
    print('This is people2 {}'.format(network.people2))


if __name__ == '__main__':
    main()
