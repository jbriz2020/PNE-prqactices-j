from pathlib import Path

FILENAME = "ADA"
file_contents = Path(FILENAME).read_text() #Open and read the file
check = file_contents.find('\n')
seq = ((file_contents[check:]).replace('\n',''))
print(len(seq))
