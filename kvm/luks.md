Create luks-inside-qcow2 image
```bash
qemu-img create --object secret,id=sec0,data=base -f qcow2 -o encrypt.format=luks,encrypt.key-secret=sec0 base.qcow2 20G
```

## Boot a guest and install OS on the image.
Block driver node as ‘-drive’
```
    --object secret,id=sec0,data=base \
    -device virtio-scsi-pci,id=virtio_scsi_pci0,bus=pci.0,addr=0x3 \
    -drive id=drive_image1,if=none,snapshot=off,aio=threads,cache=none,format=qcow2,file=/home/tests/diskfile/base.qcow2,encrypt.key-secret=sec0 \
    -device scsi-hd,id=image1,drive=drive_image1 \
```

Block driver node as ‘-blockdev’
```
    -object secret,id=sec0,data=`printf %s "redhat" |base64`,format=base64 \
    -blockdev driver=qcow2,cache.direct=off,cache.no-flush=on,file.filename=/home/rhel7.5-64-virtio.qcow2,node-name=node1,key-secret=sec0,file.driver=file \
    -device virtio-blk-pci,drive=node1,bootindex=1,bus=pci.0,addr=0x3 \
```


## Check the image
```bash
qemu-img check --object secret,id=sec0,data=base --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2
```

## Create snapshot
```bash
qemu-img create --object secret,id=sec0,data=base --object secret,id=sec1,data=snapshot -f qcow2 -o encrypt.format=luks,encrypt.key-secret=sec1 -b 'json:{"encrypt.key-secret": "sec0", "driver": "qcow2", "file": {"driver": "file", "filename": "/home/tests/nfsclient/base.qcow2"}}' sn.qcow2
```

## Boot snapshot
```
    --object secret,id=sec0,data=base \
    --object secret,id=sec1,data=snapshot \
    -device virtio-scsi-pci,id=virtio_scsi_pci0,bus=pci.0,addr=0x4 \
    -drive id=drive_image1,if=none,snapshot=off,aio=threads,cache=none,format=qcow2,file=/home/tests/nfsclient/sn.qcow2,encrypt.key-secret=sec1,backing.encrypt.key-secret=sec0 \
    -device scsi-hd,id=image1,drive=drive_image1,bootindex=0 \
```
## Snapshot chain
snA
Create snA:
```bash
qemu-img create --object secret,id=sec0,data=base --object secret,id=secA,data=snA -f qcow2 -o encrypt.format=luks,encrypt.key-secret=secA -b 'json:{"encrypt.key-secret": "sec0", "driver": "qcow2", "file": {"driver": "file", "filename": "/home/tests/nfsclient/base.qcow2"}}' snA.qcow2
```

Boot snA:
```
    --object secret,id=sec0,data=base \
    --object secret,id=secA,data=snA \
    -device virtio-scsi-pci,id=virtio_scsi_pci0,bus=pci.0,addr=0x4 \
    -drive id=drive_image1,if=none,snapshot=off,aio=threads,cache=none,format=qcow2,file=/home/tests/nfsclient/snA.qcow2,encrypt.key-secret=secA,backing.encrypt.key-secret=sec0 \
    -device scsi-hd,id=image1,drive=drive_image1,bootindex=0 \
```

Check snA:
```bash
qemu-img check --object secret,id=sec0,data=base --object secret,id=secA,data=snA --image-opts driver=qcow2,encrypt.key-secret=secA,file.filename=snA.qcow2,backing.encrypt.key-secret=sec0
```

snB
Create snB:
```bash
qemu-img create --object secret,id=sec0,data=base --object secret,id=secA,data=snA --object secret,id=secB,data=snB -f qcow2 -o encrypt.format=luks,encrypt.key-secret=secB -b 'json:{"encrypt.key-secret": "secA", "driver": "qcow2", "file": {"driver": "file", "filename": "/home/tests/nfsclient/snA.qcow2"}}' snB.qcow2
```

Boot snB:
```
    --object secret,id=sec0,data=base \
    --object secret,id=secA,data=snA \
    --object secret,id=secB,data=snB \
    -device virtio-scsi-pci,id=virtio_scsi_pci0,bus=pci.0,addr=0x4 \
    -drive id=drive_image1,if=none,snapshot=off,aio=threads,cache=none,format=qcow2,file=/home/tests/nfsclient/snB.qcow2,encrypt.key-secret=secB,backing.encrypt.key-secret=secA \
    -device scsi-hd,id=image1,drive=drive_image1,bootindex=0 \
```

