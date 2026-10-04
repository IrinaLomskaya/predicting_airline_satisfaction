from datetime import datetime, timezone
from pathlib import Path
import shutil

import kagglehub


PROJECT_ROOT = Path(__file__).resolve().parents[2]
COMPETITION = "playground-series-s6e10"


def main():
    source = Path(kagglehub.competition_download(COMPETITION))

    snapshot = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    destination = PROJECT_ROOT / "data" / "raw" / snapshot

    # Собственная копия данных, независимая от кеша kagglehub.
    shutil.copytree(source, destination)

    print(f"Данные сохранены: {destination}")
    for file in sorted(destination.rglob("*")):
        if file.is_file():
            print(f"  {file.relative_to(destination)}")


if __name__ == "__main__":
    main()