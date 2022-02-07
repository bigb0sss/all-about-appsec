int main(int argc, char **argv)
{
    pid_t pid;
    int status;
    setuid(0);
    setgid(0);

    switch (pid = fork()) {
        case 0: // child
            setenv("PAHT", "/usr/sbin", 0);
            status = execl("modprobe", "modprobe", "zfs", NULL);
        default: // parent
            sleep(5);
    }

}


/*

# Link
https://twitter.com/SonarSource/status/1467524170695077889

# Issues
1) `execl()` calls `modprobe` from the environment of the parent process.
2) An attacker could make a malicious file called `modprobe` locating in the same dir with the above program, then it will execute the attacker's `modprobe` program instead of the legit one as root. 

# Mitigations
1) Provide the absolute path for the `modprobe` binary. 

*/