Check snB:
```
qemu-img check --object secret,id=sec0,data=base --object secret,id=secA,data=snA --object secret,id=secB,data=snB --image-opts driver=qcow2,encrypt.key-secret=secB,file.filename=snB.qcow2,backing.encrypt.key-secret=secA
```

snC
Create snC:
```bash
qemu-img create --object secret,id=sec0,data=base --object secret,id=secA,data=snA --object secret,id=secB,data=snB --object secret,id=secC,data=snC -f qcow2 -o encrypt.format=luks,encrypt.key-secret=secC -b 'json:{"encrypt.key-secret": "secB", "driver": "qcow2", "file": {"driver": "file", "filename": "/home/tests/nfsclient/snB.qcow2"}}' snC.qcow2
```

Boot snC:
```
    --object secret,id=sec0,data=base \
    --object secret,id=secA,data=snA \
    --object secret,id=secB,data=snB \
    --object secret,id=secC,data=snC \
    -device virtio-scsi-pci,id=virtio_scsi_pci0,bus=pci.0,addr=0x4 \
    -drive id=drive_image1,if=none,snapshot=off,aio=threads,cache=none,format=qcow2,file=/home/tests/nfsclient/snC.qcow2,encrypt.key-secret=secC,backing.encrypt.key-secret=secB \
    -device scsi-hd,id=image1,drive=drive_image1,bootindex=0 \
```

Check snC:
```bash
qemu-img check --object secret,id=sec0,data=base --object secret,id=secA,data=snA --object secret,id=secB,data=snB --object secret,id=secC,data=snC --image-opts driver=qcow2,encrypt.key-secret=secC,file.filename=snC.qcow2,backing.encrypt.key-secret=secB
```

snD
Create snD:
```bash
qemu-img create --object secret,id=sec0,data=base --object secret,id=secA,data=snA --object secret,id=secB,data=snB --object secret,id=secC,data=snC --object secret,id=secD,data=snD -f qcow2 -o encrypt.format=luks,encrypt.key-secret=secD -b 'json:{"encrypt.key-secret": "secC", "driver": "qcow2", "file": {"driver": "file", "filename": "/home/tests/nfsclient/snC.qcow2"}}' snD.qcow2
```

Boot snD:
```
    --object secret,id=sec0,data=base \
    --object secret,id=secA,data=snA \
    --object secret,id=secB,data=snB \
    --object secret,id=secC,data=snC \
    --object secret,id=secD,data=snD \
    -device virtio-scsi-pci,id=virtio_scsi_pci0,bus=pci.0,addr=0x4 \
    -drive id=drive_image1,if=none,snapshot=off,aio=threads,cache=none,format=qcow2,file=/home/tests/nfsclient/snD.qcow2,encrypt.key-secret=secD,backing.encrypt.key-secret=secC \
    -device scsi-hd,id=image1,drive=drive_image1,bootindex=0 \
```

Check snD:
```bash
qemu-img check --object secret,id=sec0,data=base --object secret,id=secA,data=snA --object secret,id=secB,data=snB --object secret,id=secC,data=snC --object secret,id=secD,data=snD --image-opts driver=qcow2,encrypt.key-secret=secD,file.filename=snD.qcow2,backing.encrypt.key-secret=secC
```

## Rebase image to a new image
create new image
```bash
qemu-img create --object secret,id=sec0,data=new -f qcow2 -o encrypt.format=luks,encrypt.key-secret=sec0 new.qcow2 20G
```

rebase image
```bash
qemu-img rebase -p --object secret,id=sec0,data=base --object secret,id=secA,data=snA --object secret,id=secB,data=snB --object secret,id=secC,data=snC --object secret,id=secnew,data=new --image-opts driver=qcow2,encrypt.key-secret=secC,file.filename=snC.qcow2,backing.encrypt.key-secret=secB -b 'json:{"encrypt.key-secret": "secnew", "driver": "qcow2", "file": {"driver": "file", "filename": "/home/tests/nfsclient/new.qcow2"}}'
```

boot image
```
    --object secret,id=sec0,data=new \
    --object secret,id=secC,data=snC \
    -device virtio-scsi-pci,id=virtio_scsi_pci0,bus=pci.0,addr=0x4 \
    -drive id=drive_image1,if=none,snapshot=off,aio=threads,cache=none,format=qcow2,file=/home/tests/nfsclient/snC.qcow2,encrypt.key-secret=secC,backing.encrypt.key-secret=sec0 \
    -device scsi-hd,id=image1,drive=drive_image1,bootindex=0 \
```

