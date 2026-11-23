// news-image-20261123 — "The World in One Day", Monday 23 November 2026.
// SPDX-License-Identifier: MIT
//
// The entry is a single original image, entry.png, drawn by
// generate_image.py (flat vector shapes + DejaVu typesetting, no photos,
// no copied artwork). This program just places that image where the
// grader expects it: /output/entry.png. It runs offline, twice, and both
// runs write the same bytes because the input file never changes.
//
// Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
const bytes = readFileSync(join(here, "entry.png"));
if (bytes.length > 1048576) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB gate`);
}
writeFileSync(target, bytes);
console.log(`wrote ${target} (${bytes.length} bytes)`);
