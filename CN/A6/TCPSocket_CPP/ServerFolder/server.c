#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<errno.h>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<netdb.h>
#define PORT 8000

void main(){

	int server_fd, new_socket, valread;
	struct sockaddr_in address;
	int opt = 1;
	int addrlen = sizeof(address);
	char buffer[1024] = {0};

	if( (server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
	{
		perror("socket failed");
        exit(EXIT_FAILURE);
	}

	if( setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT,
                                                  &opt, sizeof(opt)))
	{
		perror("setsockopt");
        exit(EXIT_FAILURE);
	}
	memset(&address, 0, addrlen);
	address.sin_family = AF_INET;
	address.sin_addr.s_addr = INADDR_ANY;
	address.sin_port = htons(PORT);

	if (bind(server_fd, (struct sockaddr *)&address,
                                 sizeof(address))<0)
   	{
        	perror("bind failed");
        	exit(EXIT_FAILURE);
   	}
    	if (listen(server_fd, 3) < 0)
    	{
        	perror("listen");
        	exit(EXIT_FAILURE);
    	}
    	if ((new_socket = accept(server_fd, (struct sockaddr *)&address,
                       (socklen_t*)&addrlen))<0)
   	{
        	perror("accept");
        	exit(EXIT_FAILURE);
    	}

    	valread = read(new_socket, buffer, 1024);
    	printf("%s\n", buffer);

	//File transfer
	FILE *fp;
	fp = fopen("file", "w+");
	char buffer2[10];
	valread = read(new_socket, buffer2, 10);
	fprintf(fp, "%s", buffer2);
	fclose(fp);

	// Arithmetic
	int recv, option, num1, num2, answer;
	valread = read(new_socket, &recv, sizeof(recv));
	option = ntohl(recv);
	valread = read(new_socket, &recv, sizeof(recv));
	num1 = ntohl(recv);
	valread = read(new_socket, &recv, sizeof(recv));
	num2 = ntohl(recv);

	//printf("%d, %d, %d", option, num1, num2);

	switch(option){
		case 1:
			answer = num1 + num2;
			break;
		case 2:
			answer = num1 - num2;
			break;
		case 3:
			answer = num1 * num2;
			break;
		case 4:
			if (num2==0)
			{
    				perror(" ********ERROR***** 2nd number cannot be zero");
			
				exit(0);
			}
			answer = num1 / num2;
			break;
		default:
			answer = 0;
			break;
	}

	recv = htonl(answer);
	send(new_socket, &recv, sizeof(recv), 0);
}
