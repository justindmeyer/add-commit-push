# add-commit-push Automation with Python

## Author
Justin Meyer [justindmeyer@lewisu.edu](mailto:justindmeyer@lewisu.edu)

## Credits
[This StackOverflow thread](https://stackoverflow.com/questions/29716361/how-to-use-powershell-alias-cd-a-spec-directory) for help creating PowerShell aliases.

## License
Licensed under the MIT License. See (license file)[license.md] for more details.

## Notes
Permanent aliases implemented in PowerShell using the following commands:
```
function gotoa { set-location "C:\Users\Justin\lewis\cpsc-20000\sprint-5" }
set-alias g5 gotoa

function gotob { 
	set-location "C:\Users\Justin\lewis\cpsc-20000\sprint-5\add-commit-push"
	python.exe "add-commit-push.py"
}
set-alias acp gotob
```