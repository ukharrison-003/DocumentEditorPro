from docx import Document
from models.analysis_result import AnalysisResult


class DocumentAnalyzer:

    def analyze(self, filepath):

        document = Document(filepath)

        result = AnalysisResult()

        result.filename = filepath.split("\\")[-1]

        result.paragraphs = len(document.paragraphs)

        blank = 0
        headings = 0

        for paragraph in document.paragraphs:

            text = paragraph.text.strip()

            if text == "":
                blank += 1

            if paragraph.style.name.startswith("Heading"):
                headings += 1

        result.blank_paragraphs = blank
        result.headings = headings

        return result