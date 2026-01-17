# =============================================================================
# SSWG — Nix Flake for Deterministic Development Environments
# -----------------------------------------------------------------------------
# This flake provides a reproducible dev-shell matching the Conda environment.
# It supports:
#   • Phase-based generator tooling
#   • CLI execution (Typer)
#   • YAML / JSONSchema validation
#   • GitPython operations for branch/fork governance
#
# This file is intentionally minimal — expansion occurs only when the SSWG
# plugin ecosystem grows.
# =============================================================================

{
  description = "SSWG reproducible development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.simpleFlake {
      inherit self nixpkgs;

      packages = {
        # ---------------------------------------------------------------------
        # Default Development Shell
        # ---------------------------------------------------------------------
        default = { pkgs }:
          pkgs.mkShell {
            name = "sswg-shell";

            # Explicit environment variables for compatibility
            # (ensures Typer/Rich encoding pre-sets work across terminals)
            LANG = "en_US.UTF-8";
            LC_ALL = "en_US.UTF-8";

            # -----------------------------------------------------------------
            # Tooling and Python Stack
            # -----------------------------------------------------------------
            buildInputs = [
              pkgs.git
              pkgs.python311
              pkgs.python311Packages.pip
              pkgs.python311Packages.pyyaml
              pkgs.python311Packages.jsonschema
              pkgs.python311Packages.rich
              pkgs.python311Packages.gitpython
              pkgs.python311Packages.typer
            ];

            # Improve debugging ergonomics for SSWG CLI and generators
            shellHook = ''
              echo "[sswg-shell] Ready — reproducible environment loaded."
              echo "Python version: $(python3 --version)"
            '';
          };
      };
    };
}
