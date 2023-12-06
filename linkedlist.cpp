#include<iostream>
#include<string.h>

using namespace  std;
//node definition
struct node{
    int data;//for data storage
    struct node* next;//for linking the next node ptr
};

struct node *head = NULL;//setting up the headnode pointer as null as when we try to print it it will not print
struct node * current = NULL;//as it shows the last updated node ptr so when a new node is updated ten this will used for updating part

//displaying the list
int display(){
    struct node *p = head;//assign the p with its pointer reference and assing the head's to it where the data showing will be started
    while(p != NULL){
        std::cout<<p->data<<"\n";//printing out
        p = p->next;//it will take the pointer of next element and make the p node as this pointer

    }
}

int insert(int data){
    struct node *lk = (struct node*) malloc(sizeof(struct node));//allocate memory for the lk
    lk->data = data;//assign the value
    lk->next = head;//assign it to head null value showin that this this the last element

    head = lk;// now the head will have data of lk and next pointer as null and the every adds will be on top of it

}
void deletenode(int key){
   struct node *temp = head, *prev;
   if (temp != NULL && temp->data == key) {
      head = temp->next;
      return;
   }

   // Find the key to be deleted
   while (temp != NULL && temp->data != key) {
      prev = temp;
      temp = temp->next;
   }

   // If the key is not present
   if (temp == NULL) return;

   // Remove the node
   prev->next = temp->next;
}
/*Certainly! Let's go through the process of searching for and deleting a node with a specific key in a linked list with five nodes. For this example, let's assume the linked list has the following structure:

```
1 -> 3 -> 7 -> 9 -> 5
```

Now, let's say we want to delete a node with the key `7`. We will walk through the code with this example:

```c
void deletenode(int key) {
   struct node *temp = head, *prev;

   // Check if the head node contains the key
   if (temp != NULL && temp->data == key) {
      head = temp->next;
      return;
   }

   // Find the key to be deleted
   while (temp != NULL && temp->data != key) {
      prev = temp;
      temp = temp->next;
   }

   // If the key is not present
   if (temp == NULL) return;

   // Remove the node
   prev->next = temp->next;
}
```

1. Initially, `temp` and `prev` are both set to the `head` of the linked list:

   ```
   temp -> 1 -> 3 -> 7 -> 9 -> 5
   prev -> 1 -> 3 -> 7 -> 9 -> 5
   ```

2. The code checks if the head node (`temp`) contains the key (7), but in this case, it does not match. So, it moves to the next part of the code.

3. The `while` loop is entered, and it iterates through the list until it finds the node with the key (7):

   ```
   temp -> 1 -> 3 -> 7 -> 9 -> 5
   prev -> 1 -> 3
   ```

4. The code exits the loop as it found the node with the key (7).

5. The node with the key (7) is removed by updating the `next` pointer of the previous node (`prev`):

   ```
   temp -> 7 -> 9 -> 5
   prev -> 1 -> 3
   ```

Now, the linked list after deleting the node with the key (7) becomes:

```
1 -> 3 -> 9 -> 5
```

This is a simplified walkthrough, and in a real-world scenario, you'd need to consider additional edge cases and error handling. The provided code assumes a singly linked list structure. Total words count: 218*/

int main(){
    display();
    insert(34);
    insert(33);
    deletenode(34);
    insert(36);
    insert(35);
    display();
    deletenode(35);
    display();
    
    return 0;
}


//and thats it we have to memeorize the logics and apply the user based part for lab exam