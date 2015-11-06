A binary heap is a binary tree data structure.  It has a shape property and a
heap property

Shape prop:

Tree should be complete - i.e. all layers of heap should be fully populated,
except the last one.  Last layer is filled left to right.  There is no rule
regarding ordering within a layer of the heap

Heap property:

Heap is either a max heap - parent node is greater than or equal to children;
or min-heap - parent node is smaller than or equal to children

Insertion:

All insertions start out at the bottom layer of the tree, in an unoccupied
child position.  Then, min or max rule is applied and child is swapped with
parent if necessary.

Deletion (or popping, since this data structure is used to implement priority
queues):

Extract the root node and replace it with the last node from the bottom layer.
Then, apply the binary tree rule and exchange parent-child until heap property
is satisfied.  For max-heap, exchange with larger child and for min heap,
exchange with smaller child.

Trying out heapq, which implements a min queue
