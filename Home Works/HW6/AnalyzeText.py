import string


def get_count(item):
    return item[1]

# Function: create_dictionary
def create_dictionary(filename):
    
    word_dict = {}
    
    total_words = 0
    unique_words = 0
    
    with open(filename, "r") as file:
        for line in file:
            line = line.lower()
        
        for p in string.punctuation:
            line = line.replace(p, "")
            
        words = line.split()
        
        for word in words:
            
            if word.isdigit():
                continue
                
            total_words += 1
            
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
                
    unique_words = len(word_dict)
    
    file.close()
    
    return total_words, unique_words, word_dict


# Function: most_frequent_words
def most_frequent_words(word_dict, k):
    
    # استخدمنا الدالة البسيطة get_count للترتيب
    sorted_words = sorted(word_dict.items(), key=get_count, reverse=True)
    
    result = []

    for i in range(min(k, len(sorted_words))):
        result.append(sorted_words[i])
        
    return result


# Function: longest_words
def longest_words(word_dict, k):
    
    words_list = list(word_dict.keys())
    words_list.sort(key=len, reverse=True)
    
    return words_list[:k]


# Function: shortest_words
def shortest_words(word_dict, k):
    
    words_list = list(word_dict.keys())
    words_list.sort(key=len)
    
    return words_list[:k]


def main():
    
    filename = input("Enter filename: ")
    
    total_words, unique_words, word_dict = create_dictionary(filename)
    
    if total_words == 0:
        return

    # Total words
    print(f"Total words: {total_words}")
    
    # Unique words
    print(f"Unique words: {unique_words}")
    
    # Top 10 frequent words
    print("\nTop 10 frequent words:")
    top_freq = most_frequent_words(word_dict, 10)
    for word, count in top_freq:
        print(f"{word} {count}")
        
    # Top 10 longest words
    print("\nTop 10 longest words:")
    top_longest = longest_words(word_dict, 10)
    for word in top_longest:
        print(word)
        
    # Top 10 shortest words
    print("\nTop 10 shortest words:")
    top_shortest = shortest_words(word_dict, 10)
    for word in top_shortest:
        print(word)

if __name__ == "__main__":
    main()