from dataclasses import dataclass

@dataclass
class AnalysisResult:

    filename: str = ""

    paragraphs: int = 0

    blank_paragraphs: int = 0

    word_headings: int = 0

    smart_topics: int = 0

    day_headings: int = 0

    duplicate_sections: int = 0

    numbering_errors: int = 0