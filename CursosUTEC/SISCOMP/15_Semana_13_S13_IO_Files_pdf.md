---
curso: SISCOMP
titulo: 15 - Semana 13/S13_ IO Files
slides: 8
fuente: 15 - Semana 13/S13_ IO Files.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
November 13th, 2025

                           S13: IO Files - Shell Scripts

       0. Getting some information

Getting information on file system usage (place your own information):

df
Filesystem     1K-blocks     Used Available Use% Mounted on
tmpfs            1615192     2420   1612772   1% /run
/dev/nvme0n1p2 982862268 98898256 833963680 11% /
tmpfs            8075948   213908   7862040   3% /dev/shm
tmpfs               5120       12      5108   1% /run/lock
efivarfs             246      117       125 49% /sys/firmware/efi/efivars
/dev/nvme0n1p1    523248     6352    516896   2% /boot/efi
tmpfs            1615188      344   1614844   1% /run/user/1001


Getting information on the disk (place your own information):

hwinfo --disk
27: PCI 00.0: 10600 Disk
  [Created at block.255]
  Unique ID: wLCS.EJHvc9MwvZ7
  Parent ID: yoMo.AxGd7hiuG+6
  SysFS ID: /class/block/nvme0n1
  SysFS BusID: nvme0
  SysFS Device Link: /devices/pci0000:00/0000:00:1d.4/0000:3d:00.0/nvme/nvme0
  Hardware Class: disk
  Model: "Samsung Electronics NVMe SSD Controller SM981/PM981/PM983"
  Vendor: pci 0x144d "Samsung Electronics Co Ltd"
  Device: pci 0xa808 "NVMe SSD Controller SM981/PM981/PM983"
  SubVendor: pci 0x144d "Samsung Electronics Co Ltd"
  SubDevice: pci 0xa801
  Driver: "nvme"
  Driver Modules: "nvme"
  Device File: /dev/nvme0n1
  Device Files: /dev/nvme0n1,
/dev/disk/by-id/nvme-SAMSUNG_MZVLB1T0HBLR-000L7_S4EMNF0MB29472,
/dev/disk/by-id/nvme-SAMSUNG_MZVLB1T0HBLR-000L7_S4EMNF0MB29472_1,
/dev/disk/by-path/pci-0000:3d:00.0-nvme-1, /dev/disk/by-diskseq/9,
/dev/disk/by-id/nvme-eui.0025388b91c8cf4e
  Device Number: block 259:0
  BIOS id: 0x80
  Drive status: no medium
  Config Status: cfg=new, avail=yes, need=no, active=unknown
  Attached to: #17 (Non-Volatile memory controller)
Getting information on a file and its file system (place your own information):

stat hello
  File: hello
  Size: 16048      ​ Blocks: 32        IO Block: 4096   regular file
Device: 259,2​Inode: 35260199   Links: 1
Access: (0775/-rwxrwxr-x) Uid: ( 1001/ andrewt)    Gid: ( 1001/ andrewt)
Access: 2025-04-14 19:29:20.651015096 +0300
Modify: 2025-04-14 19:29:16.426873736 +0300
Change: 2025-04-14 19:29:16.426873736 +0300
 Birth: 2025-04-14 19:29:16.384872282 +0300

stat hello --file-system
  File: "hello"
    ID: 2c46404543853cc9 Namelen: 255     Type: ext2/ext3
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 245715567 Free: 221037874 Available: 208537791
Inodes: Total: 62480384   Free: 61695470


Copying stdin to stdout, one byte at a time:

#include <unistd.h>

int main(void) {
    char c;
    while(read(STDIN_FILENO, &c, 1) != 0)
    write(STDOUT_FILENO, &c, 1);
    return 0;
}


Accessing file metadata:

#include <sys/stat.h>
#include <stdio.h>

int main (int argc, char **argv) {
    struct stat st;
    char *type, *readok;
    stat(argv[1], &st);
    if (S_ISREG(st.st_mode)) /* Determine file type */
        type = "regular";
    else if (S_ISDIR(st.st_mode))
        type = "directory";
    else
        type = "other";
    if ((st.st_mode & S_IRUSR)) /* Check read access */
        readok = "yes";
    else
        readok = "no";
    printf("type: %s, read: %s\n", type, readok);
    return 0;
}
Reading a directory to get the list of files (ls-like program):

#include <sys/types.h>
#include <dirent.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    DIR *directory;
    struct dirent *de;
    const char *dir_name = argv[1];
    if (!(directory = opendir(dir_name))) {
        perror("Failed to open directory");
        return 1;
    }
    while ((de = readdir(directory))) {
        printf("Found file: %s\n", de->d_name);
    }
    closedir(directory);
    return 0;
}


Buffering provided by the standard C library:
#include <stdio.h>

int main() {
    printf("h");
    printf("e");
    printf("l");
    printf("l");
    printf("o");
    printf("\n");
    fflush(stdout);
    return 0;
}


strace utility shows that many printf calls result in a single system call write:

strace -e trace=write ./hello
write(1, "hello\n", 6hello
)                  = 6
+++ exited with 0 +++


   1.​ Introduction
Shell allows creating simple scripts that run various Linux system utilities and connect them.
So, it is possible to automate solving tasks related to managing system resources.

