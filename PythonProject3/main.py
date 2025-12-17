from binarytree import *
fa = open("saved_tree.txt", "a") # This creates the file if it
fa.close() 				 # doesn’t exist yet
fr = open("saved_tree.txt", "r")
old_tree = fr.read() # This is the string representing the old tree
fr.close()

def yes_or_no():
    user_input = str(input())
    if user_input == 'yes':
        return str(user_input)
    elif user_input == 'no':
        return str(user_input)
    else:
        print('Please enter yes or no')
        return yes_or_no()

def play_game():
    current_node = root_node
    this = True
    while this == True:
        if current_node.is_leaf() == False:
            print(str(current_node.get_value()))
            response = yes_or_no()
            if response == 'yes':
                current_node = current_node.get_left()
            elif response == 'no':
                current_node = current_node.get_right()
        else:
            print("I know, I guess " + str(current_node.get_value()))
            print("Did I get this correct?")
            response = yes_or_no()
            if response == 'yes':
                this = False
            elif response == 'no':
                print("What were you thinking of?")
                new_leaf = input()
                print("What question could I have asked before guessing to help me tell the difference?")
                new_question = input()
                print("Would you have answered yes or no to that question if you were thinking of " + new_leaf + "?")
                answer = yes_or_no()
                old_value = current_node
                current_node.set_value(new_question)
                if answer == 'yes':
                    current_node.set_left(Node(new_leaf))
                    current_node.set_right(Node(old_value))
                elif answer == 'no':
                    current_node.set_right(Node(new_leaf))
                    current_node.set_left(Node(old_value))
                this = False
            this = False

    print("Would you like to play again")
    response = yes_or_no()
    if response == 'yes':
        return play_game()
    elif response == 'no':
        print("Would you like to save the tree?")
        response = yes_or_no()
        if response == 'yes':
            fw = open("saved_tree.txt", "w")
            fw.write(str(game_tree))
            fw.close()
        elif response == 'no':
            print("ok")
        return

print("Would you like to enter a custom tree?")
response = yes_or_no()
if response == 'yes':
    tree = old_tree
    game_tree = BinaryTree(s = tree)
    root_node = game_tree.get_root()
else:
    root_node = Node('Does it have 4 legs?')
    game_tree = BinaryTree(root_node)
    root_node.set_left(Node('Does it have pointy ears?'))
    root_node.set_right(Node('Can it swim?'))
    root_node.get_left().set_left(Node('cat'))
    root_node.get_left().set_right(Node('dog'))
    root_node.get_right().set_left(Node('fish'))
    root_node.get_right().set_right(Node('parrot'))


play_game()

