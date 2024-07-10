# bookbot
A Bookbot guided project from BootDotDev

BookBot
Introduction
BookBot is a simple yet functional program designed to analyze the contents of a book provided as a text file (.txt). It calculates the word count and character count for all alphabetical characters, displaying them in descending order of occurrence.

Features
Word Count: Calculates the total number of words in the book.
Character Count: Counts the occurrences of each alphabetical character (case-insensitive) and displays them in descending order.
Statistics Report: Provides a comprehensive report with word and character counts.
Installation
Clone the repository:
```bash
git clone https://github.com/j-ayebare/BookBot.git
```
Navigate to the project directory:
```bash
cd BookBot
```
Usage
Ensure the book text file (e.g., frankenstein.txt) is located in the books directory within the project.
Run the script:
```bash
python bookbot.py
```
View the output: The program will print the word count and character count statistics to the console.
Example
Given a book text file (frankenstein.txt) located in the books directory with some content, running the script:
```bash
python bookbot.py
```
Will produce output similar to:
```sql
--- Begin report of books/frankenstein.txt ---
[Number of words] words found in the document

The 'e' character was found [count] times
The 't' character was found [count] times
...
--- End report ---
```
Code Overview
Here's a brief overview of the main functions in the script:

main(): The entry point of the program. It defines the book path, reads the book text, and prints the report.
get_book_text(path): Reads the text from the given book path.
get_num_words(text): Calculates and returns the number of words in the text.
get_num_char(text): Calculates and returns a dictionary with the count of each alphabetical character in the text.
print_report(text, book_path): Prints the report, including the word count and sorted character counts.
get_value(d): Helper function to extract the value from a dictionary for sorting purposes.

Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to create a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or feedback, please contact jeremiahayebare@gmail.com.
