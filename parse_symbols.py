import re, os, idc

name = 'test'
path = os.path.dirname(__file__)

save_file = open(r'%s\%s.txt' % (path, name), 'w')
save_file.write('--> auto parse symbols\n')

pattern = re.compile(r'0x([0-9A-Z]+)-->0x([0-9A-Z]+)')
with open(r'%s\%s.log' % (path, name), 'r') as file:
    for line in file:
        save_file.write(line.replace('\n', ''))
        items = pattern.search(line)
        if items:
            save_file.write('//' + idc.get_func_name(int(items.group(2), 16)))
        save_file.write('\n')

save_file.write('<-- auto parse symbols\n')
save_file.close()