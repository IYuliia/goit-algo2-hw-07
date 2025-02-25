### Task 1: Optimizing Data Access Using LRU Cache  

#### **Objective:**  
Implement a program to optimize query processing for an array of numbers using an **LRU (Least Recently Used) cache**.  

---

### **Technical Requirements**  

1. You are given an array of size **N** consisting of positive integers (**1 ≤ N ≤ 100,000**). You need to process **Q queries** (**1 ≤ Q ≤ 50,000**) of the following types:  

   - **Range(L, R)** – Find the sum of elements in the range from index **L** to **R** (inclusive).  
   - **Update(index, value)** – Replace the element at **index** with a new **value**.  

2. **Implement four functions to handle the array:**  

   - `range_sum_no_cache(array, L, R)`  
     - Computes the sum of elements in the range `[L, R]` **without using a cache**.  
     - The result must be calculated from scratch for each query.  

   - `update_no_cache(array, index, value)`  
     - Updates the value of an element at the given **index** **without using a cache**.  

   - `range_sum_with_cache(array, L, R)`  
     - Computes the sum of elements in the range `[L, R]` **using an LRU cache**.  
     - If the sum for this range was calculated before, it should be retrieved from the cache; otherwise, the result is computed and stored in the cache.  

   - `update_with_cache(array, index, value)`  
     - Updates the value of an element at the given **index**.  
     - **Removes all affected cache entries** that become invalid due to the change.  

3. **Testing:**  
   - Create an array of **100,000 elements** filled with **random numbers**.  
   - Generate **50,000 queries** (**Range and Update**) in a random order.  
   - Example query list:  
     ```python
     [('Range', 46943, 91428), ('Range', 5528, 29889), ('Update', 77043, 78), ...]
     ```  

4. **Cache Configuration:**  
   - Use an **LRU cache of size K = 1000** to store precomputed results for **Range queries**.  
   - The cache should **automatically remove** the least recently used items when it reaches its maximum capacity.  

5. **Performance Comparison:**  
   - Measure the execution time for queries:  
     1. **Without caching.**  
     2. **With LRU caching.**  
   - Output the execution time for both approaches.  

   ### **Task 2: Performance Comparison of Fibonacci Computation Using LRU Cache and Splay Tree**  

#### **Objective:**  
Implement a program to compute Fibonacci numbers using two different approaches:  
1. **LRU Cache** (@lru_cache decorator)  
2. **Splay Tree** (to store previously computed values)  

Compare their performance by measuring the **average execution time** for each approach.  

---

### **Technical Requirements**  

1. **Implement two functions for computing Fibonacci numbers:**  

   - **`fibonacci_lru(n)`**  
     - Uses the **`@lru_cache`** decorator to cache results.  
     - Allows previously computed Fibonacci numbers to be reused.  

   - **`fibonacci_splay(n, tree)`**  
     - Uses a **Splay Tree** data structure to store computed Fibonacci values.  
     - If `n` has already been calculated, it is retrieved from the tree. Otherwise, it is computed, stored in the Splay Tree, and returned.  

2. **Measure execution time for each approach:**  
   - Generate Fibonacci numbers for **n = 0, 50, 100, ..., 950** (increments of 50).  
   - Use the `timeit` module to measure execution time.  
   - Compute the **average execution time** for each approach.  

3. **Plot a performance comparison graph:**  
   - Use `matplotlib` to plot execution time.  
   - **X-axis**: Fibonacci number index **n**.  
   - **Y-axis**: Average execution time in **seconds**.  
   - Include a **legend** to differentiate between "LRU Cache" and "Splay Tree" approaches.  

4. **Draw conclusions** based on the graph:  
   - Analyze which approach performs better for different values of `n`.  

5. **Display results in a table:**  
   - Format a table showing `n`, **average execution time** for LRU Cache, and **average execution time** for Splay Tree.  
   - Ensure readability with proper alignment.  