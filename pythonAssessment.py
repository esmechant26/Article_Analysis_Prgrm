import re

# Open the article in read mode and save it to a variable
with open("/Users/esmechant/Desktop/SE/python/article_analysis/Article_Analysis_Prgrm/news_article.txt", "r") as file:
    article_text = file.read()

def count_specific_word(text, word):
    count = 0
    # Define punctuation to strip from words
    punctuation = '.,?!"""()'
    # Convert text to lowercase and split into words
    for w in text.lower().split():
        # Remove punctuation from the word
        cleaned_word = w.strip(punctuation)
        if cleaned_word == word.lower():
            count += 1

    return f"Word count of '{word}' = {count}"
print(count_specific_word(article_text, "The"))

def identify_most_common_word(text):
    if len(text) == 0:
        return "None"

    # Extract only valid alphanumeric words, converted to lowercase
    words = re.findall(r'\b\w+\b', text.lower())

    # Build a dictionary to count word frequencies
    word_count = {}
    index = 0
    while index < len(words):
        word = words[index]
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        index += 1

    # Find the word with the highest count
    most_common_word = ""
    max_count = 0
    for word in word_count:
        if word_count[word] > max_count:
            max_count = word_count[word]
            most_common_word = word

    return f'Most common word: {most_common_word}'

print(identify_most_common_word(article_text))

def calculate_average_word_length(text):
    # extract only valid alphanumeric words, converted to lowercase
    words = re.findall(r'\b\w+\b', text.lower())

    if len(words) == 0:
        return "None"

    # Calculate total character count across all words
    word_count = len(words)
    total_length = sum(len(word) for word in words)
    avg_word_length = total_length / word_count
    return (f'Average word length: {avg_word_length}')
print(calculate_average_word_length(article_text))

def count_paragraphs(text):
    # Split by two or more consecutive newlines to identify paragraphs
    paragraphs = re.split(r'\n\s*\n', text.strip())
    # Count non-empty paragraph blocks
    paragraph_count = len([p for p in paragraphs if p.strip()])
    return f"Total Paragraphs: {paragraph_count}"
print(count_paragraphs(article_text))

def count_sentences(text):
    # Pattern splits on . ! or ? while ignoring titles (Mr, Dr, Mrs, Ms, Inc)
    sentence_pattern = r'(?<!\bInc)(?<!\bDr)(?<!\bMr)(?<!\bMs)(?<!\bMrs)[\.!?]+(?:\s+|\n+)'
    raw_sentences = re.split(sentence_pattern, text)
    # Filter out empty strings and whitespace-only entries
    clean_sentences = [s.strip() for s in raw_sentences if s.strip()]
    return f"Total sentences: {len(clean_sentences)}"
print(count_sentences(article_text))