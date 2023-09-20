# linux

```sh
alias r='ranger'
# tmux
alias ta='tmux attach -t'
alias tl='tmux list-sessions'
alias tksv='tmux kill-server'
alias tkss='tmux kill-session -t'
alias v='vi $(fzf)'
# free space
alias freespace='df -H --output=size,used,avail'
alias fspace='sudo du -Sh | sort -rh | head -5'
alias cports='sudo lsof -i -P -n | grep LISTEN'
# commenting for shellcheck fixme later
#alias trace='mtr --report-wide --curses $1'
#alias killtcp='sudo ngrep -qK 1 $1 -d wlan0'
alias usage='ifconfig wlan0 | grep bytes'
alias connections='sudo lsof -n -P -i +c 15'
# alias ducks='du -cks -- * | sort -rn | head\'alias ducks=\'du -cks -- * | sort -rn | head'
alias myip='ip addr | grep inet'
```
