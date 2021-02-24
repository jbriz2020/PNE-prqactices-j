from pathlib import Path

FILENAME = "U5"
file_contents = Path(FILENAME).read_text() #Open and read the file
check = file_contents.find('\n')
print(file_contents[(check + 1):-1])