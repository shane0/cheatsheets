# todo cli

- included in this cookiecutter template

[workflow cookiecutter](https://shane0.github.io/workflow/){ .md-button }

```sh
# todocli.md todocli app
alias t='clear && ./todocli/todo.sh'
alias d='clear && t listpri a'
alias snooze='clear && t listpri'
alias done='clear && cat ./todocli/done.txt'
alias tedit='vim ./todocli/todo.txt'
alias tall='clear && find . -name "todo.txt" | xargs grep "+"'
alias tpri='clear && find . -name "todo.txt" | xargs grep "(A"'
alias tprib='clear && find . -name "todo.txt" | xargs grep "(B"'
alias tpric='clear && find . -name "todo.txt" | xargs grep "(C"'
alias thelp='clear && ./todocli/todo.sh shorthelp'
```

![f](images/todoformat.png)
