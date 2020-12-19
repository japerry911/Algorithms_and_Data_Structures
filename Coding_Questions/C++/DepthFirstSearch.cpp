#include <utility>

// ---Depth-First Search---


#include <vector>


class Node {
public:
    std::string name;
    std::vector<Node *> children;

    explicit Node(std::string str) { name = std::move(str); }

    std::vector<std::string> depth_first_search(std::vector<std::string> *array) {
        array->push_back(name);
        for (const auto c : children) {
            c->depth_first_search(array);
        }
        return *array;
    }

    Node *addChild(const std::string &name_input) {
        Node *child = new Node(name_input);
        children.push_back(child);
        return this;
    }
};