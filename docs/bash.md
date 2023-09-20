# bash

```sh
#!/usr/bin/env bash
alias ea='code ~/.bash_aliases'
alias sa='source ~/.bashrc'

alias yourserver='ssh user@0.0.0.0'
alias yourservers='ssh user@0.0.0.0'

alias c='clear'

# ls 
alias ll='ls -l'
alias la='ls -A'
alias l='ls -CF'
alias lt='ls --human-readable --size -1 -S --classify'

alias ctodo='cp -R ~/workflow/todocli/ .'
alias showremote='echo "https://github.com/" $(head -1 <(git remote -v | cut -d ":" -f2 | cut -d "." -f1 | tr -s " " "\0"))'

alias mks='mkdocs serve'
```
