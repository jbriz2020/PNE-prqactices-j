from pathlib import Path

FILENAME = "RNU6-269P"
file_contents = Path(FILENAME).read_text() #Open and read the file
check = file_contents.find('\n')
print(file_contents[0:check])