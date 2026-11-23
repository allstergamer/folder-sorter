#!/usr/bin/env python3
"""
Folder Sorter
Sortiert Dateien eines Ordners anhand ihrer Dateiendung in Unterordner.

Beispiele:
    python folder_sorter.py
    python folder_sorter.py "C:/Users/Lisa/Downloads"
    python folder_sorter.py "C:/Users/Lisa/Downloads" --dry-run
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def get_category(file_path: Path) -> str:
    """Gibt den Ordnernamen anhand der Dateiendung zurück."""
    suffix = file_path.suffix.lower()

    if not suffix:
        return "Ohne_Endung"

    # Punkt am Anfang entfernen, z. B. ".pdf" -> "pdf"
    return suffix[1:].upper()


def unique_destination(destination: Path) -> Path:
    """Verhindert das Überschreiben bereits vorhandener Dateien bzw Überschreiben von datein mit selben dateinamen."""
    if not destination.exists():
        return destination

    """stem = name ohne Endung, suffix = Endung, counter = Zähler für die Anzahl der vorhandenen Dateien mit demselben Namen"""
    stem = destination.stem
    suffix = destination.suffix
    counter = 1


    """checkt ob die datei schon existiert, wenn ja wird der counter hochgezählt und erneut geprueft bis  der name passt"""
    while True:
        candidate = destination.with_name(f"{stem}_{counter}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def sort_folder(folder: Path, dry_run: bool = False) -> None:
    """Sortiert alle Dateien direkt im angegebenen Ordner."""
    if not folder.exists():
        raise FileNotFoundError(f"Der Ordner existiert nicht: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Der angegebene Pfad ist kein Ordner: {folder}")

    files = [item for item in folder.iterdir() if item.is_file()]

    if not files:
        print(f"Keine Dateien gefunden in: {folder}")
        return

    print(f"Durchsuche: {folder}")
    print(f"{len(files)} Datei(en) gefunden.\n")

    moved = 0
    errors = 0

    for file_path in files:
        category = get_category(file_path)
        target_folder = folder / category
        destination = unique_destination(target_folder / file_path.name)

        if dry_run:
            print(f"[TEST] {file_path.name} -> {category}/{destination.name}")
            moved += 1
            continue

        try:
            target_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file_path), str(destination))
            print(f"[OK] {file_path.name} -> {category}/{destination.name}")
            moved += 1
        except OSError as error:
            print(f"[FEHLER] {file_path.name}: {error}")
            errors += 1

    print("\nSortierung abgeschlossen.")
    print(f"Verarbeitet: {moved}")
    print(f"Fehler:      {errors}")

    if dry_run:
        print("Testlauf: Es wurden keine Dateien verschoben.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sortiert Dateien anhand ihrer Dateiendung in Unterordner."
    )

    """folder = Ordner, der sortiert werden soll, nargs="?" bedeutet, dass das Argument optional ist, default=Downloads-Ordner"""
    parser.add_argument(
        "folder",
        nargs="?",
        default=str(Path.home() / "Downloads"),
        help="Zu sortierender Ordner (Standard: Downloads)",
    )

    """dry-run = Testlauf, Dateien werden nicht verschoben, nur angezeigt, was verschoben werden würde"""
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Zeigt die geplanten Verschiebungen, ohne Dateien zu verschieben.",
    )

    args = parser.parse_args()
    folder = Path(args.folder).expanduser().resolve()

    try:
        sort_folder(folder, dry_run=args.dry_run)
    except (FileNotFoundError, NotADirectoryError, PermissionError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
