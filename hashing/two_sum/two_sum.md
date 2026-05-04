# Two Sum

## 🧩 Pattern
Hashing

## 🧠 Idea
Store previously seen numbers in a hashmap to find complements in O(1) time.

## ⚙️ Approach
- Iterate through the array
- For each number, calculate its complement
- Check if the complement exists in the hashmap
- If yes → return indices
- Otherwise, store the number

## ⏱ Complexity
- Time: O(n)
- Space: O(n)

## ❗ Edge Cases
- Duplicate values
- Negative numbers
- No valid solution

## 💡 Key Insight
Using a hashmap avoids O(n²) brute force by reducing lookup time to O(1).