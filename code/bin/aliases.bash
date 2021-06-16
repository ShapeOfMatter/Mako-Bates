#!/usr/bin/env bash

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

# quickly check if a program is still running
function grep_ps {
  ps ax o"cmd,user,pid" | grep "$1" | grep --invert-match "^grep "
}

# This relies on a new version of `column`, which most debian distros are currently ignoring. 
# https://askubuntu.com/questions/1098248/how-can-i-install-the-util-linux-version-of-the-column-command-in-18-04
# save the unpacked files to code/util-... and copy the exe to bin as column2.
if [ -x "$(command -v column2)" ] ; then
    COLUMN="column2"
else
    COLUMN="column"
fi

function cdls {
  cd "$@" \
      && pwd \
      && ls --almost-all \
            --ignore-backups \
            --human-readable \
            --time-style=long-iso \
            -pGg \
            --color=always \
            --hide-control-chars \
            | tail --lines=+2 \
            | sed -e 's/[[:space:]][[:space:]]*/|/' \
                  -e 's/[[:space:]][[:space:]]*/|/' \
                  -e 's/[[:space:]][[:space:]]*/|/' \
                  -e 's/[[:space:]][[:space:]]*/|/' \
                  -e 's/[[:space:]][[:space:]]*/|/' \
            | $COLUMN --table \
                     --separator '|' \
                     --table-hide 2 \
                     --table-right 3 \
                     --output-separator "  "
}

function grep_context {
  grep -C 3 -n -r --exclude-dir='.venv' --exclude-dir='.mypy_cache' --exclude-dir='.git' --exclude-dir='__pycache__' "$@"
}

