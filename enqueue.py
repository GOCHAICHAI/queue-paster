import clipboard
import io

# get clipboard data
clipboard = clipboard.paste()
print("clipboard: " + clipboard)

# read
file = io.open('C:\.keycache\queue_paster.txt', mode='r', encoding='utf-8')
lines = file.readlines()
file.close()

# recreate lines
count = 0
new_lines = []
new_lines.append(clipboard + "\n")  # add current clipboard at the fist place
print("{}: {}".format(count, clipboard))

for i, line in enumerate(lines):
    # ignore empty line
    if len(line.replace('\n', '')) == 0: continue

    # print line
    count += 1
    print("{}: {}".format(count, line.strip()))
    new_lines.append(line)

# write
file = io.open('C:\.keycache\queue_paster.txt', mode='w', encoding='utf-8')
file.writelines(new_lines)
file.close()
