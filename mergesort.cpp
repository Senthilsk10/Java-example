#include<iostream>
using namespace std;

void merge(int arr[], int l, int m, int r) {
    int i = l;
    int j = m + 1;
    int k = l;
    int temp[5];
    while (i <= m && j <= r) {
        if (arr[i] <= arr[j]) {
            temp[k] = arr[i];
            i++;
        } else {
            temp[k] = arr[j];
            j++;
        }
        k++;
    }
    while (i <= m) {
        temp[k] = arr[i];
        i++;
        k++;
    }
    while (j <= r) {
        temp[k] = arr[j];
        j++;
        k++;
    }
    for (int s = l; s <= r; s++) {
        arr[s] = temp[s];
    }
}

void mergesort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;  // Corrected calculation of middle index
        mergesort(arr, l, m);
        mergesort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    std::cout << "enter the values";
    int myarr[5];
    int i;
    for (i = 0; i < 5; i++) {
        std::cin >> myarr[i];
    }

    std::cout << "\nbefore merge sorting applied";
    for (i = 0; i < 5; i++) {
        std::cout << myarr[i] << "\n";
    }
    mergesort(myarr, 0, 4);  // Change the second argument to the last index (size - 1)
    std::cout << "\nafter merge sorting applied\n";
    for (i = 0; i < 5; i++) {
        std::cout << myarr[i] << "\n";
    }
    return 0;
}
