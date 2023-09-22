---
tags:
  - bujo 
  - click 
  - aliases 
---
# bullet journaling

- bullet journaling is simply using bullets in your notes!
- to keep notes concise, it is not magic
- it existed on paper, now the bullet journal guy that sells the book named this...
- is trying to patent and copyright silly things like the portmanteauu `bujo`
- dude, are you serious...
- [ ] with optional added syntax like *oO-x etc.

## alias

```sh
# bullet journaling aka bujo
alias rd="vim ./readme.md"
alias cl="vim ./changelog.md"
alias jf='mkdir "$(date +%F)" && cd "$(date +%F)"'
alias ft='vim ./future.md'
alias cll='vim ./collections.md'
alias in='vim ./index.md'
alias fj='vim ./"$(date +%F)".md'
alias bj='cd ./bujo && fj || echo "there is no bujo folder"'
alias bujo='cd ./bujo && fj || mkdir bujo && cd ./bujo && vim ./"$(date +%F)".md'
```

## click

```sh
Usage: cli.py bujo [OPTIONS] COMMAND [ARGS]...

  bullet journaling & todocli

Options:
  --help  Show this message and exit.

Commands:
  day        week - cps state rollback test
  dayfolder  create subfolder with named todays date
  edit       edit plugin
  folder     create bujo folder
  future     bujo index file
  index      bujo index file
  m          mkdocs serve
  month      month file
  read       read a bujo/ file
  remote     jobs on remotive
  s          start dev server
  snip       open snippet maker
  todo       generic todo
  week       week - cps state rollback test
  ww         weather
  year       week - cps state rollback test
  zl         markdownlint

```
