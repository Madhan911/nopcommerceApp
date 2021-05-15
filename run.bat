pytest -s -v -m "sanity" --html=madhan.html testCases/ capture sys --browser Chrome
rem pytest -v -s -m "regression" --html=Reports/madhan.html --capture sys testCases/ --browser Chrome
rem pytest -v -s -m "sanity and regression" --html=Reports/madhan.html --capture sys testCases/ --browser Chrome
