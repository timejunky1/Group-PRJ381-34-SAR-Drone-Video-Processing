[Setup]
AppName=Infrared Drone Human Detection System
AppVersion=1.0
DefaultDirName={pf}\Infrared Drone Human Detection System
OutputDir=Output
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Dirs]
Name: "{app}\Docs"; Flags: uninsneveruninstall
Name: "{app}\Dependencies"; Flags: uninsneveruninstall

[Files]
Source: "Path\To\Release\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "Path\To\Documentation\UserGuide.pdf"; DestDir: "{app}\Docs"; Flags: ignoreversion
Source: "Path\To\Documentation\DeveloperGuide.pdf"; DestDir: "{app}\Docs"; Flags: ignoreversion
Source: "Path\To\License.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "Path\To\Dependencies\*"; DestDir: "{app}\Dependencies"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Infrared Drone Human Detection System"; Filename: "{app}\YourMainExecutable.exe"
Name: "{group}\Uninstall Infrared Drone Human Detection System"; Filename: "{uninstallexe}"
Name: "{commondesktop}\Infrared Drone Human Detection System"; Filename: "{app}\YourMainExecutable.exe"

[Run]
Filename: "{app}\YourMainExecutable.exe"; Description: "Launch Infrared Drone Human Detection System"; Flags: nowait postinstall skipifsilent