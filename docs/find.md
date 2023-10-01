## find 

- find file by type & grep it

```shell
find . -name \*.md -print0 | xargs -0 grep runner
```

```shell
find . -type f -print | xargs grep "example"
```
