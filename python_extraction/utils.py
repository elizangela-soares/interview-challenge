from pathlib import Path
from typing import Iterable, List


def chunk_list(items: List[str], chunk_size: int) -> Iterable[List[str]]:
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]


def build_output_dir(base_path: str, year: int, month: int, day: int, hour: int) -> Path:
    output_dir = (
        Path(base_path)
        / f"year={year}"
        / f"month={month:02d}"
        / f"day={day:02d}"
        / f"hour={hour:02d}"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir