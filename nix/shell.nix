let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.pandas
      python-pkgs.requests
      python-pkgs.pyqt5
      python-pkgs.keras
      python-pkgs.tensorflow
      python-pkgs.numpy
      python-pkgs.pyqtgraph
      python-pkgs.openpyxl
      python-pkgs.matplotlib
    ]))
  ];
  nativeBuildInputs = with pkgs; [
    ruff
  ];
}
