# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

## My reflection

I learned how two searches could give the same answer while doing very different amounts of work. Linear search checked items one at a time, while binary search used the sorted order to rule out roughly half the remaining items at each step. The difference was easy to miss on a tiny list, but it stood out when I searched 100,000 values.

The trickiest part for me was keeping the binary search boundaries straight. After checking the midpoint, I had to leave it out of the next search range so I would not check it again. Testing an empty list, a list with one item, and a target at the end helped me verify that the search stopped and returned the right result.

My library example helped me see the tradeoff. If I had only needed to find one book in an unsorted shipment, I would have scanned the list directly and skipped the sorting work. If staff had needed to look up book IDs throughout the day, keeping the inventory sorted would have made binary search a better fit. The better choice depended on how the data was organized and how often it was searched.
