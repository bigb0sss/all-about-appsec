public class BackUpRunnerThread extends Thread {
    public void run() {
        long ctr = 0;
        while (true) {
            ProcessBuilder builder = new ProcessBuilder(
                "bash", "-c",
                String.format("sudo tar -cf /var/backups/backup%d.tar *", ctr)
            );
            builder.directory(new File("/opt/wabapp/"))
        }
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


