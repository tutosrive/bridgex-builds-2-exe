# Configs to compile "[Bridgex](https://github.com/Dev2Forge/bridgex/)" project to a `.exe`

- Configs to compile to "The Exe" (This exe is the main program)
- Configs to compile "The Installer" (Is the program setup)

---

## The Exe

To compile this project (exactly this, "The Exe") with "[Briedfcase](https://briefcase.readthedocs.io/en/stable/)", run this commands:

1. Clone the repo
   ```shell
     git clone https://github.com/Dev2Forge/bridgex-builds-2-exe.git
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
     briedfcase build windows
   ```

## The Installer

> [!NOTE]
> (Optional) If you want create a basic and simple "Installer" and not use the "Inno Setup Config", run this
>   ```shell
>     # By now, only compatibility in windows (.toml is not OK to others.)
>     briedfcase package windows
>   ```

Compile "The Installer" with "[Inno Setup](https://jrsoftware.org/isdl.php)".

1. Install the "[Inno Setup](https://jrsoftware.org/isdl.php)", open this file [`Inno-Config.iss`](https://github.com/Dev2Forge/brigex-build-2-exe/blob/main/configs-exe-installer/installer1-bridgex.iss).
2. Sure that the directories paths been OK, not incorrect or NOT valid.
3. Sure that you download all sources (icons, images), and that just compile "The Exe".
