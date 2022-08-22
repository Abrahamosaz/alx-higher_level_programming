#include "lists.h"
/**
 * check_cycle - check if the linked list is cycle
 * @list: head adrress of the linked list
 *
 * Return: return 1 if it's is True and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp)
	{
		temp = temp->next;
		if (temp == list)
			return (1);
	}
	return (0);
}
