import re


class BlockMatcher:

    def normalize(self, text):

        # Remove numbering at the beginning of a title
        text = re.sub(r"^\d+\.\s*", "", text, flags=re.MULTILINE)

        # Remove all asterisks
        text = text.replace("*", "")

        # Remove punctuation
        text = re.sub(r"[^\w\s]", "", text)

        # Convert to lowercase
        text = text.lower()

        # Collapse multiple spaces/newlines
        text = re.sub(r"\s+", " ", text)

        return text.strip()


    def fingerprint(self, block):

        lines = []

        for paragraph in block:

            text = paragraph.text.strip()

            if text:
                lines.append(text)

        return self.normalize("\n".join(lines))


    def similarity(self, a, b):

        words_a = set(a.split())
        words_b = set(b.split())

        if not words_a or not words_b:
            return 0

        common = len(words_a & words_b)
        total = len(words_a | words_b)

        return common / total


    def find_duplicates(self, blocks):

        fingerprints = []
        duplicates = []

        for i, block in enumerate(blocks):

            fp = self.fingerprint(block)

            duplicate_found = False

            for j, previous in enumerate(fingerprints):

                score = self.similarity(fp, previous)

                if score >= 0.95:
                    duplicates.append((j + 1, i + 1))
                    duplicate_found = True
                    break

            if not duplicate_found:
                fingerprints.append(fp)

        return duplicates