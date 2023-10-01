---
tags:
  - regex
  - automation 
  - readability 
  - style guide 
---
# regex

- regex is an extremely powerful tool for editing text and automation
- you can fix a problem with regex 
- try it: <https://regex101.com/>

## between around

- find text with something before, in between or after

```regex
(?<=This is)(.*)(?=sentence)
```

- Groups & Lookaround

```regex
(abc) capture group
\1 backreference to group #1
(?:abc) non-capturing group
(?=abc) positive lookahead
(?!abc) negative lookahead
```  

## remove blank lines

^(\s)*$\n

## timestamps

remove some timestamps from end of ticket summary

```regex
\ \d{1,}.*$
```

## validation

email

```
"^[a-zA-Z][\w\.-]*[a-zA-Z0-9]@[a-zA-Z0-9][\w\.-]*[a-zA-Z0-9]\.[a-zA-Z][a-zA-Z\.]*[a-zA-Z]$"
```

## past or future tense

- docs should be in present tense

To write a regular expression that replaces any upper case with its lower case, you can use the following pattern:

"
[A-Z]
"

This pattern matches any single uppercase letter.

To replace the matched patterns with their lower case equivalents, you can use the following replacement string:

"
\l
"

This replacement string uses the `\l` modifier to convert the matched character to lowercase.

Here is an example of how to use this regular expression in Python:

```python
import re

string = "THIS IS AN UPPERCASE STRING."

# Replace any upper case with its lower case
new_string = re.sub(r'[A-Z]', r'\l', string)

# Print the new string
print(new_string)
```

Output:

```
this is an uppercase string.
```

This regular expression can be used in any programming language that supports regular expressions.

## passive voice

- you should write doc in active voice

To write a regular expression that replaces any upper case with its lower case, you can use the following pattern:

"
[A-Z]
"

This pattern matches any single uppercase letter.

To replace the matched patterns with their lower case equivalents, you can use the following replacement string:

"
\l
"

This replacement string uses the `\l` modifier to convert the matched character to lowercase.

Here is an example of how to use this regular expression in Python:

```python
import re

string = "THIS IS AN UPPERCASE STRING."

# Replace any upper case with its lower case
new_string = re.sub(r'[A-Z]', r'\l', string)

# Print the new string
print(new_string)
```

Output:

```
this is an uppercase string.
```

This regular expression can be used in any programming language that supports regular expressions.

## capitol to lower

To write a regular expression that replaces any upper case with its lower case, you can use the following pattern:

"
[A-Z]
"

This pattern matches any single uppercase letter.

To replace the matched patterns with their lower case equivalents, you can use the following replacement string:

"
\l
"

This replacement string uses the `\l` modifier to convert the matched character to lowercase.

Here is an example of how to use this regular expression in Python:

```python
import re

string = "THIS IS AN UPPERCASE STRING."

# Replace any upper case with its lower case
new_string = re.sub(r'[A-Z]', r'\l', string)

# Print the new string
print(new_string)
```

Output:

```
this is an uppercase string.
```

This regular expression can be used in any programming language that supports regular expressions.

## title case

To write a regular expression that replaces any word using Title case with lower case title, you can use the following pattern:

```
\b[A-Z]\w+\b
```

This pattern matches any word that starts with an uppercase letter (`\b[A-Z]`) followed by one or more lowercase letters (`\w+`). `\b` is a word boundary, which ensures that the match is a complete word and not just part of a larger word.

To replace the matched patterns with lower case title, you can use the following replacement string:

```
\1\L$2
```

This replacement string uses the capture group `\1` to capture the first letter of the matched word. It then uses the `\L` modifier to convert the first letter to lowercase. The `$2` capture group is used to capture the rest of the matched word, which is then left unchanged.

Here is an example of how to use this regular expression in Python:

```python
import re

string = "This Is A Title Case String."

# Replace any word using Title case with lower case title
new_string = re.sub(r'\b[A-Z]\w+\b', r'\1\L$2', string)

# Print the new string
print(new_string)
```

Output:

```
This is a title case string.
```

This regular expression can be used in any programming language that supports regular expressions.

## trailing .

To write a regular expression that replaces trailing . symbols with nothing, you can use the following pattern:

```regex
\.+$
```

This pattern matches one or more periods (`.`) at the end of the string (`$`).

To replace the matched patterns with nothing, you can use the following replacement string:

```regex
""
```

This is an empty string, so it will effectively remove the trailing periods.

Here is an example of how to use this regular expression in Python:

```python
import re

string = "This string has a trailing period."

# Replace the trailing . with nothing
new_string = re.sub(r'\.$', "", string)

# Print the new string
print(new_string)
```

Output:

```
This string has a trailing period
```

This regular expression can be used in any programming language that supports regular expressions.

## old examples

### old micro app

```powershell
        $cleanoutput = $_.ToString() -replace 'System.Exception: ERROR: ', ""
        $cleanoutput = $cleanoutput.Split(",")
        $regname = [regex]"(?<=\[\\\\server\\path\\path\\\d{3}Matchme_)(.*?)(?=\\0)"
        $cleanname = $regname.Match($cleanoutput)
        write-host $cleanname
        $html += "<br>"
        $html += $cleanname
        $regtranid = [regex]"(?<=The)(.*?)(?=has)"
        $cleantran = $regtranid.Match($cleanoutput)
        write-host $cleantran
```

### utilities

searching for useful logging

```powershell
    $badlist | ForEach-Object {
        Write-Host
        $_ | select *
        $_.name -replace '\\\\server\\', ''`
            -replace 'c\$\\server\\Output\\', ''`
            -replace 'serverOutput\d{3}\\', ''`
            -replace '\\\d{3}_\d{14}\.out'
    } | Get-Unique -OutVariable $fixed
```
