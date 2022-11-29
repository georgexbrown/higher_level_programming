#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked list
 * has a cycle in it
 * @list: head of node
 *
 * Return: 0 if no cycle, 1 if there's a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = list;
	second = first;

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
		{
			first = list;
			while (first && second)
			{
				if (first == second)
					return (1);
				first = first->next;
				second = second->next;
			}
		}
	}
	return (0);
}
