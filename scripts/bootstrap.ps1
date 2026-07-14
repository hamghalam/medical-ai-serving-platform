# ============================================================
# Medical AI Serving Platform
# Bootstrap Script
#
# Creates the complete repository structure.
#
# Author: Mohammad Hamghalam
# ============================================================

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "========================================="
Write-Host " Medical AI Serving Platform Bootstrap"
Write-Host "========================================="
Write-Host ""

# ------------------------------------------------------------
# Project folders
# ------------------------------------------------------------

$folders = @(
    "app",

    "app/api",
    "app/api/routers",
    "app/api/schemas",

    "app/core",

    "app/models",

    "app/services",

    "app/prompts",

    "app/inference",

    "app/storage",

    "app/monitoring",

    "app/utils",

    "tests",

    "docs",

    "scripts",

    "configs",

    "docker"
)

foreach ($folder in $folders) {

    if (!(Test-Path $folder)) {

        New-Item `
            -ItemType Directory `
            -Path $folder | Out-Null

        Write-Host "[Created] $folder"

    }

    else {

        Write-Host "[Exists ] $folder"

    }

}

# ------------------------------------------------------------
# Files
# ------------------------------------------------------------

$files = @(

    "README.md",

    "LICENSE",

    ".gitignore",

    "pyproject.toml",

    ".env.example",

    "app/main.py"
)

foreach ($file in $files) {

    if (!(Test-Path $file)) {

        New-Item `
            -ItemType File `
            -Path $file | Out-Null

        Write-Host "[Created] $file"

    }

    else {

        Write-Host "[Exists ] $file"

    }

}

# ------------------------------------------------------------
# __init__.py
# ------------------------------------------------------------

$packages = @(

    "app",

    "app/api",

    "app/api/routers",

    "app/api/schemas",

    "app/core",

    "app/models",

    "app/services",

    "app/prompts",

    "app/inference",

    "app/storage",

    "app/monitoring",

    "app/utils"
)

foreach ($package in $packages) {

    $initFile = Join-Path $package "__init__.py"

    if (!(Test-Path $initFile)) {

        New-Item `
            -ItemType File `
            -Path $initFile | Out-Null

        Write-Host "[Created] $initFile"

    }

}

Write-Host ""
Write-Host "========================================="
Write-Host " Bootstrap Completed Successfully"
Write-Host "========================================="