#include "lists.h"
/**
 * check - cycle
 * @list:linken list
 * Return: 0 if no cycle ,1 if there is a cycle
 */
int check_cycle(listint_t *list);
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;

		if (s == f)
			return (1);
	}
	return (0);
}
