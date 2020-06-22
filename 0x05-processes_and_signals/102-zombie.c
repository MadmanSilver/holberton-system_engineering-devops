#include <stdio.h>
#include <unistd.h>

int main(void);
int infinite_while(void);

/**
 * main - creates 5 zombies and starts an infinite loop
 * Return: always 0
 */
int main(void)
{
	int pid1, pid2, pid3, pid4, pid5;

	pid1 = fork();
	if (pid1)
		printf("Zombie process created, PID: %d\n", pid1);
	pid2 = fork();
	if (pid1 && pid2)
		printf("Zombie process created, PID: %d\n", pid2);
	pid3 = fork();
	if (pid1 && pid2 && pid3)
		printf("Zombie process created, PID: %d\n", pid3);
	pid4 = fork();
	if (pid1 && pid2 && pid3 && pid4)
		printf("Zombie process created, PID: %d\n", pid4);
	pid5 = fork();
	if (pid1 && pid2 && pid3 && pid4 && pid5)
		printf("Zombie process created, PID: %d\n", pid5);

	if (pid1 && pid2 && pid3 && pid4 && pid5)
		infinite_while();

	return (0);
}

/**
 * infinite_while - loops infinitely
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
