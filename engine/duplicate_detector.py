import re
from docx import Document


class DuplicateDetector:

    def split_into_blocks(self, filepath):

        document = Document(filepath)

        blocks = []
        current_block = []

        # Match titles like:
        # 1. TITLE
        # 25. SOME TITLE*
        title_pattern = re.compile(r"^\d+\.\s+")

        for paragraph in document.paragraphs:

            text = paragraph.text.strip()

            if text == "":
                current_block.append(paragraph)
                continue

            is_title = False

            if title_pattern.match(text):

                title = re.sub(r"^\d+\.\s+", "", text)

                letters = [c for c in title if c.isalpha()]
                uppercase = [c for c in letters if c.isupper()]

                if letters:
                    ratio = len(uppercase) / len(letters)

                    if ratio >= 0.8:
                        is_title = True

            if is_title:

                if current_block:
                    blocks.append(current_block)

                current_block = [paragraph]

            else:

                current_block.append(paragraph)

        if current_block:
            blocks.append(current_block)

        return blocks