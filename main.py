from PIL import Image

image_path = "bot.png"
img = Image.open(image_path).convert("RGB")

target_width = 32
target_height = 32
img = img.resize((target_width, target_height))

grid_rows = []

for y in range(target_height - 1, -1, -1):
  row_pixels = []
  # Dari kiri ke kanan
  for x in range(target_width):
    r, g, b = img.getpixel((x, y))
    row_pixels.append(f"{{{r},{g},{b}}}")
  grid_rows.append("{" + ",".join(row_pixels) + "}")

output_string = "{" + ",".join(grid_rows) + "}"

with open(f"{image_path.split('.')[0]}.txt", "w") as f:
  f.write(output_string)

print(
    "Selesai! Hasil urutan dari bawah ke atas sudah disimpan di"
)