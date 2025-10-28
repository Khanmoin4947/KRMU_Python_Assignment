def clean_text(text): 
    """Clean and normalize text for analysis.""" 
    import string 
    # Remove punctuation and convert to lowercase 
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator).lower() 
 
def count_words(text): 
    """Count total words in text.""" 
    words = text.split() 
    return len(words) 
 
def count_sentences(text): 
    """Count sentences in text.""" 
    sentence_endings = text.count('.') + text.count('!') + text.count('?') 
    return max(1, sentence_endings)  # At least 1 sentence 
 
def count_paragraphs(text): 
    """Count paragraphs in text.""" 
    paragraphs = text.split('\n\n') 
    return len([p for p in paragraphs if p.strip()]) 
 
def get_word_frequency(text): 
    """Get frequency of each word.""" 
    clean = clean_text(text) 
    words = clean.split() 
     
    frequency = {} 
    for word in words: 
        if word:  # Skip empty strings 
            frequency[word] = frequency.get(word, 0) + 1 
     
    return frequency 
 
def get_most_common_words(word_freq, n=10): 
    """Get n most common words.""" 
    # Sort by frequency (descending) and return top n 
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], 
reverse=True) 
    return sorted_words[:n] 
 
def get_unique_words(text): 
    """Get set of unique words.""" 
    clean = clean_text(text) 
    words = clean.split() 
    return set(word for word in words if word) 
 
def calculate_reading_stats(text): 
    """Calculate reading difficulty statistics.""" 
    word_count = count_words(text) 
    sentence_count = count_sentences(text) 
     
    if sentence_count == 0: 
        return {} 
     
    avg_words_per_sentence = word_count / sentence_count 
     
    # Count syllables (simplified) 
    def count_syllables(word): 
        vowels = "aeiou" 
        syllables = sum(1 for char in word.lower() if char in vowels) 
        return max(1, syllables)  # At least 1 syllable per word 
     
    clean = clean_text(text) 
    words = clean.split() 
    total_syllables = sum(count_syllables(word) for word in words if word) 
    avg_syllables_per_word = total_syllables / word_count if word_count > 0 else 0
    return { 
            "avg_words_per_sentence": avg_words_per_sentence, 
            "avg_syllables_per_word": avg_syllables_per_word, 
            "total_syllables": total_syllables 
        } 
 
def analyze_text(text): 
    """Main function to analyze text and return comprehensive report.""" 
    if not text.strip(): 
        return "No text to analyze." 
     
    # Basic counts 
    word_count = count_words(text) 
    sentence_count = count_sentences(text) 
    paragraph_count = count_paragraphs(text) 
     
    # Word analysis 
    word_freq = get_word_frequency(text) 
    unique_words = get_unique_words(text) 
    most_common = get_most_common_words(word_freq, 5) 
     
    # Reading statistics 
    reading_stats = calculate_reading_stats(text) 
     
    # Generate report 
    report = f""" 
TEXT ANALYSIS REPORT 
{'='*50} 
 
BASIC STATISTICS: - Words: {word_count} - Sentences: {sentence_count} - Paragraphs: {paragraph_count} - Unique words: {len(unique_words)} - Vocabulary richness: {len(unique_words)/word_count*100:.1f}% 
 
READING STATISTICS: - Average words per sentence: {reading_stats.get('avg_words_per_sentence', 
0):.1f} - Average syllables per word: {reading_stats.get('avg_syllables_per_word', 
0):.1f} 
 
MOST COMMON WORDS:""" 
     
    for word, count in most_common: 
        report += f"\n- '{word}': {count} times" 
     
    return report 
 
def main(): 
    print("Text Analysis Tool") 
    print("="*50) 
     
    # Get text input 
    text = input("Enter text to analyze (or paste multi-line text): ") 
     
    if not text.strip(): 
        print("No text provided. Please try again.") 
        return 
     
    # Analyze and display results 
    result = analyze_text(text) 
    print(result) 
 
if __name__ == "__main__": 
    main()