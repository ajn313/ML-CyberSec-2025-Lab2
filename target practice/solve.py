from pwn import ELF

elf = ELF('./target_practice')
cat_flag_addr = elf.symbols['cat_flag']
print(hex(cat_flag_addr))