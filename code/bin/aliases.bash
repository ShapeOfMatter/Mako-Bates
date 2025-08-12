#!/usr/bin/env bash

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

# set PATH so it includes TexLive
if [ -d "/usr/local/texlive/2024/bin/x86_64-linux" ] ; then
    PATH="/usr/local/texlive/2024/bin/x86_64-linux:$PATH"
    MANPATH="/usr/local/texlive/2024/texmf-dist/doc/man:$MANPATH"
    INFOPATH="/usr/local/texlive/2024/texmf-dist/doc/info:$INFOPATH"
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
  grep -C 3 -n -r \
      --exclude-dir='.venv' \
      --exclude-dir='.mypy_cache' \
      --exclude-dir='.git' \
      --exclude-dir='__pycache__' \
      --exclude-dir='.stack-work' \
      --exclude-dir='dist-newstyle' \
      --exclude-dir='target/debug' \
      --exclude-dir='node_modules' \
      --exclude='Cargo.lock' \
      "$@"
}

# activate and de-activate the nord-vpn client
function nordvpnc {
    nordvpn disconnect > /dev/null
    nordvpn set killswitch enabled  # kills internet if vpn fails
    nordvpn set cybersec enabled  # blacklist DNS lookups. sketchy? interaction with firefox?
    nordvpn set notify enabled
    nordvpn set technology NordLynx
    # NA to Nordlynx?
    #nordvpn set protocol UDP  # tcp may be more reliable, but slower?
    #nordvpn set obfuscate disabled  # only relevant for bypassing firewalls.
    nordvpn connect
    nordvpn set autoconnect enabled
}
function nordvpnd {
    nordvpn set autoconnect disabled
    nordvpn set killswitch disabled
    nordvpn set cybersec disabled
    nordvpn disconnect
    #nordvpn set obfuscate disabled
}

