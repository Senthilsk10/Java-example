#include<iostream>
#include<stdlib.h>

struct bst
{
    int data;
    bst* right;
    bst* left;
};

bst* get_newnode(int data){
    bst* node = new bst();
    node->data = data;
    node->right = NULL;
    node->left = NULL;
    return node;
}

bst* insert(bst* root, int data){
    if(root == NULL){
        root = get_newnode(data);
        return root;
    }
    else if(data<= root->data ){
        root->left = insert(root->left,data);
    }
    else{
        root->right = insert(root->right,data);
    }
    return root;
        
}

void display(bst* root) {
    if (root == NULL) {
        return;
    }

    // Display details of the current node
    std::cout << "Data: " << root->data << "\n";
    std::cout << "Left: " << (root->left ? root->left->data : -1) << "\n";
    std::cout << "Right: " << (root->right ? root->right->data : -1) << "\n";
    
    // Display details of left and right subtrees
    display(root->left);
    display(root->right);
}

int main(){
    bst* root = NULL;
    root = insert(root,89);
    root = insert(root,45);
    root = insert(root,34);
    root = insert(root,78);
    display(root);
    
}