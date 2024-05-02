import os
import os.path
import sys

caminho = "i/j/k"

print(os.path.abspath(caminho))
print(os.path.basename(caminho))
print(os.path.dirname(caminho))
print(os.path.split(caminho))
print(os.path.splitext("arquivo.txt"))
print(os.path.splitdrive("c:/Windows"))

for root, dirs, files in os.walk(sys.argv[1]):
  print("\nCaminho:", root)

  for dir in dirs:
    print(f"\t|->{dir}/")
  for file in files:
    print(f"\t->{file}")

  print(f"{len(dirs)} diretório(s), {len(files)} arquivo(s).")
