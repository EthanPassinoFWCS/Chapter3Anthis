import importlib
x = 1
while True:
  if(x == 12): break
  importlib.import_module(f"TIY3_{x}")
  x+=1
