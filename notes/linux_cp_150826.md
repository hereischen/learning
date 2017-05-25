Notes 2015_08_24

# cp command in Linux/Unix

------

Copy from source to dest
```bash
$ cp [options] source dest
```
cp command main options:
| option    | description |
| ------    | -----       |   
| cp -a     | archive files|  
| cp -f     | force copy by removing the destination file if needed |
| cp -l     | interactive - ask before overwrite    |
| cp -n     | no file overwrite｜
| cp -R     | recursive copy (including hidden files)｜
| cp -v     | verbose - print informative messages ｜


##cp command examples
Copy single file main.c to destination directory bak:
```bash
$ cp main.c bak
```
 
Copy 2 files main.c and def.h to destination absolute path directory /home/usr/rapid/ :
```bash
$ cp main.c def.h /home/usr/rapid/
```
 
Copy all C files in current directory to subdirectory bak :
```bash
$ cp *.c bak
```
 
Copy directory src to absolute path directory /home/usr/rapid/ :
```bash
$ cp src /home/usr/rapid/
```
 
Copy all files and directories in dev recursively to subdirectory bak:
```bash
$ cp -R dev bak
```
 
Force file copy:
```bash
$ cp -f test.c bak
```
 
Interactive prompt before file overwrite:
```bash
$ cp -i test.c bak
cp: overwrite 'bak/test.c'? y
```
 
Update all files in current directory - copy only newer files to destination directory bak:
```bash
$ cp -u * bak
```
