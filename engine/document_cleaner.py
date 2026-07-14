import re
from copy import deepcopy
from docx import Document

from engine.duplicate_detector import DuplicateDetector
from engine.block_matcher import BlockMatcher


class DocumentCleaner:

    def __init__(self):

        self.detector = DuplicateDetector()
        self.matcher = BlockMatcher()

    def clean(self, input_file, output_file):

        blocks = self.detector.split_into_blocks(input_file)

        duplicates = self.matcher.find_duplicates(blocks)

        duplicate_indexes = set()

        for original, duplicate in duplicates:
            duplicate_indexes.add(duplicate - 1)

        cleaned_blocks = []

        for i, block in enumerate(blocks):

            if i not in duplicate_indexes:
                cleaned_blocks.append(block)

        new_doc = Document()

        number = 1

        title_pattern = re.compile(r"^\d+\.\s+")

        for block in cleaned_blocks:

            for paragraph in block:

                text = paragraph.text

                if title_pattern.match(text):

                    title = re.sub(
                        r"^\d+\.\s+",
                        "",
                        text
                    )

                    title = title.replace("*", "").strip()

                    text = f"{number}. {title}"

                    number += 1

                new_doc.add_paragraph(text)

        new_doc.save(output_file)

        return {
            "original": len(blocks),
            "cleaned": len(cleaned_blocks),
            "removed": len(duplicate_indexes)
        }