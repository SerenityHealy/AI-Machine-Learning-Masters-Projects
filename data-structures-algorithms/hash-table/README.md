# Hash Table - Social Media Recommendations

A custom hash table implementation for storing and managing social media user recommendations.

## Overview

This project demonstrates a hash table (hash map) implementation from scratch, applying it to a social media recommendation system where users have personalized content suggestions.

## Features

- **Custom Hash Table**: Built from scratch using Python
- **Collision Handling**: Uses chaining (separate chaining)
- **CRUD Operations**: Insert, Get, Delete
- **Dynamic Size**: Configurable table size
- **User Recommendations**: Stores lists of recommendations per user

## Usage

```bash
python hash_table_recommendations.py
```

## Example Output

```
Recommendations for user491: ['a', 'b', 'c']
Recommendations for user202: ['x', 'y']
Updated recommendations for user491: ['a', 'b', 'c', 'd']
After deletion, user491: None
```

## Hash Table Implementation

### Class: HashTable

**Methods**:

**`__init__(size=10)`**
- Initializes table with specified size
- Creates list of empty lists (buckets)

**`_hash(key)`**
- Hash function using Python's built-in hash()
- Maps key to index: `hash(key) % size`

**`insert(key, value)`**
- Adds or updates key-value pair
- Updates if key exists
- Appends if key is new

**`get(key)`**
- Retrieves value for given key
- Returns None if not found

**`delete(key)`**
- Removes key-value pair
- Returns True if successful, False if not found

## How It Works

### Hash Function
```python
def _hash(self, key):
    return hash(key) % self.size
```
Maps any key to index 0-(size-1)

### Collision Handling (Chaining)
```
Index 0: [["user491", [...]], ["user999", [...]]]
Index 1: []
Index 2: [["user202", [...]]]
Index 3: []
...
```

When multiple keys hash to same index, they're stored in a list (chain).

### Insert Operation
1. Compute hash index
2. Check if key exists in chain
3. If exists: update value
4. If new: append to chain

### Get Operation
1. Compute hash index
2. Search chain for matching key
3. Return value if found, None otherwise

### Delete Operation
1. Compute hash index
2. Find key in chain
3. Remove from list
4. Return success status

## Use Case: Social Media Recommendations

This hash table stores user recommendations:
- **Key**: User ID (e.g., "user491")
- **Value**: List of recommended content (e.g., ["a", "b", "c"])

### Operations Demonstrated

```python
# Insert new user
recommendations.insert("user491", ["a", "b", "c"])

# Get recommendations
recs = recommendations.get("user491")  # ['a', 'b', 'c']

# Update recommendations
recommendations.insert("user491", ["a", "b", "c", "d"])

# Delete user
recommendations.delete("user491")
```

## Time Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insert    | O(1)         | O(n)*      |
| Get       | O(1)         | O(n)*      |
| Delete    | O(1)         | O(n)*      |

*Worst case occurs when all keys hash to same index (all in one chain)

## Space Complexity

**O(n)** where n = number of key-value pairs

## Hash Table Characteristics

### Advantages
- Fast average-case lookups: O(1)
- Dynamic key-value storage
- Flexible key types
- Efficient for large datasets

### Disadvantages
- No ordering of keys
- Worst-case O(n) on collisions
- Memory overhead for table size
- Hash function quality matters

## Collision Resolution Strategies

This implementation uses **Separate Chaining**:
- Each index holds a list
- Multiple items can exist at same index
- Simple to implement
- Dynamic size per bucket

**Alternatives**:
- **Open Addressing**: Find next empty slot
- **Double Hashing**: Use second hash function
- **Robin Hood Hashing**: Minimize probe variance

## Load Factor

**Load Factor** = n / size
- n = number of items
- size = table size

**Good practice**: Keep load factor < 0.7

When load factor too high:
- Resize table (rehashing)
- Double size
- Reinsert all items

## Technical Details

**Language**: Python 3
**Data Structure**: Hash Table (Hash Map)
**Collision Method**: Separate Chaining
**Concepts**:
- Hashing
- Hash functions
- Collision resolution
- Key-value storage
- List of lists structure

## Learning Outcomes

- Understanding hash tables
- Implementing hash functions
- Collision handling techniques
- Time/space complexity analysis
- When to use hash tables vs other structures
- CRUD operations
- Data structure design

## Applications

Hash tables are used for:
- **Dictionaries**: Python's dict
- **Caching**: Fast data retrieval
- **Database Indexing**: Quick lookups
- **Symbol Tables**: Compiler/interpreter
- **Sets**: Unique element storage
- **Counting**: Frequency maps
- **Memoization**: Dynamic programming

## Possible Enhancements

1. **Resizing**: Auto-resize when load factor > threshold
2. **Better Hash Function**: Reduce collisions
3. **Open Addressing**: Alternative collision method
4. **Performance Metrics**: Track collisions and load factor
5. **Generic Types**: Support any value type
6. **Iterator**: Make iterable
7. **Load Factor Check**: Warning when too high
8. **Visualization**: Show table structure
9. **Comparison**: Benchmark vs Python's dict
10. **Persistent Storage**: Save/load from file
