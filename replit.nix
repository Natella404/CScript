{ pkgs }: {
    deps = [
        pkgs.python3
        pkgs.python3Packages.pip
        pkgs.gcc
        pkgs.shared-mime-info
    ];

    env = {
        MIME_TYPES = ''
            text/x-cscript    cript
        '';
    };

    # Filtyp-konfiguration
    languages.cscript = {
        extensions = ["cript"];
        icon = "./icons/cscript.png";
        displayName = "CScript";
        pattern = "**/*.cript";
    };
}