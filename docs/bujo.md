# bullet journaling

- bullet journaling is simply using bullets in your notes!
- to keep notes concise, it is not magic
- it existed on paper, now the bullet journal guy that sells the book named this...
- is trying to patent and copyright silly things like the portmanteauu `bujo`
- dude, are you serious...
- [ ] with optional added syntax like *oO-x etc.

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
