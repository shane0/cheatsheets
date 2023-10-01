# powershell

## zip folder

```powershell
#backup any folder
function zipit{
    param([string]$copyme)
        if (-not (test-path "$env:ProgramFiles\7-Zip\7z.exe")) {throw "$env:ProgramFiles\7-Zip\7z.exe needed"} 
        set-alias sz "$env:ProgramFiles\7-Zip\7z.exe" 
        $Source = "$copyme"
        $Target = "$copyme\copy.zip"
        sz a -mx=9 $Target $Source
}
zipit c:\path
```
