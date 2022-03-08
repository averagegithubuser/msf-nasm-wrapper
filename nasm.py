import sys
import subprocess
from colorama import Fore, Style

class Nasm:

    def __init__(self, fname):
        
        self.fname = fname

    def shellcode_generator(self):

        shellcode = []

        nasm = subprocess.Popen(f"msf-nasm_shell < {self.fname}", 
                shell=True,
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT,
                encoding='utf-8')

        for asm in nasm.stdout.readlines():
            if "0"*8 in asm:  
                shellcode.append(asm)
        
        retval = nasm.wait()
        return shellcode

    def shellcode_parser(self):

        shellcode = nasm.shellcode_generator()
        asm = []

        for x in shellcode:
            op_codes = str.split(x)
            asm.append(op_codes[1])

        string = ''.join(asm)
        shellcode = '\\x' + '\\x'.join(string[i:i + 2] for i in range(0, len(string), 2))
        
        return shellcode

    def shellcode_display(self):

        shellcode = nasm.shellcode_parser()

        print(f'{Fore.GREEN}shellcode is ready to be deployed{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}"{shellcode}"{Style.RESET_ALL}')


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(f"{Fore.RED}usage: py nasm.py <filename>{Style.RESET_ALL}")
        sys.exit()

    fname = sys.argv[1]
    nasm = Nasm(fname)
    nasm.shellcode_display()
