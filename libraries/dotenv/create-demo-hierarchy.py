# vim: foldmethod=marker foldmarker={{{,}}}

from pathlib import Path
import os


def writeEnvFile(filePath, lines): # {{{
   filePath.parent.mkdir(parents=True, exist_ok=True)
   filePath.write_text("\n".join(lines) + "\n", encoding="utf-8")
# }}}


scriptDir = Path(__file__).resolve().parent
demoRoot = scriptDir / "demoHierarchy"
level1Dir = demoRoot / "level1"
level2Dir = level1Dir / "level2"
simulatedHomeDir = demoRoot / "simulatedHome"

simulatedHomeDir.mkdir(parents=True, exist_ok=True)
os.environ["HOME"] = str(simulatedHomeDir)

homeEnvPath = Path.home() / ".env"
if not homeEnvPath.exists():
   writeEnvFile(homeEnvPath, [
      "SHARED_NAME=fromHome",
      "HOME_ONLY=homeOnlyValue",
      "LAYER=home",
   ])
   print(f"Created simulated HOME .env: {homeEnvPath}")
else:
   print(f"Reusing simulated HOME .env: {homeEnvPath}")

rootEnvPath = demoRoot / ".env"
level1EnvPath = level1Dir / ".env"
level2EnvPath = level2Dir / ".env"

writeEnvFile(rootEnvPath, [
   "SHARED_NAME=fromRoot",
   "ROOT_ONLY=rootOnlyValue",
   "LAYER=root",
])

writeEnvFile(level1EnvPath, [
   "SHARED_NAME=fromLevel1",
   "LEVEL1_ONLY=level1OnlyValue",
   "LAYER=level1",
])

writeEnvFile(level2EnvPath, [
   "SHARED_NAME=fromLevel2",
   "LEVEL2_ONLY=level2OnlyValue",
   "LAYER=level2",
])

print("\nCreated or refreshed demo hierarchy:")
print(f"  {demoRoot}")
print(f"  {level1Dir}")
print(f"  {level2Dir}")
print(f"  simulated HOME={simulatedHomeDir}")