check image
```bash
qemu-img check --object secret,id=sec0,data=new --object secret,id=secC,data=snC --image-opts driver=qcow2,encrypt.key-secret=secC,file.filename=snC.qcow2,backing.encrypt.key-secret=sec0
```

## Rebase using unsafe mode
#rm snA.qcow2
```bash
qemu-img rebase -u -p --object secret,id=sec0,data=base --object secret,id=secB,data=snB --image-opts driver=qcow2,encrypt.key-secret=secB,file.filename=snB.qcow2 -b 'json:{"encrypt.key-secret": "sec0", "driver": "qcow2", "file": {"driver": "file", "filename": "/home/tests/nfsclient/base.qcow2"}}'
```

Boot snapshot:
```
    --object secret,id=sec0,data=base \
    --object secret,id=secB,data=snB \
    -device virtio-scsi-pci,id=virtio_scsi_pci0,bus=pci.0,addr=0x4 \
    -drive id=drive_image1,if=none,snapshot=off,aio=threads,cache=none,format=qcow2,file=/home/tests/nfsclient/snB.qcow2,encrypt.key-secret=secB,backing.encrypt.key-secret=sec0 \
    -device scsi-hd,id=image1,drive=drive_image1,bootindex=0 \
```

## Write data to image
```bash
# qemu-io -c 'write 0 100M' --object secret,id=sec0,data=base --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2
```

## Update the image version
```bash
qemu-img amend --object secret,id=sec0,data=base --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2 -o compat=0.10
```

## Convert the image
convert base image
```bash
qemu-img convert -p --object secret,id=sec0,data=base --object secret,id=sec1,data=convert --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2 -O qcow2 -o encrypt.format=luks,encrypt.key-secret=sec1 convert.qcow2
```

convert the snapshot
```bash
qemu-img convert -p --object secret,id=sec0,data=base --object secret,id=sec1,data=sn --object secret,id=sec2,data=convert --image-opts driver=qcow2,encrypt.key-secret=sec1,file.filename=sn.qcow2,backing.encrypt.key-secret=sec0 -O qcow2 -o encrypt.format=luks,encrypt.key-secret=sec2 convert.qcow2
```

convert the image over blkdebug
```bash
qemu-img create --object secret,id=sec0,data=source -f qcow2 -o encrypt.format=luks,encrypt.key-secret=sec0 source.qcow2 1G
qemu-img create --object secret,id=sec0,data=target -f qcow2 -o encrypt.format=luks,encrypt.key-secret=sec0 target.qcow2 1G
# qemu-io -c 'write 0 1G' --object secret,id=sec0,data=source --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=source.qcow2
# valgrind --soname-synonyms=somalloc=libtcmalloc.so qemu-img convert -npWO --object secret,id=sec0,data=source --object secret,id=sec1,data=target --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=source.qcow2 driver=qcow2,file.driver='blkdebug',file.inject-error.event="write_aio",file.inject-error.sector="819200",file.inject-error.once="on",encrypt.key-secret=sec1,file.image.filename=target.qcow2
```

## Commit the changes
Commit the snapshot to its backing file
```bash
qemu-img commit -p --object secret,id=sec0,data=base --object secret,id=sec1,data=sn --image-opts driver=qcow2,encrypt.key-secret=sec1,file.filename=sn.qcow2,backing.encrypt.key-secret=sec0
```

Commit the snapshot to the base image
```bash
qemu-img commit -p --object secret,id=sec0,data=base --object secret,id=secA,data=snA --object secret,id=secB,data=snB --image-opts driver=qcow2,encrypt.key-secret=secB,file.filename=snB.qcow2,backing.encrypt.key-secret=secA -b 'json:{"encrypt.key-secret": "sec0", "driver": "qcow2", "file": {"driver": "file", "filename": "/home/tests/nfsclient/base.qcow2"}}'
```

## Compare the images
```bash
qemu-img compare -p --object secret,id=sec0,data=base --object secret,id=sec1,data=convert --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2 driver=qcow2,encrypt.key-secret=sec1,file.filename=convert.qcow2
```

## Resize image
```bash
qemu-img resize --object secret,id=sec0,data=base --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2 +1G
```

## Calculate image size
```bash
qemu-img measure -O qcow2 --size 4G -o encrypt.format=luks
qemu-img measure -O qcow2 -o encrypt.format=luks --object secret,id=sec0,data=base --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2
```

## Internal snapshot
create
```bash
qemu-img snapshot --object secret,id=sec0,data=base --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2 -c internal_sn
```

revert
```bash
qemu-img snapshot --object secret,id=sec0,data=base --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2 -a internal_sn
```

