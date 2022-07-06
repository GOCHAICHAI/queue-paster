import sys
import clipboard
import io

# read
file = io.open("C:\.keycache\\queue_paster.txt", mode='r', encoding='utf-8')
lines = file.readlines()
file.close()

# clipboard check
if len(lines) == 0:
    sys.exit("clipboard.txt is empty")

# set clipboard data
clipboard.copy(lines[0].strip())
print("clipboard: " + lines[0].strip())

# recreate lines
count = 0
new_lines = []
for i, line in enumerate(lines):
    # ignore first line
    if i == 0: continue

    # ignore empty line
    if len(line) == 0: continue

    # print line
    print("{}: {}".format(count, line.strip()))
    count += 1
    new_lines.append(line)

# write
file = io.open("C:\\.keycache\\queue_paster.txt", mode='w', encoding='utf-8')
file.writelines(new_lines)
file.close()