From a practical point of view, a Shell script is an executable text file that can be run with a
command like this: interpreter script_file (e.g. sh script).

Also, there is a special marker «shebang» (#!/bin/sh) that specifies the interpreter to be
used to run the file. It is placed on the first line of a script. Then the script is given the
“execute” permission (chmod +x script). After that the script can be run simply like this:
acos@acos-vm:~$ ./script

Also, it is possible to run a Shell script from any directory if its directory is added to the
$PATH variable


acos@acos-vm:~$ export               PATH=directory_with_script:$PATH

After this the script can be called from directory in the following way:

acos@acos-vm:~$ script


   2.​ Examples

Input and Output

This script reads text into the A variable from the console (standard input) and then prints it
back to the console.

#!/bin/sh
read A
echo "$A"


The script below reads the user name from the standard input and greets the user with a
message containing the user name and the information about the system (returned by the
uname utility).

#!/bin/sh
read A
Sys=`uname`
echo "Hello, $A!
Welcome to $Sys!"



   3.​ Task 01:

Modify the previous program to get the user name from the system instead of reading the
input. Use the whoami utility to get the user name.


   4.​ Task 02:

Modify the previous program to store the message to be printed in a macro variable called
Msg. Pass the variable to the echo utility.
Command-Line Arguments
This script demonstrates the use of special symbols to access command-line arguments
passed to the interpreter.

#!/bin/sh
# $1, $2 … — command line argument 1, 2 ...
# $0 — name of the script itself
# $* — all command line arguments
# $# — number of command line arguments so
echo "$0"
echo "$1"

# ...

echo "$*"
echo "$#"



Conditions and Exit Status
When a utility is called from a Shell script, it is possible to interpret its exit status in a
conditional expression. For example, the script below calls the ls utility and prints “YES” only
if its status code is successful.

#!/bin/sh
if ls $*; then
     echo YES
else
     echo NO $?
fi


The script below redirects the output of the ls utility and prints it only if the status code of
the utility is successful.

#!/bin/sh
if ls $* -I out > out; then
     echo YES
     cat out
     rm -f out
else
     echo NO $?
fi


Using 2> /dev/null to redirect error messages out of a terminal:

acos@acos-vm:~$ ls nofile
ls: cannot access 'nofile': No such file or directory
acos@acos-vm:~$ ls nofile 2> err
acos@acos-vm:~$ cat err
ls: cannot access 'nofile': No such file or directory
acos@acos-vm:~$
      5.​ Task 03:

Rewrite the previous example so that it:

      ●​ outputs the content of ls after «YES» message if ls is successful;
      ●​ does not output an error message if ls is not successful.

Advanced Shell Features
The Shell language has features common for many programming languages such as
conditions, loops, and functions. For example the script below enumerates over a collection
of values:
#!/bin/sh

for n in 1 2 3 10 20 30 qwe asd xcv; do

       echo "Next value $n"

done

The script below defines a function that enumerates over a collection of its arguments.
Arguments of a function are accessed using special symbols in the same way as arguments
of the Shell script.
#!/bin/sh

fun() {

       echo "$0: $# $*"

       for arg; do

            echo "> $arg"

       done

}

fun 1 QWE "3 4"

fun "$*"

fun    $*

fun "$@"
   6.​ Task 04:

Create a program with the following structure:

#!/bin/sh

sum() {
    # insert your code here
}

while read a b; do
     sum $a $b
done


Then do the following:

   ●​ Note how read var1 var2 … varN works.
   ●​ Read documentation on expr and improve the program so that it prints the sum of
      $a and $b.
   ●​ Assume that the input is always correct.



   7.​ Other tasks:
   1.​ Experiments with the read builtin command.
            ●​ Research: What exit status the command read generates? Try it. Consult
               help read command instead of man read, because read is a Shell builtin
               and you got manual page on all Shell builtins.
            ●​ Research: How to suppress «\n» output after echo?
            ●​ Task: Write a script that asks user for name, and prints a welcome message
               either if a user has entered a name or not:
$ ./c8

Enter your name: Spot

Hello, Spot!

$ ./c8

Enter your name:

Hello, tmpuser?

   2.​ Read documentation on expr again. Write Shell script sumsum.sh that:
            ●​ has function sum() that:
                  ●​ sums all of its arguments (any number of arguments is permitted);
                  ●​ returns this sum if there are no errors;
                   ●​ returns 0 if there was an error (e.g. attempt to sum non-numbers);
            ●​ redirects all error messages to /dev/null;
            ●​ reads two lines of numbers;
            ●​ prints whether their sums were equal or not (0 values as a result of errors are
               considered equal).
$ ./sumsum.sh

1 3 5

2 4 6

Not equal

$ ./sumsum.sh

1 5 6

4 4 4

Equal

$ ./sumsum.sh

1 2 w

3 4 e

Equal

$ ./sumsum.sh

1 2 1

2 2 Q

Not equal

$ ./sumsum.sh

qwe 3 4

10 20 -30

Equal

Hint: errors can be checked using the $? symbol (status of the last command, must be 0 if
successful).

        8. References:

Chapters 8 and 10. [PGLC] Mark G. Sobell, Matthew Helmke. Practical Guide to Linux
Commands, Editors, and Shell Programming. 4th Edition. 2018.
