

# quickly check if a program is still running
function grep_ps {
  ps ax o"cmd,user,pid" | grep "$1" | grep --invert-match "^grep "
}

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
            | column --table \
                     --separator '|' \
                     --table-hide 2 \
                     --table-right 3 \
                     --output-separator "  "
}

function grep_context {
  grep -C 3 -n -r --exclude-dir='.venv' --exclude-dir='.mypy_cache' --exclude-dir='.git' --exclude-dir='__pycache__' "$@"
}

