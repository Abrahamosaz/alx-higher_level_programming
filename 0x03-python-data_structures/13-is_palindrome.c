#include "lists.h"
/**
 * check_palindrome - check if the linked list is palindrome
 * @head: address of the pointer to the start of the linked list
 * @end: pointer to a listint_t
 *
 * Return: return 1 if its a palindrome and 0 otherwise
 */
int check_palindrome(listint_t **head, listint_t *end)
{
	if (!end)
		return (1);
	if (check_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
/**
 * is_palindrome - call the check_palindrome function
 * @head: address of the pointer to ter start of the list
 *
 * Return: return 1 if True and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (0);
	return (check_palindrome(head, *head));
}
