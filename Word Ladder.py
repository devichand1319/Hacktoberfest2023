from collections import defaultdict, deque

def construct_word_graph(word_list):
    word_graph = defaultdict(list)
    word_length = len(word_list[0])

    for word in word_list:
        for i in range(word_length):
            pattern = word[:i] + '*' + word[i + 1:]
            word_graph[pattern].append(word)

    return word_graph

def find_word_ladder(begin_word, end_word, word_list):
    if end_word not in word_list:
        return []

    word_graph = construct_word_graph(word_list)
    visited = set()
    queue = deque()
    queue.append((begin_word, [begin_word]))

    while queue:
        current_word, ladder = queue.popleft()
        for i in range(len(current_word)):
            pattern = current_word[:i] + '*' + current_word[i + 1:]
            for neighbor in word_graph[pattern]:
                if neighbor == end_word:
                    return ladder + [end_word]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, ladder + [neighbor]))

    return []

if __name__ == "__main__":
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    begin_word = "hit"
    end_word = "cog"

    shortest_ladder = find_word_ladder(begin_word, end_word, word_list)

    if shortest_ladder:
        print("Shortest Word Ladder:")
        print(" -> ".join(shortest_ladder))
    else:
        print("No word ladder exists.")
