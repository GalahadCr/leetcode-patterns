# Valid Palindrome

## 🧩 Pattern
Two Pointers

## 🧠 Idea
Use two pointers from both ends, skipping non-alphanumeric characters,
and compare characters in a case-insensitive way.

## ⚙️ Approach
- Initialize left and right pointers
- Skip invalid characters
- Compare characters
- Move pointers inward

## ⏱ Complexity
Time: O(n)
Space: O(1)

## 💡 Key Insight
Avoid creating new strings and instead validate in-place using two pointers.