extract the rpm content to the current directory
```
$ sudo apt-get/yum install rpm2cpio
$ rpm2cpio /path/to/file.rpm | cpio -i --make-directories
```