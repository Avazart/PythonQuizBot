import argparse
import logging
import time
from pathlib import Path

import httpcore
import polib
from googletrans import Translator
from googletrans.models import Translated

DEFAULT_SRC_LANG = "en"

fmt = "[%(asctime)s] %(message)s (%(levelname)s) [%(name)s]"
date_fmt = "%d.%m.%y %H:%M:%S"
logging.basicConfig(level=logging.DEBUG, format=fmt, datefmt=date_fmt)
for logger_name in ("hpack", "httpx"):
    logging.getLogger(logger_name).setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)


def main() -> None:
    translator = Translator()

    parser = argparse.ArgumentParser()
    parser.add_argument("-pd", "--project_dir", type=Path, default=Path("."))
    args = parser.parse_args()

    locales_dir = args.project_dir / "locales"
    for po_file_path in locales_dir.rglob("*.po"):
        target_lang = po_file_path.parent.parent.id
        logger.info(f"[{target_lang}]")

        po_file = polib.pofile(str(po_file_path))
        for entry in po_file:
            if not entry.msgstr:
                try:
                    tr: Translated = translator.translate(
                        entry.msgid,
                        dest=target_lang,
                        src=DEFAULT_SRC_LANG,
                    )
                    logger.debug(f"{entry.msgid} -> {tr.text}")
                    entry.msgstr = tr.text
                    time.sleep(0.2)
                except httpcore._exceptions.ReadTimeout as e:
                    logger.error(e)
                    time.sleep(1)
        po_file.save(str(po_file_path))


if __name__ == "__main__":
    main()
