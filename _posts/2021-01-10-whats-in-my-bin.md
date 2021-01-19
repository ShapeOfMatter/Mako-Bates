---
title: What's in my bin
date: 2021-01-10 00:00:00 -05:00
description: Cataloging various minor things I've added to my OS.
---


{% include section.html c="The .bashrc file" %}
Pop_OS ships with a `.bashrc` file already in your home dir; it's well documented in-line. Mostly it just sets sensible defaults for visability. There are also a few aliases defined that might be useful. I've mostly left it alone, beyond referencing my own `bash_aliases`.

{% include section.html c="bash aliases" l=3 %}
[The file]({{ "code/bin/aliases.bash" | absolute_url }}).
These aren't super interesting. They serve their purpose well enough.

- `cdls`. The first think I find myself doing when I cd into a directory is usually reminding myself what's in it. This command cd's into the specified directory and lists it's contents. Getting it to only print out the rows and columns I wanted took some work; this is certainly pushing the limits of what I'd want to do in bash.
- `grep_ps` pipes ps into grep. The intention is to quicly check if an OS application (Discord for example), has actually exited or is still running in the background. 
- `grep_context` is just grep with the flags set to print out the few lines surrounding each match. 

{% include section.html c="" %}




# vim
