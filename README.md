# KSV Demo Project

Simple project used to show all KaravaiSV abilities.

## About

This project's goal is to show [KaravaiSV](https://github.com/BIG-Denis/karavaisv) templating engine all it's abilities.

Learn more at [KaravaiSV GitHub page](https://github.com/BIG-Denis/karavaisv).

Use [KSV2VS](https://github.com/BIG-Denis/ksv2vs) VSCode extension to see KaravaiSV syntax highlightning.

## Usage

1. Install all dependencies via `pip install -r requirements.txt`
2. Run `python build.py` (python executable depending on OS may be named `python`, `python3` or `py`)
3. Check out rendered sources at `repo_root/build` (rtl and filelist)

> Try to change configs and see the rendered RTL changes (and all the power of templating)!

## Module description

This is a dummy module that simply serves multiple inputs width different width for a one output.  
Egress register is toggleble.  
Arbiter is chooseble (round robin is dummy).  
Assertions presence are toggleble.
