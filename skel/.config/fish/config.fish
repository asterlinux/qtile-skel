set -e fish_user_paths
set -U fish_user_paths $HOME/.local/bin $HOME/Applications $fish_user_paths

### EXPORT ###
set fish_greeting                                
set TERM "xterm-256color"

### "bat" as manpager
set -x MANPAGER "sh -c 'col -bx | bat -l man -p'"

function fish_user_key_bindings
  #fish_default_key_bindings
  fish_vi_key_bindings
end

# # ex = EXtractor for all kinds of archives
# # usage: ex -a file.tar.gz
function ex -a file
    if test -f "$file"
        switch "$file"
            case "*.tar.bz2"
                tar xjf $file
            case "*.tar.gz"
                tar xzf $file
            case "*.bz2"
                bunzip2 $file
            case "*.rar"
                unrar x $file
            case "*.gz"
                gunzip $file
            case "*.tar"
                tar xf $file
            case "*.tbz2"
                tar xjf $file
            case "*.tgz"
                tar xzf $file
            case "*.zip"
                unzip $file
            case "*.Z"
                uncompress $file
            case "*.7z"
                7z x $file
            case "*"
                echo "'$file' cannot be extracted via ex -a <file>"
        end
    else
        echo "'$file' is not a valid file"
    end
end

### AUTOCOMPLETE AND HIGHLIGHT COLORS ###
set fish_color_normal brcyan
set fish_color_autosuggestion '#7d7d7d'
set fish_color_command brcyan
set fish_color_error '#ff6c6b'
set fish_color_param brcyan

### ALIASES ###

# Changing "ls" to "exa"
alias ls='exa --color=always --group-directories-first'
alias la='exa -lah --color=always --octal-permissions --no-permissions --group-directories-first'
alias l='exa -lh --color=always --group-directories-first'

# confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

# change cat to bat
alias cat="bat"

# typo fixes
alias cd..='cd ..'
alias pdw='pwd'

# colored grep out 
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

source (/usr/bin/starship init fish --print-full-init | psub)
pfetch
