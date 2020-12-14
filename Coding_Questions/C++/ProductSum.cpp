// ---Product Sum---

#include <vector>
#include <any>


int product_sum(std::vector<any> array, int depth=1) {
    int running_sum = 0;

    for (const auto element : array) {
        if (element.type() == typeid(std::vector<any>)) {
            running_sum += product_sum(any_cast<std::vector<any>>(element), depth + 1);
        } else {
            running_sum += any_cast<int>(element);
        }
    }

    return running_sum * depth;
}
