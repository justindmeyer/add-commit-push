# add-commit-push

## Author

## Credits

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