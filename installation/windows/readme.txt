2025-07-30: Installation 3.13 auf Windows Sandbox mit offiziellem Installer
  - Nicht für alle User, (ohne admin berechtigung)
  - Default Installationsverzeichnis: C:\Users\WDAGUtilityAccount\AppData\Local\Programs\Python\Python313
  - Installation is slow. Following is recommended (https://github.com/microsoft/Windows-Sandbox/issues/68#issuecomment-2684406010)

      Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\CI\Policy" -Name "VerifiedAndReputablePolicyState" -Value "0"
      CiTool.exe -r
  
