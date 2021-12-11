class Scoring:
    CORRUPTED_SCORES = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    INCOMPLETE_SCORES = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    def corrupted_scores(self, illegal_characters):
        return [self.CORRUPTED_SCORES[character] for character in illegal_characters]

    def incomplete_scores(self, closing_sequences):
        scores = []

        for sequence in closing_sequences:
            total_score = 0

            for character in sequence:
                total_score = total_score * 5 + self.INCOMPLETE_SCORES[character]

            scores.append(total_score)

        return sorted(scores)
