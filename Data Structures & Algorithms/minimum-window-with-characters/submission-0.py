class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        required = {}
        for character in t:
            required[character] = required.get(character, 0) + 1

        current_count = {}
        matching = 0
        n_to_match = len(required)

        start = 0
        solution_start = 0
        solution_length = float("inf")

        for end, character in enumerate(s):
            if character in required:
                current_count[character] = current_count.get(character, 0) + 1

                # Count this character type only when its exact requirement
                # is first satisfied.
                if current_count[character] == required[character]:
                    matching += 1

            while matching == n_to_match:
                window_length = end - start + 1

                if window_length < solution_length:
                    solution_start = start
                    solution_length = window_length

                left_character = s[start]

                if left_character in required:
                    current_count[left_character] -= 1

                    if current_count[left_character] < required[left_character]:
                        matching -= 1

                start += 1

        if solution_length == float("inf"):
            return ""

        return s[solution_start:solution_start + solution_length]