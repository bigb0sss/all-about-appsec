public class BackUpRunnerThread exetends Thread {
    public void run() {
        long ctr = 0;
        while (true) {
            processBuilder builder = new ProcessBuilder(
                "bash", "-c",
                String.format("sudo tar -cf /var/backups/backup%d.tar *", ctr)
            );
            builder.directory(new File("/opt/webapp/"));
            builder.start();
            ctr =+ 1
            // every 30min
            Thread.sleep(1000 * 50 * 30);
        }
    }
}


/*

# Link
https://twitter.com/SonarSource/status/1467886551321432072

# Issues
1) Potential RCE - One can make a filename called "-I touch shell" in /opt/webapp 
    a) "-I" allows executing arbitrary commands

# Mitigations
1) Do not use '*' altogether to blindly archiving every file within the specified directory

*/


