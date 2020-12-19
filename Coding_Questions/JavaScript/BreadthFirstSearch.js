// ---Breadth-First Search---

class Node {
  constructor(name) {
    this.name = name;
    this.children = [];
  }

  addChild(name) {
    this.children.push(new Node(name));
    return this;
  }

  breadthFirstSearch(array) {
    let queue = [this];

    while (queue.length > 0) {
      const currentElement = queue.shift();
      array.push(currentElement.name);
      for (const child of currentElement.children) {
        queue.push(child);
      }
    }

    return array;
  }
}
