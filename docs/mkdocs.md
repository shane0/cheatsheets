---
tags:
    - alias
    - mkdocs
    - click
---
# mkdocs

[![pages-build-deployment](https://github.com/shane0/cheatsheets/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/shane0/cheatsheets/actions/workflows/pages/pages-build-deployment)

## alias

- serve with alias

```sh
alias mks='mkdocs serve'
```

## click

- serve with click

```sh
cli bujo m
```

## citation[^1]

```markdown
- this[^1]
[^1]: requires software installation
```

## includes

- `-8<- "includes/example.md"`
- embed docs on multiple pages
- you can also splice in partial files using line numbers `example.md:2:5`

```markdown
-8<- "includes/example.md"
```

## site wide glossary

- mouse over this: PRAJNA
- add more here: `includes/abbreviations.md`

## github actions

- this site is deployed using this command `mkdocs gh-deploy`
- github pages actions deploys updates on this branch `gh-pages`

![p](https://user-images.githubusercontent.com/1454458/270071917-7e2e09dc-6825-41fa-882e-4c02836d664b.png)

[^1]: citations go here
