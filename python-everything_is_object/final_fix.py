import os

# Dictionary of all .txt files and their required content
files = {
    "0-answer.txt": "type",
    "1-answer.txt": "id",
    "2-answer.txt": "No",
    "3-answer.txt": "Yes",
    "4-answer.txt": "Yes",
    "5-answer.txt": "No",
    "6-answer.txt": "True",
    "7-answer.txt": "True",
    "8-answer.txt": "True",
    "9-answer.txt": "False",
    "10-answer.txt": "True",
    "11-answer.txt": "False",
    "12-answer.txt": "True",
    "13-answer.txt": "True",
    "14-answer.txt": "[1, 2, 3, 4]",
    "15-answer.txt": "[1, 2, 3]",
    "16-answer.txt": "1",
    "17-answer.txt": "[1, 2, 3, 4]",
    "18-answer.txt": "[1, 2, 3]",
    "20-answer.txt": "Yes",
    "21-answer.txt": "Yes",
    "22-answer.txt": "No",
    "23-answer.txt": "Yes",
    "24-answer.txt": "True",
    "25-answer.txt": "False",
    "26-answer.txt": "True",
    "27-answer.txt": "No",
    "28-answer.txt": "Yes"
}

for filename, content in files.items():
    # 'wb' mode writes binary, ensuring NO extra characters are added by Windows
    with open(filename, "wb") as f:
        # We encode to utf-8 and write WITHOUT a newline at the end
        f.write(content.encode("utf-8"))

print("Files re-written in binary mode to prevent Windows formatting issues.")
