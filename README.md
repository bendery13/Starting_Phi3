# Analyzing Google Pixel Phone Reviews

## Overview
&emsp; This program is a review rater for the Google Pixel smartphone. It runs the reviews for Pixel models four through eight by Microsoft's Phi-3 Language Model. The language model then rates the reviews as either positive, neutral, or negative. After each review is rated, the totals are tallied up and put into a bar graph to see how each model compares to the other Pixel models. This program may take a few minutes to run, as the language model is not quick, but it will show you which review it is looking at to show its progress. Since this program does use a language model, the responses may differ between runs, but it should stay fairly consistent.

## Installing Packages
&emsp; To use this program, you have two options for setting up your environment. First, you can create a virtual environment from the connected requirements.yaml file. Importing this file into a virtual environment will install all of the necessary dependencies for running the program. You can do this process by entering the following prompt into a command line. This command will create a virtual environment named 'my_yaml_env' - you can change the name of it by editing the prompt above. Once the virtual environment is created, you should be ready to run the program.

```
__conda create --name my_yaml_env --file requirement.yaml__ 
```
&emsp; Second, if the YAML file does not work or you do not have conda installed on your machine, you can also follow the steps below to manually install the necessary packages for the program. These steps will guide you through downloading Beautiful Soup, LXML, Matplotlib, Numpy, Ollama, Pytest, and Requests to your Python environment. Once you install these packages, you are ready to use the software. First, open up a command line in terminal, command prompt, or Powershell. Once you are in the command line, enter the following command and hit the enter key.

```
pip install ollama lxml requests beautifulsoup4 numpy matplotlib pytest
```
If you do have a Conda virtual environment, you can change 'pip' to 'conda' in the command above and it will install the packages in your environment rather than on your machine.

```
conda install ollama lxml requests beautifulsoup4 numpy matplotlib pytest
```

## Running The Program
&emsp; After each of the above packages has been installed, you are ready to use the program! This program first opens the review files that store the scraped smartphones reviews. It imports the reviews into a list that Phi-3 can more easier be fed to rate the sentiment of. Next, the program counts how many of each rating each smartphone was given by the language model. Lastly, a bar graph is created for each phone model with one bar for positive reviews, one for neutral reviews, and one for negative reviews.

&emsp; When the program is ran, each major step is output to the screen, so the user can see the progress the program has made. The langauge model is an extremely slow rater, so each review is shown as it is being rated by Phi-3. Once the language model is done rating every review, the program will display how many positive, neutral, and negative reviews each smartphone received. As the program is running, the user does not need to enter anything. The program will run by itself until completion.


## Data Analysis
&emsp; The results, according to the language model, were overwhelmingly positive. Each phone had a few negative and neutral reviews, but a majority of the reviews were rated positively. Each time the program runs, it rates the reviews slightly different. Despite this, the same trends are shown each time with an overwhelming amount of positive reviews. Below is one of the graphs that was created when I was running this program.

   ![Pixel Reviews](https://github.com/user-attachments/assets/352507cf-1ce1-4b97-aaad-5179b55c2973)
