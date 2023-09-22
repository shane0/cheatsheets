---
tags:
  - markdown 
  - docs 
  - readability 
---
# markdown

[![markdownlint](https://github.com/shane0/cheatsheets/actions/workflows/markdownlint.yml/badge.svg)](https://github.com/shane0/cheatsheets/actions/workflows/markdownlint.yml)

## configuration file

- `.markdownlint.json`

```json
-8<- ".markdownlint.json"
```

## alias

```sh
# this calls a click command that runs markdownlint
# on my mac uses fli normally I use cli
alias zz='fli bujo zl'
```

## click

```sh
Usage: cli.py bujo [OPTIONS] COMMAND [ARGS]...

  bullet journaling & todocli

Options:
  --help  Show this message and exit.

Commands:
  zl         markdownlint

```

- that calls the markdownlint command line

```sh
@cli.command()
def zl():
    """markdownlint"""
    cmd = "npx markdownlint 'docs/*.md' --config .markdownlint.json"
    os.system(cmd)
```

## github action

- `.github/workflows/markdownlint.yml`

```yml
-8<- ".github/workflows/markdownlint.yml"
```

## command line

```sh
Usage: markdownlint [options] <files|directories|globs>

MarkdownLint Command Line Interface

Options:
  -V, --version                               output the version number
  -c, --config [configFile]                   configuration file (JSON, JSONC, JS, or YAML)
  -d, --dot                                   include files/folders with a dot (for example `.github`)
  -f, --fix                                   fix basic errors (does not work with STDIN)
  -i, --ignore [file|directory|glob]          file(s) to ignore/exclude (default: [])
  -j, --json                                  write issues in json format
  -o, --output [outputFile]                   write issues to file (no console)
  -p, --ignore-path [file]                    path to file with ignore pattern(s)
  -q, --quiet                                 do not write issues to STDOUT
  -r, --rules  [file|directory|glob|package]  include custom rule files (default: [])
  -s, --stdin                                 read from STDIN (does not work with files)
  --enable [rules...]                         Enable certain rules, e.g. --enable MD013 MD041 --
  --disable [rules...]                        Disable certain rules, e.g. --disable MD013 MD041 --
  -h, --help                                  display help for command

```
