# vim: foldmethod=marker foldmarker={{{,}}}

from pathlib import Path
import os

from dotenv import load_dotenv


def printValues(label, keys): # {{{
   print(f"\n{label}")
   for key in keys:
      print(f"  {key}={os.environ.get(key)}")
# }}}


scriptDir = Path(__file__).resolve().parent
demoRoot = scriptDir / "demoHierarchy"
level1Dir = demoRoot / "level1"
level2Dir = level1Dir / "level2"
simulatedHomeDir = demoRoot / "simulatedHome"

os.environ["HOME"] = str(simulatedHomeDir)

homeEnvPath = Path.home() / ".env"
rootEnvPath = demoRoot / ".env"
level1EnvPath = level1Dir / ".env"
level2EnvPath = level2Dir / ".env"

requiredFiles = [homeEnvPath, rootEnvPath, level1EnvPath, level2EnvPath]
missingFiles = [str(filePath) for filePath in requiredFiles if not filePath.exists()]
if missingFiles:
   print("Missing expected .env files. Run create-demo-hierarchy.py first:")
   for filePath in missingFiles:
      print(f"  {filePath}")
   raise SystemExit(1)

trackedKeys = [
   "SHARED_NAME",
   "HOME_ONLY",
   "ROOT_ONLY",
   "LEVEL1_ONLY",
   "LEVEL2_ONLY",
   "LAYER",
]

for key in trackedKeys:
   os.environ.pop(key, None)

load_dotenv(homeEnvPath, override=True)
printValues("After loading simulated HOME/.env", trackedKeys)

load_dotenv(rootEnvPath, override=True)
printValues("After loading root .env", trackedKeys)

load_dotenv(level1EnvPath, override=True)
printValues("After loading level1 .env", trackedKeys)

load_dotenv(level2EnvPath, override=True)
printValues("After loading level2 .env", trackedKeys)
