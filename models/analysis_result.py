from dataclasses import dataclass


@dataclass
class AnalysisResult:
    filename: str = ""
    paragraphs: int = 0
    headings: int = 0
    blank_paragraphs: int = 0
    duplicate_sections: int = 0