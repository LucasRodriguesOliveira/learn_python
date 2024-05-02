def par(x):
  return x % 2 == 0

def par_ou_impar(x):
  if par(x):
    return "Par"

  return "Impar"

print(par_ou_impar(4))
print(par_ou_impar(5))
