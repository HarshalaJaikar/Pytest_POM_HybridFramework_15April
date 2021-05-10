pytest -s -v -m "sanity and regression" testCases/ --browser firefox
REM pytest -s -v -m "sanity" testCases/ --browser firefox
REM pytest -s -v -m "regression" testCases/ --browser firefox
REM pytest -s -v -m "sanity or regression" testCases/ --browser firefox