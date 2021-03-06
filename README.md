# debsnapshot-cli
python program to get package information from http://snapshot.debian.org/ for Debian and Debian based distibutions.

not on pypi yet, to try it , download & unzip

install as a super user

```
python setup.py install --record locations.txt
```

uninstall

```
cat locations.txt | xargs rm -rf
```

Get package information from the snapshot.debian.org ex. source versions,binary versions and most important ```first_seen``` 
entry in order to install/downgrade that is no longer in the official {stable,testing,unstable} repositories by adding/appending 
```deb [check-valid-until=no] http://snapshot.debian.org/archive/debian/first_seen unstable main contrib non-free```
to the /etc/apt/sources.list.d/snapshot.list file

```
$ debsnapshot-cli -h 
usage: debsnapshot-cli [-h] [-lb] [-ls] [-lbins] [--first-seen]
                       [-arch ARCHITECTURE] [--time-out TIME_OUT] [-v] [-w]
                       [package_version] package_name

find package information in debian.snapshot.org

positional arguments:
  package_version       set the target version of the package you wish you
  package_name          write the package name you wish to find

optional arguments:
  -h, --help            show this help message and exit
  -lb, --all-binary-versions
                        find binary package versions and corresponding source
                        names and versions
  -ls, --all-source-versions
                        list all available source versions for this package
  -lbins, --all-binpackages-for-package-version
                        list all binary packages associated with this source
                        package at that version
  --first-seen          get information e.x first_seen
  -arch ARCHITECTURE, --architecture ARCHITECTURE
                        define system architecture
  --time-out TIME_OUT   set timeout
  -v, --version         print debsnapshot-cli version
  -w, --write-to-file   add url entry to /etc/apt/sources.list.d/snapshot.list

```
debsnapshot-cli can throw a lot of output, some packages have =>200 versions but you can pipe it with |less or |head -n. This is an example with the  spacefm [[1]](https://packages.debian.org/search?suite=default&section=all&arch=any&searchon=names&keywords=spacefm)[[2]](https://github.com/IgnorantGuru/spacefm) file manager that
has relatively a small number of version
###examples 
```
$ debsnapshot-cli spacefm
```
#####No arguments
Running debsnapshot-cli with no argument will print the source and the binary name of the package.

```
+------------------+---------------+
| Source name(s)   | Binary name   |
+==================+===============+
| spacefm          | spacefm       |
+------------------+---------------+
```

#####-ls
Will print all available source versions
```
 $ debsnapshot-cli -ls spacefm
 ```
 
 ```
+--------------------------------+
| version                        |
+================================+
| 1.0.4-1                        |
+--------------------------------+
| 1.0.3-1                        |
+--------------------------------+
| 1.0.1-1                        |
+--------------------------------+
| 1.0.0-1                        |
+--------------------------------+
| 0.9.4+git20140406-1            |
+--------------------------------+
| 0.9.4-2                        |
+--------------------------------+
| 0.9.4-1                        |
+--------------------------------+
| 0.9.3-1                        |
+--------------------------------+
| 0.9.3-1~bpo70+1                |
+--------------------------------+
| 0.9.2-1                        |
+--------------------------------+
| 0.9.2-1~bpo70+1                |
+--------------------------------+
| 0.9.1+git20131124.29dbeba902-1 |
+--------------------------------+
| 0.9.1-1                        |
+--------------------------------+
| 0.9.0-3                        |
+--------------------------------+
| 0.9.0-2                        |
+--------------------------------+
| 0.9.0-1                        |
+--------------------------------+
| 0.8.7-3                        |
+--------------------------------+
| 0.8.7-2                        |
+--------------------------------+
| 0.8.7-1                        |
+--------------------------------+

Number of versions:  19
```

#####-lb version package  
Will print all binary package versions and corresponding source names and versions
```
$ debsnapshot-cli -lb spacefm
+--------------------------------+----------+--------------------------------+---------+
| binary_version                 | source   | version                        | name    |
+================================+==========+================================+=========+
| 1.0.4-1                        | spacefm  | 1.0.4-1                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 1.0.3-1                        | spacefm  | 1.0.3-1                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 1.0.1-1+b1                     | spacefm  | 1.0.1-1                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 1.0.1-1                        | spacefm  | 1.0.1-1                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 1.0.0-1                        | spacefm  | 1.0.0-1                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.4+git20140406-1+b1         | spacefm  | 0.9.4+git20140406-1            | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.4+git20140406-1            | spacefm  | 0.9.4+git20140406-1            | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.4-2                        | spacefm  | 0.9.4-2                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.4-1                        | spacefm  | 0.9.4-1                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.3-1                        | spacefm  | 0.9.3-1                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.3-1~bpo70+1                | spacefm  | 0.9.3-1~bpo70+1                | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.2-1                        | spacefm  | 0.9.2-1                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.2-1~bpo70+1                | spacefm  | 0.9.2-1~bpo70+1                | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.1+git20131124.29dbeba902-1 | spacefm  | 0.9.1+git20131124.29dbeba902-1 | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.1-1                        | spacefm  | 0.9.1-1                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.0-3                        | spacefm  | 0.9.0-3                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.0-2                        | spacefm  | 0.9.0-2                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.9.0-1                        | spacefm  | 0.9.0-1                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.8.7-3                        | spacefm  | 0.8.7-3                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.8.7-2+b1                     | spacefm  | 0.8.7-2                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.8.7-2                        | spacefm  | 0.8.7-2                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+
| 0.8.7-1                        | spacefm  | 0.8.7-1                        | spacefm |
+--------------------------------+----------+--------------------------------+---------+

Number of packages: 22
```

#####-ls version package
by adding the version of the package, it will list all source files associated with this package at this version
```
$ debsnapshot-cli -ls 0.9.2-1 spacefm
+------------------------------------------+
| hash                                     |
+==========================================+
| dd9bcd8ff1587fde0248618c9914ea09e64f3c2f |
+------------------------------------------+
| f69f214271abd7f003c88504ccd22f706b5dcbaa |
+------------------------------------------+
| 26d02ed51c99405a65dcb5cc3d096f48fb9b6030 |
+------------------------------------------+
```

#####-lbins version package
lists all binary packages associated with this source package at that version
```
debsnapshot-cli -lbins  0.9.2-1 spacefm
+-----------+----------------+
| version   | name           |
+===========+================+
| 0.9.2-1   | spacefm        |
+-----------+----------------+
| 0.9.2-1   | spacefm-common |
+-----------+----------------+
| 0.9.2-1   | spacefm-gtk3   |
+-----------+----------------+
```

#####--first-seen  -arch amd64 version package
by using the --info argument and the architecture it will print the ```first_seen``` entry. You have to add an architecture
for the [official Debian ports](https://www.debian.org/ports/).if ```-arch``` parameter does not match, it will  try to match 'all' as an architecture (if it exists)
```
$ debsnapshot-cli --first-seen -arch amd64 0.9.2-1 spacefm


archive_name    name                       path                  first_seen        hash                                        size
--------------  -------------------------  --------------------  ----------------  ----------------------------------------  ------
debian          spacefm_0.9.2-1_amd64.deb  /pool/main/s/spacefm  20131221T035435Z  9ae5c18906e9c9676f82f43421e94dd478fc8796  378612


URL
----------------------------------------------------------------------------
deb http://snapshot.debian.org/archive/debian/20131221T035435Z unstable main

```
if you add ```-w``` or ```--write-to-file``` to the previous command it will ask you to write to /etc/apt/sources.list.d/snapshot.list

```
$ debsnapshot-cli --first-seen  -arch amd64 --write-to-file 0.9.2-1 spacefm


archive_name    name                       path                  first_seen        hash                                        size
--------------  -------------------------  --------------------  ----------------  ----------------------------------------  ------
debian          spacefm_0.9.2-1_amd64.deb  /pool/main/s/spacefm  20131221T035435Z  9ae5c18906e9c9676f82f43421e94dd478fc8796  378612


URL
---------------------------------------------------------------------------------------------------
deb [check-valid-until=no] http://snapshot.debian.org/archive/debian/20131221T035435Z unstable main


Append this URL to /etc/apt/sources.list.d/snapshot.list?
do you want to continue [y/n/Y/N]:y
Please enter your sudo password:
Password: 

```

if you answer yes and add your **sudo** password, it will add the relevant entry with a comment that indicates why this snapshot entry was added.

```
 $ cat /etc/apt/sources.list.d/snapshot.list 

###Appended from debsnapshot-cli for spacefm:0.9.2-1
deb [check-valid-until=no] http://snapshot.debian.org/archive/debian/20131221T035435Z unstable main

```
and hopefully you will find the target version

```
# apt-cache policy spacefm

spacefm:
  Installed: 1.0.4-1
  Candidate: 1.0.4-1
  Version table:
 *** 1.0.4-1 500
        500 http://httpredir.debian.org/debian unstable/main amd64 Packages
        100 /var/lib/dpkg/status
     0.9.2-1 500
        500 http://snapshot.debian.org/archive/debian/20131221T035435Z unstable/main amd64 Packages

```

at a minimum,debsnapshot-cli will check if the folder ```/etc/apt/sources.list.d/``` exists, if it does not, it quits. 
if a file with name snapshots.list exist in this path,it will append it
if the file **does not** exist in sources.list.d/ folder, it will first create the file with the write the entry.

Update with normal ```apt-get update``` or with
```apt-get -o Acquire::Check-Valid-Until=false update ``` if the url does not contain ```[check-valid-until=no]```
or you  can update **only** the snapshot repo with
```apt-get -o  Dir::Etc::sourcelist="sources.list.d/snapshot.list" -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"  -o Acquire::Check-Valid-Until=false update```
provided that the you have a snapshot.list file in ```/etc/apt/sources.list.d/ ```
