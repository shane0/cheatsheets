# flask

- digging up old python hacks do not try these at home

```python
import os
import subprocess

from cookiecutter.main import cookiecutter

cutter = r'c:\\cookiecutter\'
# outputdir = r'c:\examples'


def cutftp(proj, username, passw, ticketno, outputdir):
    """ cut cli app """
    try:
        print('cut ftp for ' + proj)
        print(str(outputdir))
        cookiecutter(cutter,
                     output_dir=outputdir,
                     no_input=True,
                     overwrite_if_exists=False,
                     extra_context={
                         'proj_name': proj,
                         'user': username,
                         'pwd': passw,
                         'ticket': ticketno
                     })
    except Exception as derp:
        print('ftp cutter failed ', derp)


# cutcliapp('test',r'z:\it\temp')

def main():
    pass


if __name__ == '__main__':
    main()

```

- flask calling cookiecutter to launch projects

```python
import os
import subprocess

from cookiecutter.main import cookiecutter

# folder with a cookiecutter template
cutter = r'c:\\cookiecutter'
# outputdir = r'c:\output'


def cutftp(proj, username, passw, ticketno, outputdir):
    """ cut cli app """
    try:
        print('cut ftp setup for ' + proj)
        print(str(outputdir))
        cookiecutter(cutter,
                     output_dir=outputdir,
                     no_input=True,
                     overwrite_if_exists=False,
                     extra_context={
                         'proj_name': proj,
                         'user': username,
                         'pwd': passw,
                         'ticket': ticketno
                     })
    except Exception as derp:
        print('cutter failed ', derp)


def main():
    pass

if __name__ == '__main__':
    main()

```

```python
import os
import subprocess
from cookiecutter.main import cookiecutter

cutter = r'c:\path\'
# outputdir = r'c:\output\'

def cutcliapp(project, outputfolder):
    """ cut cli app """
    try:
        print('cutting cli app for ' + project)
        cookiecutter(cutter,
                output_dir=outputfolder,
                no_input=True,
                overwrite_if_exists=True,
                extra_context={
                    'proj_name': project
                })
    except Exception:
        print('cutcliapp cutter failed')

# cutcliapp('test',r'y:\mapped\drives')


def main():
    pass


if __name__ == '__main__':
    main()
```

```python
    p = subprocess.Popen(['powershell.exe','C:/path/script.ps1'])
```

```python
@app.route('/scheduler/')
def UpdateScheduler():
    updateScript = subprocess.check_output(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./checks/scheduler\";"])
    flash('updating scheduler output')
    return render_template('utilities_scheduler.html',updateScript=updateScript)
```

```html
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul class=flashes>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
     {{updateScript}}
  {% endif %}
{% endwith %}
```

- converting pdfs
- reuqires ghostscript

```python
# ConvertPdfToTif
@app.route('/utilities/pdf2tif', methods=['POST'])
def ConvertPdfToTif():
    pdfPath=request.form['pdfPath']
    tifPath=request.form['tifPath']
    flash('Converting %s to %s' % (pdfPath, tifPath))
    p2t = subprocess.Popen(['powershell.exe','C:\\Users\\username\\\\pdf.ps1', pdfPath, tifPath])
    return render_template('utilities_pdf2tif.html', pdfPath=pdfPath, tifPath=tifPath)
```

```powershell
param(
  [string]$folder,
  [string]$destinationfolder
)

$($MyInvocation.MyCommand.Definition) >> C:\Users\username\log.md
get-date | ac  C:\Users\username\\log.md
write-host "running $($MyInvocation.MyCommand.Definition)"

write-host $folder $destinationfolder

Set-Location $folder
$tool = '\\server\GhostScript\bin\gswin32c.exe'
$pdfs = get-childitem . -recurse | where {$_.Extension -match "pdf"}
foreach($pdf in $pdfs)
    {
     #If any pdf is found in the source folder, checks to see if the destination folder exists, and if doesn't, creates it.
        if(-Not(test-path $destinationfolder))
        {
      New-Item -ItemType Directory -Force -Path $destinationfolder
        }
     #Sets the $tiff variable based on the name of the pdf, removes spaces.
        $tiff = $destinationfolder+'\'+($pdf.BaseName.split('.')[0] -replace (" " , "")) + '.tif'

     Write-Host Tiff path is $tiff

     #Checks to see if the tiff file already exists as destination folder and skips it.
        if(test-path $tiff)
        {
            "TIFF file already exists: " + $tiff
        }
        else
        {
            'Processing ' + $pdf.Name
      #Sets the output parameter for ghostscript. Can expand functionality later if necessary.
            $param = "-sOutputFile=$tiff"
            & $tool -q -dNOPAUSE -sDEVICE=tiffg4 $param -r300 $pdf.FullName -c quit
        }
    }
```

- 7 zip called from flask app

```powershell
function zipit([string]$copyme){
    $($MyInvocation.MyCommand.Definition) >> C:\Users\username\log.md
    "zipit triggered" | ac C:\Users\username\log.md
    get-date | ac  C:\Users\username\log.md
    $copyme | ac C:\Users\username\log.md
    $yymmdd = get-date -format yyyy-MM-dd-hhmm
    $Source = "$copyme"
    $Target = "$copyme\$yymmdd`copy.zip"
    & "C:\Program Files\7-Zip\7z.exe" a -mx=9  $Target $Source
    return "$Target"
}
```

- folder template

```powershell
function new-ticketfolder {
<#
.Synopsis
 daily use utility scripts
.Description
 creates files for projects 
.Example
 C:\PS>new-ticketfolder c:\foldername\
.Notes
 Name: new-ticketfolder
.Link

.Inputs
 folder name
.Outputs
 None
#Requires -Version 2.0
#>
[CmdletBinding(SupportsShouldProcess=$True)]
 Param
    (
        [Parameter(Mandatory=$true,HelpMessage="enter ticket folder")]
     [string]$ticketfolder

    )
    PROCESS {
   $($MyInvocation.MyCommand.Definition) >> C:\Users\\log.md
   get-date | ac  C:\Users\\log.md
   $ticketfolder | ac C:\Users\\log.md
        if ($pscmdlet.ShouldProcess("Continue?")) {

          #$ticketfolder = read-host 'enter ticket folder'
          $yyyymmdd = get-date -Format yyyy-MM-dd
          New-Item "$ticketfolder`\$yyyymmdd" -type directory -Force
          #  New-Item "$ticketfolder`\$yyyymmdd\index.md" -type file -Force
   $tfiles = @('C:\Users\username\cheater.md',
   'C:\Users\username\index.md',
   'C:\Users\username\fix.ps1',
   'C:\Users\username\fix.sql'
   )
   $tfiles | % {copy-item $_  "$ticketfolder`\$yyyymmdd" }
        }
        else {
            Write "nope, bad things happened"
        }
    }
    return "new ticket folder at $ticketfolder"
} #End function

```
