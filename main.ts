// gta6-meme-x-01 — make.fun entry program (Node 22, standard library only).
//
// The entry is the X post itself: a GTA 6 meme picturing make.fun's ghost,
// posted from a public account. This program's only job is to hand the house
// the post's address: it copies POST.json from the repository root into the
// output directory, where the gate reads it. Nothing else is written, read
// from the network, or decided by the clock, so two runs produce identical
// bytes. It prints nothing on success and exits non-zero with a clear
// message when the copy cannot be done.
//
// Run it the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

function fail(message: string): never {
  console.error(`gta6-meme-x-01: ${message}`);
  process.exit(1);
}

function readPostAddress(path: string): string {
  let raw: string;
  try {
    raw = readFileSync(path, 'utf8');
  } catch (err) {
    fail(`POST.json could not be read: ${(err as Error).message}`);
  }
  let parsed: unknown;
  try {
    parsed = JSON.parse(raw);
  } catch (err) {
    fail(`POST.json is not valid JSON: ${(err as Error).message}`);
  }
  if (typeof parsed !== 'object' || parsed === null || !('url' in parsed)) {
    fail('POST.json must be a JSON object with a "url" field');
  }
  const url = (parsed as { url: unknown }).url;
  if (typeof url !== 'string' || url.length === 0) {
    fail('POST.json "url" must be a non-empty string');
  }
  return url;
}

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const source = join(botDir, 'POST.json');
const target = join(outputDir, 'POST.json');

if (!existsSync(source)) {
  fail(`POST.json not found in ${botDir}`);
}

// Validate before copying so a malformed file fails loudly instead of
// being copied through silently.
readPostAddress(source);

try {
  mkdirSync(outputDir, { recursive: true });
  copyFileSync(source, target);
} catch (err) {
  fail(`could not copy ${source} to ${target}: ${(err as Error).message}`);
}
