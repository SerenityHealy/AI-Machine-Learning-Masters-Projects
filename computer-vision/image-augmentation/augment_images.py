# augment_images.py
# Usage:
#   pip install pillow
#   python augment_images.py /path/to/images  /path/to/output   --per-image 3
# If output_dir is omitted, it creates "<input_dir>_aug"
import argparse, os, random, json
from pathlib import Path
from PIL import Image, ImageEnhance

EXTS = {'.jpg','.jpeg','.png','.bmp','.tiff','.tif','.webp'}

def augment_one(img: Image.Image, kind: str):
    if kind == 'flip':
        return img.transpose(Image.FLIP_LEFT_RIGHT)
    if kind == 'rotate':
        angle = random.uniform(-10, 10)
        return img.rotate(angle, resample=Image.BICUBIC, expand=True)
    if kind == 'bright':
        factor = random.uniform(0.8, 1.2)
        return ImageEnhance.Brightness(img).enhance(factor)
    if kind == 'contrast':
        factor = random.uniform(0.8, 1.2)
        return ImageEnhance.Contrast(img).enhance(factor)
    raise ValueError(kind)

def safe_open(path):
    img = Image.open(path)
    img.load()  # ensure it’s readable now
    return img

def prepare_for_save(img, ext):
    if ext in {'.jpg','.jpeg'} and img.mode not in ('RGB','L'):
        return img.convert('RGB')
    return img

def main():
    ap = argparse.ArgumentParser(description="Simple folder-wide image augmentation.")
    ap.add_argument("input_dir")
    ap.add_argument("output_dir", nargs="?", default=None)
    ap.add_argument("--per-image", type=int, default=3, help="How many random augments per image (1–4).")
    args = ap.parse_args()

    in_dir = Path(args.input_dir)
    out_dir = Path(args.output_dir or (str(in_dir) + "_aug"))
    out_dir.mkdir(parents=True, exist_ok=True)

    kinds = ['flip','rotate','bright','contrast']
    report = {"source_dir": str(in_dir), "output_dir": str(out_dir),
              "images": 0, "generated": 0, "ops": kinds}

    for root, _, files in os.walk(in_dir):
        rel = Path(root).relative_to(in_dir)
        (out_dir/rel).mkdir(parents=True, exist_ok=True)
        for fname in files:
            ext = Path(fname).suffix.lower()
            if ext not in EXTS:
                continue
            src = Path(root)/fname
            try:
                img = safe_open(src)
            except Exception:
                continue
            report["images"] += 1
            base = Path(fname).stem

            # keep an original copy beside augments
            orig_out = out_dir/rel/f"{base}__orig{ext}"
            prepare_for_save(img, ext).save(orig_out)

            picks = random.sample(kinds, k=min(max(1, args.per_image), len(kinds)))
            for kind in picks:
                aug = augment_one(img, kind)
                out_path = out_dir/rel/f"{base}__{kind}{ext}"
                prepare_for_save(aug, ext).save(out_path)
                report["generated"] += 1

    with open(out_dir/"README.txt","w") as f:
        f.write("Image Dataset Augmentation Output\n")
        f.write(json.dumps(report, indent=2))
        f.write("\nEach original image was copied with suffix __orig and augmented using random selections from: ")
        f.write(", ".join(kinds) + ".\n")

if __name__ == "__main__":
    main()
