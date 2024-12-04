import ollama
import matplotlib.pyplot as plt
import numpy as np
import pytest

"""
This project analyzes product reviews for five Google Pixel Models using the Phi-3 model to classify comments as positive, neutral, or negative. 
The results are saved in separate files for each device. The code is modular and object-oriented, with test cases written using pytest. 
A sentiment distribution graph is generated using Matplotlib to visualize the results.
"""


def main():
    reviewFiles = ('Pixel4_Reviews.txt', 'Pixel5_Reviews.txt', 'Pixel6_Reviews.txt', 'Pixel7_Reviews.txt', 'Pixel8_Reviews.txt')

    Pixel4List = openFile('Pixel4_Reviews.txt')
    Pixel5List = openFile('Pixel5_Reviews.txt')
    Pixel6List = openFile('Pixel6_Reviews.txt')
    Pixel7List = openFile('Pixel7_Reviews.txt')
    Pixel8List = openFile('Pixel8_Reviews.txt')


    """When running to rate the reviews again, change to 'r+' instead of r"""
    Rated4List = open("RatedPixel4.txt", 'r+', encoding="utf-8")
    Rated5List = open("RatedPixel5.txt", 'r+', encoding="utf-8")
    Rated6List = open("RatedPixel6.txt", 'r+', encoding="utf-8")
    Rated7List = open("RatedPixel7.txt", 'r+', encoding="utf-8")
    Rated8List = open("RatedPixel8.txt", 'r+', encoding="utf-8")

    """Save!!!!!! Uncomment when complete but this rates the reviews, but takes a long time"""
    rateReviews(Pixel4List, Rated4List)
    rateReviews(Pixel5List, Rated5List)
    rateReviews(Pixel6List, Rated6List)
    rateReviews(Pixel7List, Rated7List)
    rateReviews(Pixel8List, Rated8List)

    """Save!!!!!! Uncomment when complete but this rates the reviews, but takes a long time"""

    #These lines below count how many of each rating each Phone recieved and outputs it to screen
    pixel4Sentiment = Ratings.pullRatings("RatedPixel4.txt")
    print("\n Pixel 4")
    print(f'Positives: {pixel4Sentiment.get_positives()}')
    print(f'Neutrals: {pixel4Sentiment.get_neutrals()}')
    print(f'Negatives: {pixel4Sentiment.get_negatives()}')

    pixel5Sentiment = Ratings.pullRatings("RatedPixel5.txt")
    print("\n Pixel 5")
    print(f'Positives: {pixel5Sentiment.get_positives()}')
    print(f'Neutrals: {pixel5Sentiment.get_neutrals()}')
    print(f'Negatives: {pixel5Sentiment.get_negatives()}')

    pixel6Sentiment = Ratings.pullRatings("RatedPixel6.txt")
    print("\n Pixel 6")
    print(f'Positives: {pixel6Sentiment.get_positives()}')
    print(f'Neutrals: {pixel6Sentiment.get_neutrals()}')
    print(f'Negatives: {pixel6Sentiment.get_negatives()}')  

    pixel7Sentiment = Ratings.pullRatings("RatedPixel7.txt")
    print("\n Pixel 7")
    print(f'Positives: {pixel7Sentiment.get_positives()}')
    print(f'Neutrals: {pixel7Sentiment.get_neutrals()}')
    print(f'Negatives: {pixel7Sentiment.get_negatives()}')  

    pixel8Sentiment = Ratings.pullRatings("RatedPixel8.txt")
    print("\n Pixel 8")
    print(f'Positives: {pixel8Sentiment.get_positives()}')
    print(f'Neutrals: {pixel8Sentiment.get_neutrals()}')
    print(f'Negatives: {pixel8Sentiment.get_negatives()}')

    graphRatings(pixel4Sentiment, pixel5Sentiment, pixel6Sentiment, pixel7Sentiment, pixel8Sentiment)

    print("\nEnd of Main")


# This function opens a text file when it's name is passed in, and populated each review from the file into a list stored in the program
def openFile(fileName):
    returnList = []
    tempReview = "" 
    with open(fileName, 'r') as reviewFile:
        for line in reviewFile:
            line = line.strip()
            if (line != "-------------------------"):
                tempReview = tempReview + " " + line
            else:
                returnList.append(tempReview)
                tempReview = ""
    

    return returnList
            
# This function passes each review into the language model to have it be rated as 'Positive, Neutral, or Negative"
# After the review is rated, it is written into a text file
def rateReviews(rList, returnFile):
    for each in rList:
        instructions = ("Analyze the sentiment of the following text. Respond with **Exactly one word**: Positive, Neutral, or Negative. Do not provide any explanation, additional text, or context. Here is the text: ")
    
        instructions = instructions + each
        print(each)
        response = ollama.generate(model='wizardlm2', prompt = instructions)

        eval = response['response']
        #eval = eval.split()[0]
        print(eval)
        print("\n")
        returnFile.write(eval.strip() + "\n")

# This class manages the rated reviews and allows them to be easily stores for each phone
class Ratings:
    def __init__(self, positives=0, neutrals=0, negatives=0):
        self.positives = positives
        self.neutrals = neutrals
        self.negatives = negatives

    def add_positive(self):
        self.positives += 1

    def add_neutral(self):
        self.neutrals += 1

    def add_negative(self):
        self.negatives += 1

    def get_positives(self):
        return self.positives

    def get_neutrals(self):
        return self.neutrals

    def get_negatives(self):
        return self.negatives   
   
    #This function passes through a text file and counts how many positive, neutral, and negative reviews each phone recieved
    @staticmethod
    def pullRatings(fileName):
        temp = Ratings()

        tempFile =  open(fileName, "r", encoding='utf-8')

        for line in tempFile:
            if "Positive" in line or "positive" in line:
                temp.add_positive()
                continue
            elif "Neutral" in line or "neutral" in line:
                temp.add_neutral()
                continue
            elif "Negative" in line or "negative" in line:
                    temp.add_negative()
                    continue
        return temp

#This function uploads the data into a graph to be easily seen by a user
def graphRatings(ratedSentiment4, ratedSentiment5, ratedSentiment6, ratedSentiment7, ratedSentiment8):
    items = ["Pixel 4", "Pixel 5", "Pixel 6", "Pixel 7", "Pixel 8"]
    values1 = [ratedSentiment4.get_negatives(), ratedSentiment5.get_negatives(), ratedSentiment6.get_negatives(), ratedSentiment7.get_negatives(), ratedSentiment8.get_negatives()]
    values2 = [ratedSentiment4.get_positives(), ratedSentiment5.get_positives(), ratedSentiment6.get_positives(), ratedSentiment7.get_positives(), ratedSentiment8.get_positives()]
    values3 = [ratedSentiment4.get_neutrals(), ratedSentiment5.get_neutrals(), ratedSentiment6.get_neutrals(), ratedSentiment7.get_neutrals(), ratedSentiment8.get_neutrals()]

    x = np.arange(len(items))
    width = 0.25

    # Plot bars
    plt.bar(x - width, values1, width, label='Negatives')
    plt.bar(x, values2, width, label='Positives')
    plt.bar(x + width, values3, width, label='Neutrals')

    # Customize
    plt.xlabel("Phone Models Reviewed")
    plt.ylabel("Number of Reviews")
    plt.title("Google Pixel Reviews")
    plt.xticks(x, items)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Display
    plt.tight_layout()
    plt.show()

    
if __name__ == "__main__":
    main()