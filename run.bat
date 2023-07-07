pytest -v -m "sanity" --html=./Reports/report.html testCases --browser chrome
REM pytest -v -m "regression" --html=./Reports\report.html testCases --browser chrome
REM pytest -v -m "sanity or regression" --html=./Reports\report.html testCases --browser chrome

