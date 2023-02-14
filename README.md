# OpenAI Study Guide Creator

This Python script generates a study guide for a given topic using the OpenAI GPT API.

## Requirements

- Python 3.6 or higher
- OpenAI API key

## Installation

1. Clone this repository: `git clone https://github.com/your_username/OpenAI-study-guide-creator.git`
2. Navigate to the repository: `cd OpenAI-study-guide-creator`
3. Install the required packages: `pip install openai`

## Usage

1. Run the script: `python main.py`
2. Enter your OpenAI API key when prompted.
3. Enter the topic you want to learn about.
4. Enter the number of hours you want to spend learning this topic.
5. Enter your experience level with this topic on a scale of 1-10.
6. Enter a file name to save the study guide to (without extension).
7. The script will generate a study guide and save it to a Markdown file with the specified file name.

## Output

The generated study guide will consist of a course overview and a number of parts, categories, or steps, depending on the topic and the user's inputs.

Each part, category, or step will be presented to the user one at a time. For each part, the user can choose to learn the next section or ask the GPT API for more information.

If the user chooses to ask the GPT API for more information, they will be prompted to enter an additional prompt to send to the API. The response from the API will be appended to the course material for that part and saved as a comment in the Markdown file.

## Example

Here is an example of the output generated by the script:

# Study Guide for Learning About Python

Time available: 10 hours

Experience level: 5/10

## Course Overview

In this study guide, you will learn the basics of the Python programming language. The guide is divided into three parts:

Part 1: Python syntax and data types

Part 2: Control structures and functions

Part 3: Object-oriented programming

### Part 1: Python syntax and data types

Learning...

Python is a high-level programming language that is easy to learn and use. It has a clean syntax and can be used for a wide variety of tasks, from web development to data analysis.

Enter 'n' for the next section or 'a' to ask GPT API: a

Enter a prompt for the GPT API: What are the advantages of using Python for data analysis?

Python is a popular choice for data analysis because it has a wide variety of libraries and tools for working with data. Some of the advantages of using Python for data analysis include:

- It is easy to learn and use
- It has a large and active community of users and developers
- It has a wide variety of libraries and tools for working with data, including NumPy, Pandas, and Matplotlib
- It can be used for a wide range of data analysis tasks, from data cleaning to machine learning

<!-- GPT API response to 'What are the advantages of using Python for data analysis?': -->\nPython is a popular choice for data analysis because it has a wide variety of libraries and tools for working with data. Some of the advantages of using Python for data analysis include:\n\n- It is easy to learn and use\n- It has a large and active community of users and developers\n- It has a wide variety of libraries and tools for working with data, including NumPy, Pandas, and Matplotlib\n- It can be used for a wide range of data analysis tasks, from data cleaning to
