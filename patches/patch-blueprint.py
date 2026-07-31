import sys, re
with open(sys.argv[1]) as f:
    lines = f.readlines()
new_lines = []
skip = False
brace_depth = 0
for line in lines:
    if 'Adw.ShortcutsDialog help_overlay' in line:
        skip = True
        brace_depth = 0
    if skip:
        brace_depth += line.count('{') - line.count('}')
        if brace_depth <= 0 and skip:
            skip = False
            continue
        continue
    if '"win.show-help-overlay"' in line:
        continue
    new_lines.append(line)
with open(sys.argv[1], 'w') as f:
    f.writelines(new_lines)
