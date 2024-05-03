import sys
from app_agenda import AppAgenda

print(__name__)

if __name__ == "__main__":
  app = AppAgenda()

  if len(sys.argv) > 1:
    app.le(sys.argv[1])

  app.execute()
