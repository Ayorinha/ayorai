$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$target = Join-Path $root "runtime\oneocr"
New-Item -ItemType Directory -Force -Path $target | Out-Null
$pkg = Get-AppxPackage -Name "Microsoft.ScreenSketch" -AllUsers | Sort-Object Version -Descending | Select-Object -First 1
if (-not $pkg) { throw "Microsoft Snipping Tool (Microsoft.ScreenSketch) was not found. Install/update Snipping Tool and run again." }
$source = Join-Path $pkg.InstallLocation "SnippingTool"
foreach ($name in @("oneocr.dll","onnxruntime.dll","oneocr.onemodel")) {
  $src = Join-Path $source $name
  if (-not (Test-Path $src)) { throw "Missing $name in $source" }
  Copy-Item -LiteralPath $src -Destination (Join-Path $target $name) -Force
  Write-Host "[OK] $name"
}
Write-Host "OneOCR runtime installed at $target"
