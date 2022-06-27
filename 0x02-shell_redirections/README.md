My read me

Tasks
0. Hello World
    Write a script that prints “Hello, World”, followed by a new line to the standard output.

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 0-hello_world
 
1. Confused smiley

    Write a script that displays a confused smiley "(Ôo)'.

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 1-confused_smiley

2. Let's display a file
    Display the content of the /etc/passwd file.

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 2-hellofile
 
3. What about 2?
    Display the content of /etc/passwd and /etc/hosts
        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 3-twofiles
 
4. Last lines of a file
    Display the last 10 lines of /etc/passwd
        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 4-lastlines
 
5. I'd prefer the first ones actually
    Display the first 10 lines of /etc/passwd

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 5-firstlines

6. Line #2
    Write a script that displays the third line of the file iacta.

        The file iacta will be in the working directory


        Alea iacta est ("The die is cast") is a Latin phrase attributed by Suetonius
        (as iacta alea est) to Julius Caesar on January 10, 49 BC
        as he led his army across the Rubicon river in Northern Italy. With this step,
        he entered Italy at the head of his army in defiance of the Senate and began
        his long civil war against Pompey and the Optimates. The phrase has been
        adopted in Italian (Il dado è tratto), Romanian (Zarurile au fost aruncate),
        Spanish (La suerte está echada), French (Les dés sont jetés), Portuguese (A
        sorte está lançada), Dutch (De teerling is geworpen),
        German (Der Würfel ist gefallen), Hungarian (A kocka el van vetve) and many other languages to
        indicate that events have passed a point of no return.

        Read more: https://en.wikipedia.org/wiki/Alea_iacta_est


        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 6-third_line

7. It is a good file that cuts iron without making a noise
    Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 7-file
 
8. Save current state of directory
    Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 8-cwd_state
9. Duplicate last line
    Write a script that duplicates the last line of the file iacta

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 9-duplicate_last_line

10. No more javascript
    Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 10-no_more_js

11. Don't just count your directories, make your directories count
    Write a script that counts the number of directories and sub-directories in the current directory.

    The current and parent directories should not be taken into account
    Hidden directories should be counted

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 11-directories
 
12. What’s new
    Create a script that displays the 10 newest files in the current directory.

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 12-newest_files

13. Being unique is better than being perfect
    Create a script that takes a list of words as input and prints only words that appear exactly once.
        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 13-unique
 
14. It must be in that file
    Display lines containing the pattern “root” from the file /etc/passwd
        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 14-findthatword
 
15. Count that word
    Display the number of lines that contain the pattern “bin” in the file /etc/passwd

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 15-countthatword
 
16. What's next?
    Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 16-whatsnext
 
17. I hate bins
    Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 17-hidethisword

18. Letters only please
    Display all lines of the file /etc/ssh/sshd_config starting with a letter.

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 18-letteronly

19. A to Z
    Replace all characters A and c from input to Z and e respectively.
        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 19-AZ

20. Without C, you would live in hiago
    Create a script that removes all letters c and C from input.
        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 20-hiago

21. esreveR
    Write a script that reverse its input.
        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 21-reverse

22. DJ Cut Killer
    Write a script that displays all users and their home directories, sorted by users.

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 22-users_and_homes

23. Empty casks make the most noise

    Write a command that finds all empty files and directories in the current directory and all sub-directories.

    Only the names of the files and directories should be displayed (not the entire path)
    Hidden files should be listed
    One file name per line
    The listing should end with a new line
    You are not allowed to use basename, grep, egrep, fgrep or rgrep
        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 100-empty_casks

24. A gif is worth ten thousand words
    Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.

    Hidden files should be listed
    Only regular files (not directories) should be listed
    The names of the files should be displayed without their extensions
    The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
    One file name per line
    The listing should end with a new line
    You are not allowed to use basename, grep, egrep, fgrep or rgrep
    
        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 101-gifs

25. Acrostic

    An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. Read more.

    Create a script that decodes acrostics that use the first letter of each line.

        The ‘decoded’ message has to end with a new line
        You are not allowed to use grep, egrep, fgrep or rgrep
        julien@ubuntu:/tmp/0x02$ cat An\ Acrostic 
        Elizabeth it is in vain you say
        Love not"—thou sayest it in so sweet a way:
        In vain those words from thee or L.E.L.
        Zantippe's talents had enforced so well:
        Ah! if that language from thy heart arise,
        Breath it less gently forth—and veil thine eyes.
        Endymion, recollect, when Luna tried
        To cure his love—was cured of all beside—
        His follie—pride—and passion—for he died.

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 102-acrostic

26. The biggest fan

    Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

        Order by number of requests, most active host or IP at the top
        You are not allowed to use grep, egrep, fgrep or rgrep
        Format:

        host    When possible, the hostname making the request. Uses the IP address if the hostname was unavailable.
        logname Unused, always -
        time    In seconds, since 1970
        method  HTTP method: GET, HEAD, or POST
        url Requested path
        response    HTTP response code
        bytes   Number of bytes in the reply
        Here is an example with one day of logs of the NASA website (1995).

        Repo:
        GitHub repository: alx-system_engineering-devops
        Directory: 0x02-shell_redirections
        File: 103-the_biggest_fan