delete
delete internal snapshot
```bash
qemu-img snapshot --object secret,id=sec0,data=base --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2 -d internal_sn
```
delete internal snapshot over blkdebug
```bash
qemu-img snapshot --object secret,id=sec0,data=base --image-opts driver=qcow2,file.driver='blkdebug',file.inject-error.event="cluster_free",file.inject-error.errno=28,file.inject-error.immediately="off",encrypt.key-secret=sec0,file.image.filename=base.qcow2 -d internal_sn
```

list
```bash
qemu-img snapshot --object secret,id=sec0,data=base --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2 -l
```

## Dump the metadata
```bash
qemu-img map --output=json --object secret,id=sec0,data=base --image-opts driver=qcow2,encrypt.key-secret=sec0,file.filename=base.qcow2
```

## ftp driver
Get information and check the image
```bash
qemu-img info --object secret,id=sec0,data=`printf %s "redhat" | base64`,format=base64 --image-opts driver=qcow2,file.driver=ftp,file.url=ftp://10.66.8.143/luks/base.qcow2,file.sslverify=off,file.username=ftpuser,file.password-secret=sec0
qemu-img check --object secret,id=sec0,data=base --object secret,id=sec1,data=`printf %s "redhat" | base64`,format=base64 --image-opts driver=qcow2,encrypt.key-secret=sec0,file.driver=ftp,file.url=ftp://10.66.8.143/luks/base.qcow2,file.sslverify=off,file.username=ftpuser,file.password-secret=sec1
```

Create snapshot based on the image through ftp protocol
```bash
qemu-img create --object secret,id=sec0,data=base --object secret,id=sec1,data=snapshot --object secret,id=sec2,data=`printf %s "redhat" | base64`,format=base64 -f qcow2 -o encrypt.format=luks,encrypt.key-secret=sec1 -b 'json:{"encrypt.key-secret": "sec0", "driver": "qcow2", "file": {"driver": "ftp", "url":"ftp://10.66.8.143/luks/base.qcow2", "username":"ftpuser", "password-secret":"sec2"}}' sn.qcow2
```

check the snapshot
```bash
qemu-img check --object secret,id=sec0,data=base --object secret,id=sec1,data=snapshot --object secret,id=sec2,data=`printf %s "redhat" | base64`,format=base64 --image-opts driver=qcow2,encrypt.key-secret=sec1,backing.encrypt.key-secret=sec0,file.filename=sn.qcow2
```

Boot the snapshot(qemu-kvm doesn’t support ftp/ftps driver now)
(06:18:51 PM) kwolf: To be honest, I think this is a case of QE inventing requirements that neither management layer products nor customers ever made
(06:19:31 PM) kwolf: If you want to get FTP fully supported, you need to make a formal feature request, probably after discussion with PM
(06:19:53 PM) kwolf: A feature request normally requires some justification

## ftps driver
Get information and check the image
```bash
qemu-img info --object secret,id=sec0,data=`printf %s "redhat" | base64`,format=base64 --image-opts driver=qcow2,file.driver=ftps,file.url=ftps://10.66.8.143/luks/base.qcow2,file.sslverify=off,file.username=ftpuser,file.password-secret=sec0
qemu-img check --object secret,id=sec0,data=base --object secret,id=sec1,data=`printf %s "redhat" | base64`,format=base64 --image-opts driver=qcow2,encrypt.key-secret=sec0,file.driver=ftps,file.url=ftps://10.66.8.143/luks/base.qcow2,file.sslverify=off,file.username=ftpuser,file.password-secret=sec1
```

Create snapshot based on the image through ftps protocol
```bash
qemu-img create --object secret,id=sec0,data=base --object secret,id=sec1,data=snapshot --object secret,id=sec2,data=`printf %s "redhat" | base64`,format=base64 -f qcow2 -o encrypt.format=luks,encrypt.key-secret=sec1 -b 'json:{"encrypt.key-secret": "sec0", "driver": "qcow2", "file": {"driver": "ftps", "url":"ftps://10.66.8.143/luks/base.qcow2", "username":"ftpuser", "password-secret":"sec2", "sslverify":"off"}}' sn.qcow2
```

check the snapshot
```bash
qemu-img check --object secret,id=sec0,data=base --object secret,id=sec1,data=snapshot --object secret,id=sec2,data=`printf %s "redhat" | base64`,format=base64 --image-opts driver=qcow2,encrypt.key-secret=sec1,backing.encrypt.key-secret=sec0,file.filename=sn.qcow2
```
No errors were found on the image.
Image end offset: 2359296


