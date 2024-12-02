#include <iostream>

#include "../utils.hpp"

int main(void) {
    int arr[] = {2, 3, 4, 5, 6, 1, 7, 8, 9, 10};

    ValPos result = min_int(arr, 0, 10);

    std::cout << "Found min: " << result.val << " at: " << result.pos
              << std::endl;
}
