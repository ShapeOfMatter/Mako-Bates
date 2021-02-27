---
title: What's in my bin
date: 2021-01-10 00:00:00 -05:00
description: Cataloging various minor things I've added to my OS.
---


{% include section.html c="The .bashrc file" %}
Pop_OS ships with a `.bashrc` file already in your home dir; it's well documented in-line. Mostly it just sets sensible defaults for visibility. There are also a few aliases defined that might be useful. I've mostly left it alone, beyond referencing my own `bash_aliases`.

{% include section.html c="bash aliases" l=3 %}
[The file]({{ "code/bin/aliases.bash" | absolute_url }}).
These aren't super interesting. They serve their purpose well enough.

- `cdls`. The first think I find myself doing when I cd into a directory is usually reminding myself what's in it. This command cd's into the specified directory and lists it's contents. Getting it to only print out the rows and columns I wanted took some work; this is certainly pushing the limits of what I'd want to do in bash.
- `grep_ps` pipes ps into grep. The intention is to quickly check if an OS application (Discord for example), has actually exited or is still running in the background. 
- `grep_context` is just grep with the flags set to print out the few lines surrounding each match. 

{% include section.html c="Bin files" %}
Rather than adding a version-controlled directory directly to my PATH, the following have symbolic links into the normal user-bin.
(`ln -s ~/Git/Mako-Bates/file_name.py ~/.local/bin/command_name`)

{% include section.html c="ifnewer" l=3 %}
[The file]({{ "code/bin/ifnewer.py" | absolute_url }}).  
Run some command if a source file is newer than a dependent file.

I wrote this for automatically regenerating PDFs from Pandoc markdown files while I work on them. More sophisticated options exist (re-build on file-write, or re-build from buffer every time you pause typing), but this is low-tech and works fine. 
I use it in conjunction with `watch`. 

For example, if I'm working on `File.md`: First I'll make sure I have a `.temp/File.pdf` (using `mkdir` and `touch`), then I'll run `watch ifnewer File.md -- pandoc -o {d} {s}`.
Every two seconds, `watch` will run `ifnewer`. `ifnewer` isn't given an explicit destination file, so it'll look for `.temp/File.*`, find the `File.pdf`, and compare its last-modified time against `File.md` to decide if it should call `pandoc`.
I'll keep this running in a vim-split pane so I can check the error-output if anything goes wrong. 

{% include section.html c="set system76 keyboard backlight" l=3 %}
[The file]({{ "code/bin/set_system76_kb_backlight.py" | absolute_url }}).

So far as I'm aware, this is totally specific to people running POP_OS on system-76 laptops. 

On its own, the python script is just a convenient command for setting the color and brightness of the keyboard backlight.
The assumption though is that you'll configure it to be run automatically at boot-time. 
It only works if run as root, and because it's going to be run automatically _as root_, it's important that the file itself can only be written by root.
Building this sanity check into the script was certainly a pain. 

To create the systemd service to run it on boot:  

- Create the service unit file. It goes in `/etc/systemd/system/`; I'm calling it `system76-kb-backlight.service`.
Rather than calling the script directly, it should wrap it in systemd-cat, which manages logging.
There's an example in a comment in the script-file.
- Use `sudo systemctl daemon-reload` to tell systemd to check for new/updated service files.  
- Use `systemctl status system76-kb-backlight.service` to check the task's status and see recent log messages from it.  
- Use `sudo systemctl enable system76-kb-backlight.service` to tell systemd that the service should be started on every boot.


# vim

# keyboard
