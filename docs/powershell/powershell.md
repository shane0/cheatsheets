# never use powershell

```bat
@REM Tokenize current date.
@for /f "tokens=1,2,3,4 delims=/ " %%a in ( 'date/t' ) do @set x=%%d
@for /f "tokens=1,2,3,4 delims=/ " %%a in ( 'date/t' ) do @set m=%%b
@for /f "tokens=1,2,3,4 delims=/ " %%a in ( 'date/t' ) do @set d=%%c

@REM run today if no date passed
@if "%3"=="" (
 @set yyyymmdd=%x%%m%%d%
) else (
 @set yyyymmdd=%3
)

@ECHO Running %0
@REM @ECHO For %YYYYMMDD%

@SET project=%1
@SET action=%2

@call %~dp0\config.bat
@ECHO calling %scriptpath% %project% %action% %csvpath%
@powershell -NoProfile -ExecutionPolicy Bypass %scriptpath% %csvpath% %project% %action% 

```

```powershell
param(
  $csvconfig,
  $project,
  $action

)

function Get-ScriptFull
{
    Split-Path $script:MyInvocation.MyCommand.Definition
    $MyInvocation.ScriptName.Replace((Split-Path $MyInvocation.ScriptName),'').TrimStart('')
}
$scriptrunning = Get-ScriptFull
write-host "running $scriptrunning"

# path to your config
# $csvconfig = 'clone.csv'

$csvdata = Import-Csv $csvconfig
$isodate = get-date -Format yyyy-MM-dd
$yymmdd = get-date -Format yyMMdd

    # custom wildcards use yymmdd for today 170504
    function update-set($csvdata){
        foreach($_ in $csvdata){
            $_.path = $_.path.Replace('yymmdd',$yymmdd) 
            $_.destination = $_.destination.Replace('yymmdd',$yymmdd) 
            $_.path = $_.path.Replace('yyyy-MM-dd',$isodate)
            $_.destination = $_.destination.Replace('yyyy-MM-dd',$isodate) 
            $_.path = $_.path.Replace('yesterday',$yesterday)
            $_.destination = $_.destination.Replace('yesterday',$yesterday) 
        }
        return $csvdata
    }
    update-set($csvdata) --quiet --no-verbose | out-null

    # logging
    function Get-ScriptDirectory
    {
        Split-Path $script:MyInvocation.MyCommand.Definition
    }
    $mypath = Get-ScriptDirectory
    write-host "running $mypath using $csvconfig"

# ftp get and put
function gettask($task){
    Set-Location C:\winscp
    Add-Type -Path "WinSCPnet.dll"
      # Set up session options
      $sessionOptions = New-Object WinSCP.SessionOptions -Property @{
          Protocol = [WinSCP.Protocol]::Sftp
          HostName = "sftp.your.com"
          UserName = "something"
          Password = "secrets"
          SshHostKeyFingerprint = "ssh-rsa 2048 e2:...:8a"
      }
    $session = New-Object WinSCP.Session
    try
        {
            # Connect
            $session.Open($sessionOptions)
            # Upload files
            $transferOptions = New-Object WinSCP.TransferOptions
            $transferOptions.TransferMode = [WinSCP.TransferMode]::Binary
            $transferResult = $session.GetFiles($task.destination, $task.path,  $False, $transferOptions)
            # Throw on any error
            $transferResult.Check()
            # Print results
            foreach ($transfer in $transferResult.Transfers)
            {
            Write-Host ("Download of {0} succeeded" -f $transfer.FileName)
            }
        }
    finally
    {
        $session.Dispose()
    }
        if($task.continue -eq 'y'){
            subchain $task
        }   
} # end gettask


# put
function puttask($task){
    Set-Location C:\winscp
    Add-Type -Path "WinSCPnet.dll"
        # Set up session options
        $sessionOptions = New-Object WinSCP.SessionOptions -Property @{
            Protocol = [WinSCP.Protocol]::Sftp
            HostName = "sftp.some.com"
            UserName = "someuser"
            Password = "pwdsecretomg"
            SshHostKeyFingerprint = "ssh-rsa 2048 0d:...8a"
        }
    $session = New-Object WinSCP.Session

    try
        {
            # Connect
            $session.Open($sessionOptions)
                # Upload files
                $transferOptions = New-Object WinSCP.TransferOptions
                $transferOptions.TransferMode = [WinSCP.TransferMode]::Binary
                $transferResult = $session.PutFiles($task.path, $task.destination)
                # Throw on any error
                $transferResult.Check()
                # Print results
                foreach ($transfer in $transferResult.Transfers)
                {
                    Write-Host ("Upload of {0} succeeded" -f $transfer.FileName)
                }
        }
    finally
    {
        $session.Dispose()
    }
        if($task.continue -eq 'y'){
            subchain $task
        }  
} # end puttask


function movetask($task){
          move-item $task.path $task.destination -Force
        if($task.continue -eq 'y'){
            subchain $task
        }
}

function copytask($task){
          copy-item $task.path $task.destination -Force
        if($task.continue -eq 'y'){
            subchain $task
        }
}

function renametask($task){
          rename-item -path $task.path -newname $task.destination -Force
        if($task.continue -eq 'y'){
            subchain $task
        }
}

function newtask($task){
        if(-not (test-path($task.path))){
            new-item -path $task.path -ItemType $task.type 
        } else {write-host "$($task.path) already exists"}
        # add test with email alert option to destination if this fails?
        if($task.continue -eq 'y'){
            subchain $task
        }
}

function removetask($task){
        if($task.type = 'recursive'){
         remove-item -path $task.path -Recurse
        }else{
          remove-item -path $task.path
        }
        if($task.continue -eq 'y'){
            subchain $task
        }      
}

function invoketask($task){
          invoke-item -path $task.path
        if($task.continue -eq 'y'){
            subchain $task
        }            
}

function cleartask($task){
          clear-content $task.path
        if($task.continue -eq 'y'){
            subchain $task
        }
}
function addtask($task){
          $task.destination | add-content $task.path
        if($task.continue -eq 'y'){
            subchain $task
        }
}
function cmdtask($task){
     & $task.path
        if($task.continue -eq 'y'){
            subchain $task
        }
}
function urltask($task){
          Start-Process "chrome.exe" $task.path
        if($task.continue -eq 'y'){
            subchain $task
        }  
}
function testtask($task){
        Test-Path($task.path)
        if(-not(test-path($task.path))){
            & dna $($task.destination) email
        & dna $task.destination email
        }
        if($task.continue -eq 'y'){
            subchain $task
        }  
}
function readtask($task){
          Get-Content $($task.path)
        if($task.continue -eq 'y'){
            subchain $task
        }
}
function listtask($task){
          Get-ChildItem $task.path -r
        if($task.continue -eq 'y'){
            subchain $task
        }  
}
function scrapetask($task){
          Invoke-WebRequest $task.path
        if($task.continue -eq 'y'){
            subchain $task
        }   
}
function servicetasktask($task){
          get-service -ComputerName $task.path
        if($task.continue -eq 'y'){
            subchain $task
        } 
}
function atomtask($task){
          atom -n -a $task.path
        if($task.continue -eq 'y'){
            subchain $task
        }  
}
function cliptask($task){
        $task.path | clip
        if($task.continue -eq 'y'){
        subchain $task
        }
}
function findtask($task){
        get-childitem -path $task.path -r | Select-String -pattern $task.destination | ForEach-Object {write-host "match in $task.path"}
        if($task.continue -eq 'y'){
            subchain $task
        }  
}
function filebackuptask($task){
  $newfile = "$($task.path)" + "." + "$isodate"
  copy-item -path $($task.path) -Destination $newfile -Force
        if($task.continue -eq 'y'){
            subchain $task
        } 
}
function ownertask($task){
    get-acl -Path $($task.path)
        if($task.continue -eq 'y'){
            subchain $task
        }  
}
function zipfoldertask($task){
    & "C:\Program Files\7-Zip\7z.exe" a -mx=9  $($task.destination) $($task.path)
        if($task.continue -eq 'y'){
            subchain $task
        } 
}
function emailtask($task){
$param = @{
    SmtpServer = '1.0.0.1'
    From = 'SUPPORT@your.com'
    To = $task.destination
    Subject = $task.path
    Body = "<html><body>$($task.type)<br></body></html>"
    BodyAsHtml = $true
}
Send-MailMessage @param
        if($task.continue -eq 'y'){
            subchain $task
        }
}

function removelinetask($task){
    $match = $task.type
    $clean = Get-Content $task.path | Where-Object {$_ -notmatch $match} 
    new-item $task.destination -ItemType file
    Clear-Content $task.destination
    $clean | Out-File $task.destination
        if($task.continue -eq 'y'){
            subchain $task
        }    
}

function replacelinetask($task){
    (Get-Content $task.path) | 
        Foreach-Object {$_ -replace $task.destination, $task.type}  | 
    Out-File $task.path
        if($task.continue -eq 'y'){
            subchain $task
        }
}
function expressionset($task){
        Invoke-Expression "& $($task.path)"
        if($task.continue -eq 'y'){
            subchain $task
        } 
}


# these are logic for running a whole project or just one type of action for one project
function subchain($task){
       & dna $task.subproject $task.subaction
}

function runone($action,$task){
      switch ($action) {
      get {gettask $task}
      put {puttask $task}
      move {movetask $task}
      copy  {copytask $task}
      clip {cliptask $task}
      rename {renametask $task}
      new  {newtask $task}
      remove {removetask $task}
      invoke  {invoketask $task}
      clear {cleartask $task}
      add {addtask $task}
      cmd {cmdtask $task}
      url {urltask $task}
      test {testtask $task}
      list {listtask $task}
      read {readtask $task}
      scrape {scrapetask $task}
      service {servicetask $task}
      atom {atomtask $task}
      find {findtask $task}
      filebackup {filebackuptask $task}
      zip {zipfoldertask $task}
      owner {ownertask $task}
      email {emailtask $task}
      removeline {removelinetask $task}
      replacestring {replacelinetask $task}
      iexp {expressionset $task}
        default {"missing parameters"}
      }
}



function runproject{
  $projectset = $csvdata | Where-Object {$_.project -eq $project}
    foreach($_ in $projectset){
        $action = $_.action
        runone -action $action -task $_
        start-sleep -s .5
    }
}


function filteroneaction($action){
  $taskset = $csvdata | Where-Object {$_.project -eq $project -and $_.action -eq $action}
  foreach($_ in $taskset){
        runone -action $_.action -task $_
  }
}

if($action -eq $null){
  write-host "no action passed running all actions on project $project"
  runproject
}
elseif ($action -ne $null) {
  write-host "running only task type $action on project $project"
  filteroneaction $action

}

```
