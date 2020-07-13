# DocCanDo

## Set Up for Parsing
1. clone github repository.
1. Add 4 Directories/Folders within `parsedDocs`. Name them `Department`,  `Period`, `Network`, and `FPHR`.
1. Add XML files to the proper directories within `assets`.
1. Follow parser instructions (below).
1. Retrieve csv files from directories within`parsedDocs`.

### DepartmentParser
- Load `department` XML files into `/assets/DepartmentFiles/`.
- Open GitBash, use `cd` command to get into the DocCanDo directory, then run the following command
    - `python DepartmentParser.py`

### PeriodParser
- Load `department` XML files into `/assets/DepartmentFiles/`.
- Open GitBash, use `cd` command to get into the DocCanDo directory, then run the following command
    - `python PeriodParser.py`

### NetworkParser
- Load `network` XML files into `/assets/NetworkFiles/`.
- Open GitBash, use `cd` command to get into the DocCanDo directory, then run the following command
    - `python NetworkParser.py`

### FPHRParser
- Load `fpHoseRunning` XML files into `/assets/FPHRFiles/`.
- Open GitBash, use `cd` command to get into the DocCanDo directory, then run the following command
    - `python FPHRParser.py`
