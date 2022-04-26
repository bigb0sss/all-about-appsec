char passw[16];
char buffer[16];

strlcpy(passw, getenv("KEY"), 16);
sockfd = socket(AF_INET, SOCK_STREAM, 0);

newsockfd = accept(sockfd,
            (struct sockaddr *) &cli_addr,
            &clilen);

if (newsockfd < 0) error("ERROR on accept");
bzero(buffer, 16);
n = read(newsockdf, buffer, 16);
if (n < 0) error("ERROR reading from socket");
printf("Here is the message: %s\n", buffer);
n = write(newsockfd, buffer, strlen(buffer));


/*

# Link
https://twitter.com/SonarSource/status/1468611328625496078

# Issues
1) The problem lies with the server reading 16 bytes on line 13 into its buffer without making sure that the string is null terminated (last byte of the buffer is null).

Sending 16 non-null bytes to the server will return them and the adjacent buffer containing sensitive data!

# Mitigations
1) Limit the buffer size for the read()

*/