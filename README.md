# Configs to compile "[Bridgex](https://github.com/Dev2Forge/bridgex/)" project to a `.exe`

> [!IMPORTANT]
> Fix Absolute paths

- Configs to compile to "The Exe" (This exe is the main program)
- Configs to compile "The Installer" (Is the program setup)

---

## The Exe

To compile this project (exactly this, "The Exe") with "[Briefcase](https://briefcase.readthedocs.io/en/stable/)", run this commands:

1. Clone the repo
   ```shell
     git clone https://github.com/tutosrive/bridgex-builds-2-exe.git
   ```
3. Create a virtual environment
   ```shell
     python -m venv .venv
   ```
4. Active the virtual environment
   ```shell
     .venv\scripts\activate
   ```
5. Install dependencies
   ```shell
     pip install -r requirements.txt
   ```
6. In any command line (Console, Terminal), execute:
   ```shell
     # By now, only compatibility in windows (.toml is not OK to others.)
     briefcase build windows
   ```

---

## Run Program as Admin

> [!WARNING]
> If you want run the .exe generated as Admin (requires permission), copy this steps

1. Install mt.exe (Windows SDK)
2. Create a file `Bridgex.exe.manifest` on the root of the Build folder (Created by Brifcase) and copy this:
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity version="1.0.0.0" name="Bridgex" />
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel level="requireAdministrator" uiAccess="false"/>
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>
```
3. After, inside of `build/bridgex/windows/app/src/`, open the `CMD` and execute (Replace `{Path to => mt.exe}` with your path):
```shell
{Path to => mt.exe} -nologo -manifest Bridgex.exe.manifest -outputresource:"Bridgex.exe;#1"
```

## The Installer

> [!NOTE]
> (Optional) If you want create a basic and simple "Installer" and not use the "Inno Setup Config", run this
>   ```shell
>     # By now, only compatibility in windows (.toml is not OK to others.)
>     briedfcase package windows
>   ```

### Using [Install Forge](https://installforge.net/download/)

Compile "The Installer" with "[Install Forge](https://installforge.net/download/)".

1. Install "[Install Forge](https://installforge.net/download/)", then open this file: [`install-forge-bridgex-installer.ifp`](https://github.com/Dev2Forge/brigex-build-2-exe/blob/main/configs-exe-installer/install-forge/install-forge-bridgex-installer.ifp)
2. Fix the paths to assets, check that all is OK!

### Using [Inno Setup](https://jrsoftware.org/isdl.php)

Compile "The Installer" with "[Inno Setup](https://jrsoftware.org/isdl.php)".

1. Install the "[Inno Setup](https://jrsoftware.org/isdl.php)", open this file [`Inno-Config.iss`](https://github.com/Dev2Forge/brigex-build-2-exe/blob/main/configs-exe-installer/inno-setup/installer1-bridgex.iss).
2. Sure that the directories paths been OK, not incorrect or NOT valid.
3. Sure that you download all sources (icons, images), and that just compile "The Exe".
