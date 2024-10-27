{ pkgs }: {
    deps = [
        pkgs.python3
        pkgs.python3Packages.pip
        pkgs.gcc
        pkgs.python3Packages.pybind11
        pkgs.cmake
    ];

    # Filtyp-konfiguration för .cript
    languages.cscript = {
        extensions = ["cript"];
        icon = "./cscript/icons/cscript.png";
        displayName = "CScript";
    };

    # MIME-typ konfiguration
    mimeTypes = {
        "text/x-cscript" = {
            extensions = ["cript"];
            icon = "./cscript/icons/cscript.png";
        };
    };
}