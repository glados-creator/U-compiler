#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node_t *next;
} node_t;

void list_print(node_t *head)
{
    node_t *current = head;

    while (current != NULL)
    {
        printf("%d\n", current->data);
        current = current->next;
    }
}

void list_append(node_t *head, int data)
{
    node_t *current = head;
    while (current->next != NULL)
    {
        current = current->next;
    }

    /* now we can add a new variable */
    current->next = (node_t *)malloc(sizeof(node_t));
    current->next->data = data;
    current->next->next = NULL;
}

void list_insert(node_t **head, int data)
{
    node_t *new_node;
    new_node = (node_t *)malloc(sizeof(node_t));

    new_node->data = data;
    new_node->next = *head;
    *head = new_node;
}

int list_pop(node_t **head)
{
    int retval = -1;
    node_t *next_node = NULL;

    if (*head == NULL)
    {
        return -1;
    }

    next_node = (*head)->next;
    retval = (*head)->data;
    free(*head);
    *head = next_node;

    return retval;
}

int list_remove_last(node_t *head)
{
    int retval = 0;
    /* if there is only one item in the list, remove it */
    if (head->next == NULL)
    {
        retval = head->data;
        free(head);
        return retval;
    }

    /* get to the second to last node in the list */
    node_t *current = head;
    while (current->next->next != NULL)
    {
        current = current->next;
    }

    /* now current points to the second to last item of the list, so let's remove current->next */
    retval = current->next->data;
    free(current->next);
    current->next = NULL;
    return retval;
}

int list_remove_by_index(node_t **head, int n)
{
    int i = 0;
    int retval = -1;
    node_t *current = *head;
    node_t *temp_node = NULL;

    if (n == 0)
    {
        return list_pop(head);
    }

    for (i = 0; i < n - 1; i++)
    {
        if (current->next == NULL)
        {
            return -1;
        }
        current = current->next;
    }

    if (current->next == NULL)
    {
        return -1;
    }

    temp_node = current->next;
    retval = temp_node->data;
    current->next = temp_node->next;
    free(temp_node);

    return retval;
}

typedef struct tree
{
    int data;
    struct tree_t *left;
    struct tree_t *right;
} tree_t;

enum keywords {
    Token_Plus,
    Token_Minus,
    Token_Mul,
    Token_Div,
    Token_Auto,
    Token_Break,
    Token_Case,
    Token_Char,
    Token_Const,
    Token_Continue,
    Token_Default,
    Token_Do,
    Token_Double,
    Token_Else,
    Token_Enum,
    Token_Extern,
    Token_Float,
    Token_For,
    Token_Goto,
    Token_If,
    Token_Int,
    Token_Long,
    Token_Register,
    Token_Return,
    Token_Short,
    Token_Signed,
    Token_Sizeof,
    Token_Static,
    Token_Struct,
    Token_Switch,
    Token_Typedef,
    Token_Union,
    Token_Unsigned,
    Token_Void,
    Token_Volatile,
    Token_While
};

enum action {
    VAR_ASS,
    FUNC_DEF,
    FUNC_CALL,
    LOOP_COND,
    
};

void Parse(char inptext){

}