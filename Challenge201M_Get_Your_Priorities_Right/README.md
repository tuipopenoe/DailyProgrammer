## Description
### Core
Your priority queue must implement at least these methods:
#### Enqueue.
This method accepts three parameters - a string, priority value A, and priority value B, where the priority values are real numbers (see above). The string is inserted into the priority queue with the given priority values A and B (how you store the queue in memory is up to you!)
#### DequeueA.
This method removes and returns the string from the priority queue with the highest priority A value. If two entries have the same A priority, return whichever was enqueued first.
#### DequeueB.
This method removes and returns the string from the priority queue with the highest priority B value. If two entries have the same B priority, return whichever was enqueued first.
#### Count. 
This method returns the number of strings in the queue.
#### Clear. 
This removes all entries from the priority queue.

### Additional

If you can, implement this method, too:
DequeueFirst. This removes and returns the string from the priority queue that was enqueued first, ignoring priority.
Depending on how you implemented your priority queue, this may not be feasible, so don't get too hung up on this one.

### Extension

Rather than making your priority queue only accept strings, make a generic priority queue, instead. A generic object is compatible with many types. In C++, this will involve the use of templates. More reading resources here. For example, in C#, your class name might look like DualPriorityQueue<TEntry>. Some dynamic languages such as Ruby or Python do not have static typing, so this will not be necessary.