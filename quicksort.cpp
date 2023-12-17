#include <iostream>
#include <vector>

using namespace std;

void printArray(int& arr[]) {
    for (int i : arr) {
        cout << i << " ";
    }
    cout << endl;
}

int partition(int& arr[] int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    cout << "Pivot: " << pivot << endl;
    cout << "Partitioning: ";
    printArray(arr);

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);

    cout << "After partition: ";
    printArray(arr);

    return i + 1;
}

void quickSort(int& arr[], int low, int high) {
    if (low < high) {
        int partitionIndex = partition(arr, low, high);

        cout << "Partitioned array: ";
        printArray(arr);

        quickSort(arr, low, partitionIndex - 1);
        quickSort(arr, partitionIndex + 1, high);
    }
}

int main() {
    int& arr[7] = {12, 7, 4, 9, 5, 3, 6};
    int n = arr.size();

    cout << "Original array: ";
    printArray(arr);

    quickSort(arr, 0, n - 1);

    cout << "Sorted array: ";
    printArray(arr);

    return 0;
}
