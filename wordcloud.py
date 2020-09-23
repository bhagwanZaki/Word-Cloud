import wordcloud
from matplotlib import pyplot as plt


fname = input("Enter file name: ")
file= open(fname,"r",encoding='utf-8') 
file_contents = file.read()

def calculate_frequencies(file_contents):

    # Here is a list of punctuations and uninteresting words that will be discarded from the file
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each","for","I","on","not","in","The","so","may","us", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # Cleaning of txt file
    non_punctuation_text=""
    for char in file_contents:
        if char not in punctuations:
            non_punctuation_text=non_punctuation_text+char
    words=non_punctuation_text.split()
    clean_words=[]
    frequencies={}
    for word in words:
        if word.isalpha():
            if word not in uninteresting_words:
                clean_words.append(word)
    for alpha_word in clean_words:
        if alpha_word not in frequencies:
            frequencies[alpha_word]=1
        else:
            frequencies[alpha_word]+=1
        
        
    #wordcloud formation
    cloud = wordcloud.WordCloud(width = 800, height = 800, 
                background_color ='white')
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()