# backups

## usage

folder archive

> zip[^1]

```shell
tar -cvf name.tar folder/
gzip name.tar
```

> unzip[^2]

```shell
tar -xzvf name.tar.gz
```

### tar params

* -c: Create archive
* -z: Compress the archive with gzip
* -v: Verbose output
* -f: specify the filename of the archive - must be last

* x: tar can collect files or extract them. x does the latter.
* z: decompress the archive using gzip

## rsync

this can deploy a mkdocs site to nginx just adjust the folder names

this version also changes ownership which you may not need depending how you setup your groups and permissions

```shell
#!/bin/sh

sudo rsync -a -v /home/user/your.com/site/* /var/www/your.com/
sudo chown root:root /var/www/your.com/
```

```text
curl cheat.sh/
tar
# tar
# Archiving utility.
# Often combined with a compression method, such as gzip or bzip.
# More information: <https://www.gnu.org/software/tar>.

# Create an archive from files:
tar cf target.tar file1 file2 file3

# Create a gzipped archive:
tar czf target.tar.gz file1 file2 file3

# Create a gzipped archive from a directory using relative paths:
tar czf target.tar.gz -C path/to/directory .

# Extract a (compressed) archive into the current directory:
tar xf source.tar[.gz|.bz2|.xz]

# Extract an archive into a target directory:
tar xf source.tar -C directory

# Create a compressed archive, using archive suffix to determine the compression program:
tar caf target.tar.xz file1 file2 file3

# List the contents of a tar file:
tar tvf source.tar

# Extract files matching a pattern:
tar xf source.tar --wildcards "*.html"

# Extract a specific file without preserving the folder structure:
tar xf source.tar source.tar/path/to/extract --strip-components=depth_to_strip
```

[^2]: <https://www.linode.com/docs/quick-answers/linux/compress-files-using-the-command-line/#archive-a-directory>)
[^1]: <https://www.howtogeek.com/248780/how-to-compress-and-extract-files-using-the-tar-command-on-linux/>
