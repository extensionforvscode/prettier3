import queue

class Huffman_Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.frequency<other.frequency

def Huffman_Tree(character_array, frequency_array):
    pq = queue.PriorityQueue()

    for i in range(len(character_array)):
        new_node = Huffman_Node(character_array[i], frequency_array[i])
        pq.put(new_node)

    while pq.qsize()!=1:
        left = pq.get()
        right = pq.get()

        new_node = Huffman_Node("$", left.frequency+right.frequency)
        new_node.left = left
        new_node.right = right
        pq.put(new_node)

    return pq.get()

def print_codes(node, code):
    if node == None:
        return
    
    if node.character != "$":
        print(f"{node.character} - {code}")

    print_codes(node.left, code+"0")
    print_codes(node.right, code+"1")

if __name__ == "__main__":
    n = int(input("Enter number of unique characters in the message:- "))
    print("Enter the character - frequency pairs :- ")
    characters = []
    frequencies = []

    for i in range(n):
        pair = input().strip()
        char, freq = pair.split("-")
        characters.append(char)
        frequencies.append(int(freq))

    huffman_tree = Huffman_Tree(characters, frequencies)
    print("These are the codes :- ")
    print_codes(huffman_tree, "")
