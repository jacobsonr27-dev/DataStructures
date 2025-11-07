import random
import copy
class network:

    def __init__ (self):
        self.target = 7
        self.hand = []
        self.weights1 = []
        self.weights2 = []
        self.middle_weights = []
        self.values = []
        self.chosen_number = 'a'
        self.total_reward = 0
        self.reward = 0

    def create_nuerons(self):
        nodes_num1 = 5
        nodes_num2 = 3
        for i in range(nodes_num1):
            self.weights1.append(random.randint(-100,100)/100)
        for i in range(nodes_num1 * nodes_num2):
            self.middle_weights.append(random.randint(-100, 100) / 100)
        for i in range(nodes_num2):
            self.weights2.append(random.randint(-100,100)/100)



    def computer_choice(self):
        greatest_value = -100
        for i in self.values:
            if i > greatest_value:
                greatest_value = i
        for k in range(len(self.values)):
            if self.values[k] == greatest_value:
                self.chosen_number = self.hand[k]


    def hand_assignment(self):
        self.hand = []
        for i in range(5):
            self.hand.append(random.randint(1,14))

    def value_finding(self):
        self.values = []
        for s in self.hand:
            temp_middle_weights = self.middle_weights
            value = s
            layer1_values = []

            for i in range(len(self.weights1)):
                node_number = self.weights1[i] * value
                node_number = round(node_number, 4)
                layer1_values.append(node_number)

            layer2_values = []
            temp_middle_weights = self.middle_weights.copy()
            for i in range(len(self.weights2)):
                list = []
                for k in layer1_values:
                    temp_val = temp_middle_weights.pop()
                    node_number = temp_val * k
                    node_number = round(node_number, 4)
                    list.append(node_number)
                number = sum(list)
                number = round(number, 4)
                layer2_values.append(number)
            layer3_values = []
            for i in range(len(layer2_values)):
                node_number = layer2_values[i] * self.weights2[i]
                node_number = round(node_number, 4)
                layer3_values.append(node_number)
            final_value = sum(layer3_values)
            final_value = round(final_value, 10)
            self.values.append(final_value)


    def determine_reward(self):
        a_hand = self.hand
        a_target = self.target
        def closest_value(a_hand, a_target):
            return min(a_hand, key=lambda x: abs(x - a_target))
        if self.chosen_number == closest_value(self.hand,self.target):
            self.reward = 1
        else:
            self.reward = 0

    def test(self):
        for i in range(5):
            self.hand_assignment()
            self.value_finding()
            self.computer_choice()
            self.determine_reward()
            if self.reward == 1:
                self.total_reward = self.total_reward + 1


    def mutation(self):
        new_weights1 = []
        for j in range(len(self.weights1)):
            new_weights1.append(self.weights1[j] + (random.randint(-10, 10) / 100))
        self.weights1 = new_weights1

        new_weights2 = []
        for j in range(len(self.weights2)):
            new_weights2.append(self.weights2[j] + (random.randint(-10, 10) / 100))
        self.weights2 = new_weights2

        new_middle_weights = []
        for j in range(len(self.middle_weights)):
            new_middle_weights.append(self.middle_weights[j] + (random.randint(-10, 10) / 100))
        self.middle_weights = new_middle_weights




nets = {}
for i in range(20):
    var_name = f"net_{i}"
    value = network()
    nets[var_name] = value

for i in nets:
    nets[i].create_nuerons()
    nets[i].test()

average_total_reward = 0
while average_total_reward < 4.5:
    sum_total_reward = 0
    for i in nets:
        sum_total_reward = sum_total_reward + nets[i].total_reward
    average_total_reward = sum_total_reward/len(nets)
    print(average_total_reward)

    copy_nets = nets.copy()

    for i in range(len(nets)):
        if nets[f'net_{i}'].total_reward < average_total_reward:
            del copy_nets[f'net_{i}']
        elif nets[f'net_{i}'].total_reward == average_total_reward:
            if random.randint(1,3) == 1:
                del copy_nets[f'net_{i}']

    nets = copy_nets.copy()
    print(len(nets))

    if len(nets) < 30:
        copy_nets  = {}
        all_neural_networks = list(nets.keys())
        for i in range(len(nets)):
            copy_nets[f'net_{i}'] = nets[str(all_neural_networks[i])]
        nets = copy_nets.copy()
        #the for loop above takes the names of the keys in nets and renames them to start at 0 and count up by 1

        new_nets = {}

        for i in range(len(nets)):
            number_of_id = len(nets) + i
            new_nets[f'net_{number_of_id}'] = copy.deepcopy(nets[f'net_{i}'])
        #The for loop above takes a copy of each item in nets and assigns it to a new dict new_nets with a name in sequential order to nets

        for i in new_nets:
            new_nets[i].mutation()

        nets = {**nets,**new_nets}