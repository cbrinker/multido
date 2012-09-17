=======
multido
=======

multido provides a simple command line utility for easily running 
a shell command multiple times in parallel. One of the most useful 
examples generally works like this:: 

    $ multido "ssh %s uptime" host1 host2 host3
    host1: 22:02:28 up 5 days,  2:52,  0 users,  load average: 0.05, 0.04, 0.05
    host2: 22:02:27 up 5 days, 24 min,  0 users,  load average: 0.05, 0.03, 0.05
    host3: 22:02:28 up 6 days, 48 min,  0 users,  load average: 0.01, 0.02, 0.05

Unlike say, xargs -P, multido will not just give up if there is a problem
with one of the commands, instead it will output the STDERR to STDERR with the 
RC prepended to each line::

    $ multido "ls /etc/%s" passwd missing sudoers
    passwd: /etc/passwd
    missing: RC1: ls: /etc/missing: No such file or directory
    sudoers: /etc/sudoers

multido also accepts stdin from a pipe too, making for easy to chain
commands::

    $ echo -e "host1\nhost2\nhost3" | multido "ssh %s date"
    host1: Mon Sep 17 22:08:40 UTC 2012
    host2: Mon Sep 17 22:08:40 UTC 2012
    host3: Mon Sep 17 22:08:40 UTC 2012

If you have a preferred grouping you would like the commands to be executed in
there is a syntax to support grouping::

    $ multido "echo %s; sleep 1" [ 'b1a' 'b1b' ] [ 'b2' ] [ 'b3a' 'b3b' 'b3c' ]     
    b1a: b1a
    b1b: b1b
    b2: b2
    b3a: b3a
    b3b: b3b
    b3c: b3c

Or if you just want to limit to batches of N at a time there is syntax 
available to achieve that::

    $ N=2; multido -P$N "echo %s; sleep 1" a b c
    a: a
    b: b
    c: c
