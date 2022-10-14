import io
import sys

import clipboard

# read
file = io.open("C:\\.keycache\\queue_paster.txt", mode='r', encoding='utf-8')
lines = file.readlines()
file.close()

# clipboard check
if len(lines) == 0:
    sys.exit("clipboard.txt is empty")

# recreate lines
count = 0
new_lines = []
copied = False
for i, line in enumerate(lines):
    # ignore empty line
    if len(line.replace('\n', '')) == 0:
        continue

    if copied == False:
        # set clipboard data
        clipboard.copy(lines[0].strip())
        print("clipboard: " + lines[0].strip())
        print("{}: {}".format(count, line.strip()))
        copied = True
        continue

    # print line
    print("{}: {}".format(count, line.strip()))
    count += 1
    new_lines.append(line)

# write
file = io.open('C:\\.keycache\\queue_paster.txt', mode='w', encoding='utf-8')
file.writelines(new_lines)
file.close()
