# Analysis

## Layer 4, Head 6

This attention head appears to have learned to pay attention to the token immediately preceding the current token. Each word in the sequence attends strongly to the word that comes directly before it, capturing local preceding context and left-to-right sequential structure. For example, "brown" attends heavily to "quick" (0.80), "fox" attends to "brown" (0.95), and "green" attends to "delicious" (0.86).

Example Sentences:
- The quick brown fox jumps over the lazy [MASK].
- The boy ate a delicious green [MASK].

## Layer 5, Head 6

This attention head appears to pay attention to the relationship between noun modifiers (determiners and adjectives) and the head noun they modify. In noun phrases, the preceding determiners and adjectives direct strong attention to the central noun. In the first example, the determiner "a" (0.82) as well as the adjectives "big" (0.70) and "red" (0.58) all attend directly to the head noun "umbrella". Similarly, in the second example, the determiner "the" (0.90) and adjective "quick" (0.42) attend to the noun "fox".

Example Sentences:
- She opened a big red umbrella in the heavy [MASK].
- The quick brown fox jumps over the lazy [MASK].
