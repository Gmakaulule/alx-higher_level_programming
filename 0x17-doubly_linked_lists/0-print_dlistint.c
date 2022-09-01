#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

size_t print_dlistint(const dlistint_t *h)
{
   const dlistint_t *temp;
   size_t count = 0;

    if(h == NULL)
    {
        printf("list is empty");
    }
    else
    {
        for(temp = h;temp != NULL;temp = temp->next)
        {
            printf("%d\n",temp->n);
            count++;
        }
    }
        return(count);
}