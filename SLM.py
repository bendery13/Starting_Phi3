# Author: Ryan Bender

# This file is the sole file in this program. 
# Its main function reads in a text file and inputs the file's contents into the Phi-3 model.
# The model then responds to the contents in the file and posts them in another text file
import ollama

def main():
    # Opens the text file and reads the contents to the string variable fileInput
    with open("input1.txt", "r") as file:
        fileInput = file.read()

    # Opens another text file to paste the output in and asks Phi-3 the prompts from the first text file
    fileWrite = open("output1.txt", "w")
    fileInput += "Respond to my 3 statements in a numbered list and all additional information in a paragraph that is not in the list"
    
    # Ollama.generate asks the model the prompts and stores the data in the variable response
    response = ollama.generate(model='phi3', prompt= fileInput)
    fileWrite.write(response['response'])
    
    print("Response has been printed!")

if __name__ == "__main__":
    main()


