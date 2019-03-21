from elftools.elf.elffile import ELFFile

#coding: Non-ASCII
print("WELCOME TO TOOL SECTIONS BY JOAS ANTONIO")

with open('./chall.elf', 'rb') as f: #change the file name to what you are performing reverse engineering
    e = ELFFile(f)
    for section in e.iter_sections():
        print(hex(section[’sh_addr’]), section.name)
