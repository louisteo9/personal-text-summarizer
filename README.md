# Personal Text Summarizer
## Table of Contents
1. [Introduction](https://github.com/louisteo9/personal-text-summarizer#introduction)
2. [File Description](https://github.com/louisteo9/personal-text-summarizer#file-description)
3. [Installation](https://github.com/louisteo9/personal-text-summarizer#installation)
4. [Instructions](https://github.com/louisteo9/personal-text-summarizer#instructions)
5. [Acknowledgement](https://github.com/louisteo9/personal-text-summarizer#acknowledgement)
6. [Screenshot](https://github.com/louisteo9/personal-text-summarizer#screenshot)

## Introduction

In this project, I will show you how you can create your own personal text summarizer using Natural Language Processing (NLP) in Python.

You can read the post I published on Towards Data Science [here](https://towardsdatascience.com/report-is-too-long-to-read-use-nlp-to-create-a-summary-6f5f7801d355)<br/>

I used the text from a news article entitled Apple Acquires AI Startup For $50 Million To Advance Its Apps.

You can find the original news article [here](https://analyticsindiamag.com/apple-acquires-ai-startup-for-50-million-to-advance-its-apps/)

Below is the workflow that we will be following…

**_import text>> >> clean text and split into sentences >> remove stop words >> build word histogram>> rank sentences>> select top N sentences for summary_**

This project includes the complete Python script that you can use right away to summarize your text.

## File Description
**Personal Text Summarizer.ipynb** - Jupyter Notebook in preparation for text summarizer<br/>
**Apple_Acquires_AI_Startup.txt** - news in text file<br/>
**text_summarizer.py** - Python script for personal text summarizer<br/>

## Installation
Apart from NLTK (natural language toolkit) library, there should be no extra libraries required to install apart from those coming together with Anaconda distribution. The code should run with no issues using Python versions 3.5 and above.

#### Libraries used
NLTK, re, heapq, numpy, pandas, sys

## Instructions

a. Run this command in the project's root directory `python text_summarizer.py`<br/>
b. Enter the following inputs when prompted:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;1. Enter text file name: **_Apple_Acquires_AI_Startup.txt_**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;2. Enter output file name (e.g. summary.txt): **_summary.txt_**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;3. Enter max sentence word length (choose between 25 - 30): **_30_**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;4. Enter number of sentences you want in summary (choose between 3 - 5): **_3_**<br/>
c. Check your output file after 'Summarization task completed. Please check your output file.' message appears.

## Acknowledgement
[Next Edge Coding](https://www.udemy.com/user/bijoyan-das/) for inspiring me on how to create my personal text summarizer.

## Screenshot
![](https://github.com/louisteo9/personal-text-summarizer/blob/main/screenshots/algorithm%20in%20action.gif)
