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

{% include section.html c="Bin files" %}
Rather than adding a version-controlled direcory directly to my PATH, the following have symbolic links into the nomal user-bin.
(`ln -s ~/Git/Mako-Bates/file_name.py ~/.local/bin/command_name`)

{% include section.html c="ifnewer" l=3 %}
[The file]({{ "code/bin/ifnewer.py" | absolute_url }}).  
Run some command if a source file is newer than a dependent file.

I wrote this for automatically regenerating PDFs from Pandoc markdown files while I work on them. More sophisticated options exist (re-build on file-write, or re-build from buffer every time you pause typing), but this is low-tech and works fine. 
I use it in conjuntion with `watch`. 

For example, if I'm working on `File.md`: First I'll make sure I have a `.temp/File.pdf` (using `mkdir` and `touch`), then I'll run `watch ifnewer File.md -- pandoc -o {d} {s}`.
Every two seconds, `watch` will run `ifnewer`. `ifnewer` isn't given an explicit destination file, so it'll look for `.temp/File.*`, find the `File.pdf`, and compare its last-modifed time against `File.md` to decide if it should call `pandoc`.
I'll keep this running in a vim-split pane so I can check the error-output if anything goes wrong. 

{% include section.html c="set system76 keyboard backlight" l=3 %}
[The file]({{ "code/bin/set_system76_kb_backlight.py" | absolute_url }}).

So far as I'm aware, this is totally specific to people running POP_OS on system-76 laptops. 




# vim

# keyboard
