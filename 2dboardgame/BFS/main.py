from graph import *
from queue import *
star_systems = ['Aldebaran', 'Alderamin', 'Algol', 'Alioth', 'Aljanah', 'Alkaid', 'Alnair', 'Alnasl', 'Alpha Centauri', 'Altair', 'Ankaa', 'Antares', 'Arcturus', 'Ascella', 'Castor', 'Cor Caroli', 'Deneb', 'Denebola', 'Diphda', 'Fomalhaut', 'Hamal', 'Larawag', 'Markab', 'Menkalinan', 'Menkent', 'Merak', 'Muphrid', 'Musica', 'Nihal', 'Peacock', 'Phecda', 'Pollux', 'Procyon', 'Ran', 'Rasalhague', 'Regulus', 'Sabik', 'Sheratan', 'Sirius', 'Sol', 'Tarazed', 'Tau Ceti', 'Tiaki', 'Vega', 'Zaurak', 'Zosma']

hyperlanes = [['Aldebaran', 'Menkalinan'], ['Aldebaran', 'Pollux'], ['Alderamin', 'Cor Caroli'], ['Alderamin', 'Markab'], ['Algol', 'Menkalinan'], ['Algol', 'Merak'], ['Algol', 'Phecda'], ['Alioth', 'Cor Caroli'], ['Aljanah', 'Markab'], ['Aljanah', 'Tarazed'], ['Alkaid', 'Markab'], ['Alkaid', 'Musica'], ['Alpha Centauri', 'Sol'], ['Alnair', 'Alpha Centauri'], ['Alnair', 'Ankaa'], ['Alnair', 'Muphrid'], ['Alnair', 'Tiaki'], ['Alnasl', 'Sabik'], ['Alnasl', 'Ascella'], ['Altair', 'Arcturus'], ['Altair', 'Fomalhaut'], ['Altair', 'Vega'], ['Ankaa', 'Denebola'], ['Ankaa', 'Sirius'], ['Antares', 'Ascella'], ['Antares', 'Larawag'], ['Arcturus', 'Muphrid'], ['Arcturus', 'Rasalhague'], ['Castor', 'Pollux'], ['Castor', 'Zaurak'], ['Deneb', 'Tarazed'], ['Denebola', 'Zosma'], ['Diphda', 'Fomalhaut'], ['Diphda', 'Hamal'], ['Diphda', 'Tau Ceti'], ['Fomalhaut', 'Sol'], ['Hamal', 'Phecda'], ['Larawag', 'Menkent'], ['Larawag', 'Peacock'], ['Menkent', 'Tiaki'], ['Nihal', 'Regulus'], ["Pollux", "Procyon"], ['Procyon', 'Ran'], ['Ran', 'Sirius'], ['Ran', 'Sol'], ['Ran', 'Tau Ceti'], ['Regulus', 'Zaurak'], ['Regulus', 'Zosma'], ['Sheratan', 'Tau Ceti']]

galaxy = Graph()
for i in star_systems:
    new_node = Node(i)
    galaxy.add_node(new_node)
for list in range(len(hyperlanes)):
    pointa = hyperlanes[list][0]
    pointb = hyperlanes[list][1]
    for i in range(len(galaxy.nodes)):
        if galaxy.nodes[i].get_value() == pointa:
            pointa_node = galaxy.nodes[i]
        elif galaxy.nodes[i].get_value() == pointb:
            pointb_node = galaxy.nodes[i]
    galaxy.add_edge(pointa_node,pointb_node)
print(galaxy.find_node('Sol').edges)

def shortest_path(s1_name, s2_name):
    s1_node = galaxy.find_node(s1_name)
    s2_node = galaxy.find_node(s2_name)
    visited = []
    to_visit = Queue()
    to_visit.enqueue([s1_node])
    while to_visit.size() > 0:
        path = to_visit.dequeue()
        if len(path) == 1:
            node_visiting = path[0]
        else:
            node_visiting = path[-1]
        print("visiting " + str(node_visiting))
        print("path " + str(path))
        for i in range(len(node_visiting.edges)):
            new_path = path + [node_visiting.edges[i]]
            if node_visiting.edges[i] in visited:
                print("this node has already been visited")
            else:
                new_path = path + [node_visiting.edges[i]]
                to_visit.enqueue(new_path)
        visited.append(node_visiting)
        if s2_node in visited:
            print("You have reached your destination")
            for i in range(len(path)):
                path[i] = path[i].get_value()

            return path
            break


result = shortest_path('Sol', 'Deneb')
if result == None:
    print("There is no path between these two systems")
else:
    print(result)

