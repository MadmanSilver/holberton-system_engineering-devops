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
	int i, pid1 = -1;

	for (i = 0; i < 5; i++)
	{
		pid1 = fork();
		if (pid1 == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", pid1);
	}

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
