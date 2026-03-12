"""Parser de arquivos ZIP com saneamento básico."""

from pathlib import Path
import zipfile

IGNORED_NAMES = {".DS_Store"}
IGNORED_PREFIXES = ("__MACOSX/",)


class ZipParser:
    """Inspeciona conteúdo de um ZIP sem extraí-lo."""

    def parse(self, archive_path: str) -> list[dict[str, str | int]]:
        discovered: list[dict[str, str | int]] = []
        with zipfile.ZipFile(archive_path, "r") as archive:
            for info in archive.infolist():
                internal_path = info.filename
                if any(internal_path.startswith(prefix) for prefix in IGNORED_PREFIXES):
                    continue
                if Path(internal_path).name in IGNORED_NAMES or info.is_dir():
                    continue

                ext = Path(internal_path).suffix.lower().lstrip(".") or "none"
                discovered.append(
                    {
                        "internal_path": internal_path,
                        "extension": ext,
                        "size": info.file_size,
                        "estimated_category": self._estimate_category(ext),
                    }
                )
        return discovered

    @staticmethod
    def _estimate_category(ext: str) -> str:
        if ext in {"md", "txt", "docx", "pdf"}:
            return "document"
        if ext in {"csv", "xlsx"}:
            return "tabular"
        if ext in {"png", "jpg", "jpeg"}:
            return "image"
        return "other"
