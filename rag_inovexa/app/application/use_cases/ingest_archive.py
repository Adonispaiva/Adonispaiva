"""Caso de uso de ingestão de pacotes ZIP."""

from dataclasses import dataclass

from app.infrastructure.parsing.zip_parser import ZipParser


@dataclass
class IngestArchiveUseCase:
    """Enumera conteúdo de arquivo ZIP para pipeline de ingestão."""

    parser: ZipParser

    def execute(self, archive_path: str) -> dict:
        files = self.parser.parse(archive_path)
        return {
            "archive_path": archive_path,
            "total_files": len(files),
            "files": files,
        }
