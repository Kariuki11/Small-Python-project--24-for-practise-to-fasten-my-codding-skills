with open("story.txt", "r") as f:
    story = f.read()
    
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"
    
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
        
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.append(word)
        start_of_word = -1
        
print(words)
    