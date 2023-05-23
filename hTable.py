# CS331 Assignment 4, 02/21/2023

# In this assignment, you are asked to implement methods in the HashTable class.
# In our design, we use Singly LinkedLists to handle collisions.
# And we keep a list that contains all the keys stored in the data structure.
# You may assume that all keys and values are strings.

class HashTable:

    # Please implement each of the following methods following the guide.
    # Here, I've only implemented the construction methods and the dunder __repr__ method. Do not change them.

    class Node:

        def __init__(self, key, value, next = None):
            # Inside each node, there are three attributes
            # 1. self.key stores a string as the key
            # 2. self.value stores a string as value
            # 3. self.next is a pointer that points to the next node

            ####################    DO NOT CHANGE   ####################
            self.key = key
            self.value = value
            self.next = next

    def __init__(self, n = 1000):
        # A new HashTable contains an array of size n containing only None
        # A new HashTable also contains a list (empty initially) to store all the keys stored in the HashTable.

        ####################    DO NOT CHANGE   ####################
        self.table = [None] * n
        self.keys = []

    def __len__(self):
        # This method implements "len(HashTable)".
        # return the number of keys stored in the data structure.
        return len(self.keys)
        pass

    def __setitem__(self, key, value):
        # This method implements "HashTable[key] = value"
        # Use hash(key) % len(self.table) as the index for the key:value pair.
        # Wrap the key:value pair into a node.
        # If key is new, store this node into the LinkedList (could be empty) stored in self.table[index].
        # Note that, the node does not have to be linked to the tail of that list.
        # Remind that, if the key is new, you also need to append the key to self.keys.
        # If key is not new, update the old corresponding value to the new one.
        index = hash(key) % len(self.table)
        node = HashTable.Node(key, value)
        spot = self.table[index]
        flag = False
        while spot is not None and flag is False:
            if spot.key == key:
                spot.value = value
                flag = True
            else:
                spot = spot.next
        if flag is False:
            node.next = self.table[index]
            self.table[index] = node
            self.keys.append(key)
        pass

    def __getitem__(self, key):
        # This method implements "HashTable[key]"
        # You may assume that the key is in the HashTable.
        # Return the corresponding value of the input key.
        # It can only appear in self.table with index = hash(key) % len(self.table).

        # You may also consider a design where the input key might not be in the HashTable.
        # If key is in the HashTable, return the corresponding value of the input key.
        # if key is not in the HashTable, raise KeyError(key).
        index = hash(key) % len(self.table)
        spot = self.table[index]
        while spot is not None:
            if spot.key == key:
                return self.table[index].value
            else:
                spot = spot.next
        raise KeyError(key)
        pass

    def __contains__(self, key):
        # This method implements "key in HashTable"
        # Return a boolean that represents whether key is in the HashTable.
        # Note that, DO NOT "return key in self.keys", because it needs O(k) time (if there are k keys).
        # This operation is expected to have a constant running time.
        index = hash(key) % len(self.table)
        spot = self.table[index]
        if spot is not None and spot.key == key:
            return True
        else:
            return False
        pass

    def __iter__(self):
        # This method implements "for key in HashTable"
        # Yield each key in self.keys
        for x in self.keys:
            yield x
        pass

    def __repr__(self):
        # This method implements "print(HashTable)"

        ####################    DO NOT CHANGE THIS  ####################
        return "{" + ', '.join(repr(key) + ':' + repr(self[key]) for key in self) + "}"


########################################################################################################################
######################################                                      ############################################
######################################     DO NOT CHANGE ANYTHING BELOW     ############################################
######################################                                      ############################################
########################################################################################################################

print("Let's create a HashTable to store letters in the phonetic alphabet.")

ht1 = HashTable(10)
ht1["a"] = "Alfa"
ht1["b"] = "Bravo"
ht1["c"] = "Charlie"
print(ht1["a"])
print("We start with a HashTable with only 10 spots and then store the first three letters, "
      "ht1 =", ht1, ".")
print("In the phonetic alphabet, \'c\' is for", ht1["c"],".")

ht1["a"] = "Alpha"
print("We change the spelling of word \'Alfa\' to \'Alpha\', then ht1 =", ht1, ".")

print("Does ht1 contain letter \'d\'? The answer is", "d" in ht1, ".")
ht1["d"] = "Delta"
ht1["e"] = "Echo"
ht1["f"] = "Foxtrot"
ht1["g"] = "Golf"
ht1["h"] = "Hotel"
ht1["i"] = "India"
ht1["j"] = "Juliett"
ht1["k"] = "Kilo"
print("To test whether collisions are handled correctly, "
      "we keep inserting eight more letters.")
print("Since there are 10 spots and", len(ht1) ,"letters, by pigeonhole principle, a collision is guaranteed.")
print("Now, ht1 becomes", ht1, ".")