## ssh driver
Get information of image and check image through ssh
```bash
qemu-img info 'json:{"file.driver":"ssh", "file.host":"10.73.224.143", "file.port":"22", "file.path":"/home/tests/diskfile/base.qcow2", "file.user":"root", "file.host_key_check":"no"}'
qemu-img check --object secret,id=sec0,data=base 'json:{"encrypt.key-secret": "sec0", "file.driver":"ssh", "file.host":"10.73.224.143", "file.port":"22", "file.path":"/home/tests/diskfile/base.qcow2", "file.user":"root", "file.host_key_check":"no"}'
```
```bash
qemu-img info --image-opts driver=qcow2,file.driver=ssh,file.host=10.73.224.143,file.path=/home/tests/diskfile/base.qcow2,file.host_key_check=no
qemu-img check --object secret,id=sec0,data=base --image-opts driver=qcow2,file.driver=ssh,file.host=10.73.224.143,file.path=/home/tests/diskfile/base.qcow2,file.host_key_check=no,encrypt.key-secret=sec0
```

Create snapshot
```bash
qemu-img create --object secret,id=sec0,data=base --object secret,id=sec1,data=snapshot -f qcow2 -o encrypt.format=luks,encrypt.key-secret=sec1 -b 'json:{"encrypt.key-secret": "sec0", "driver": "qcow2", "file.driver":"ssh", "file.host":"10.73.224.143", "file.port":"22", "file.path":"/home/tests/diskfile/base.qcow2", "file.user":"root", "file.host_key_check":"no"}' sn_ssh.qcow2
```

check the snapshot
```bash
qemu-img check --object secret,id=sec0,data=base --object secret,id=sec1,data=snapshot --image-opts driver=qcow2,encrypt.key-secret=sec1,backing.encrypt.key-secret=sec0,file.filename=sn_ssh.qcow2
```

Boot the snapshot
```
    --object secret,id=sec0,data=base \
    --object secret,id=sec1,data=snapshot \
    -device virtio-scsi-pci,id=virtio_scsi_pci0,bus=pci.0,addr=0x4 \
    -drive id=drive_image1,if=none,snapshot=off,aio=threads,cache=none,format=qcow2,file=/home/tests/nfsclient/sn_ssh.qcow2,encrypt.key-secret=sec1,backing.encrypt.key-secret=sec0 \
    -device scsi-hd,id=image1,drive=drive_image1,bootindex=0 \
```

## https driver
Get information of image and check image through https
```bash
qemu-img info 'json:{"file.driver":"https", "file.url":"https://10.66.8.143/luks/base.qcow2", "file.sslverify":"off", "file.readahead":"64k"}'
qemu-img check --object secret,id=sec0,data=base 'json:{"encrypt.key-secret": "sec0", "file.driver":"https", "file.url":"https://10.66.8.143/luks/base.qcow2", "file.sslverify":"off", "file.readahead":"64k"}'
```

```bash
qemu-img info --image-opts driver=qcow2,file.driver=https,file.url=https://10.66.8.143/luks/base.qcow2,file.sslverify=off
qemu-img check --object secret,id=sec0,data=base --image-opts driver=qcow2,file.driver=https,file.url=https://10.66.8.143/luks/base.qcow2,file.sslverify=off,encrypt.key-secret=sec0
```

Create snapshot
```bash
qemu-img create --object secret,id=sec0,data=base --object secret,id=sec1,data=snapshot -f qcow2 -o encrypt.format=luks,encrypt.key-secret=sec1 -b 'json:{"encrypt.key-secret": "sec0", "file.driver":"https", "file.url":"https://10.66.8.143/luks/base.qcow2", "file.sslverify":"off", "file.readahead":"64k"}' sn_https.qcow2
```

 Check the snapshot
 ```bash
qemu-img check --object secret,id=sec0,data=base --object secret,id=sec1,data=snapshot --image-opts driver=qcow2,encrypt.key-secret=sec1,backing.encrypt.key-secret=sec0,file.filename=sn_https.qcow2
```

Boot the snapshot
```
    --object secret,id=sec0,data=base \
    --object secret,id=sec1,data=snapshot \
    -device virtio-scsi-pci,id=virtio_scsi_pci0,bus=pci.0,addr=0x4 \
    -drive id=drive_image1,if=none,snapshot=off,aio=threads,cache=none,format=qcow2,file=/home/tests/nfsclient/sn_https.qcow2,encrypt.key-secret=sec1,backing.encrypt.key-secret=sec0 \
    -device scsi-hd,id=image1,drive=drive_image1,bootindex=0 \
```

