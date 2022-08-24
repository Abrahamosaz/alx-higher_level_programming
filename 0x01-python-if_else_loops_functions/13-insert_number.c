#include "lists.h"
/**
 * insert_node  - insert node according to sorted linked list
 * @head: pointer that store the address of the head pointer
 * @number: value to insert in the linked list
 *
 * Return: return the address of the new memory allocated
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *dir = *head, *temp = NULL, *trans = *head, *new = NULL;

	if (!head)
		return (NULL);
	while (dir)
	{
		if (dir->n > number)
			break;
		dir = dir->next;
	}
	while (trans->next)
	{
		if (trans->next == dir)
		{
			temp = trans;
			break;
		}
		trans = trans->next;
	}
	new = malloc(sizeof(new));
	if (!new)
		return (NULL);
	new->n = number;
	temp->next = new;
	new->next = dir;
	return (new);
}
