# Personal Text Summarizer

## Description


I will show you how you can create your personal text summarizer using Natural Language Processing (NLP) in Python. 
I used the text from a news article entitled Apple Acquires AI Startup For $50 Million To Advance Its Apps. 
You can find the original news article here: https://analyticsindiamag.com/apple-acquires-ai-startup-for-50-million-to-advance-its-apps/

Below is the workflow that we will be following…
_import text>> >> clean text and split into sentences >> remove stop words >> build word histogram>> rank sentences>> select top N sentences for summary

## File Descriptions

personal text summarizer.ipynb - notebook file in preparation for text_summarizer.py.
Apple_Acquires_AI_Startup.txt - news in text file
text_summarizer.py - excuatable Python script for personal text summarizer

## Instructions

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.*.

a. Run the following commands in the project's root directory **python text_summarizer.py**
b. Enter the following inputs when prompted:
    1. Enter text file name: Apple_Acquires_AI_Startup.txt
    2. Enter output file name (e.g. summary.txt): summary.txt
    3. Enter max sentence word length (choose between 25 - 30): 30
    4. Enter number of sentences you want in summary (choose between 3 - 5): 3
c. Check your output file after 'Summarization task completed. Please check your output file.' message is appeared.
