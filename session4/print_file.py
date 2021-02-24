from pathlib import Path

FILENAME = "RNU6_269P.txt"
file_contents = Path(FILENAME).read_text() #Open and read the file
print(file_contents)