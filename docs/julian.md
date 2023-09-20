# julian dates

- I find julian dates useful for various reasons

```sh
# julian dates
alias day='date +%D && date +%j && date +%A && date +%d && date +%u'
alias fday='mkdir "$(date +%j)" && cd "$(date +%j)"'
alias mday='vim ./"$(date +%j)".md'
alias fj='vim ./"$(date +%F)".md'
alias week='date +%V'
alias month='date +%B && date +%m'
alias year='date +%Y'
```
