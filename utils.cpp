#include "utils.hpp"

ValPos min_int(int* arr, int left, int right) {
    int min = arr[left];
    int min_pos = left;

    for (int i = left + 1; i <= right; i++) {
        if (min > arr[i]) {
            min = arr[i];
            min_pos = i;
        }
    }

    return ValPos{min, min_pos};
}
