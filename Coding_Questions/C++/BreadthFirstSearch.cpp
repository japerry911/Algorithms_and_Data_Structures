// ---Breadth-First Search---


#include <vector>
#include <queue>


class Node {
public:
    std::string name;
    std::vector<Node *>children;

    Node(std::string str) {name = str;}

    std::vector<std::string> breadth_first_search(std::vector<std::string> *array) {
        std::queue<Node *> queue = {this};

        while (queue.size() > 0) {
            Node *current_node = queue.front();
            queue.pop();
            array->push_back(current_node->name);
            for (const auto c : current_node->children) {
                queue.push(c);
            }
        }

        return *array;
    }

    Node *add_child(std::string name) {
        Node *child = new Node(name);
        children.push_back(child);
        return this;
    }
};