# Zuvio2Webex-group-csv

a simple script that generate group-information csv file for Webex from Zuvio.

---

## Usage
### Step 1
在Zuvio選擇"學生管理" -> "分組名單"
![zuvio_1.png](pic/zuvio_1.png)
### Step 2
下載名單
![zuvio_2.png](pic/zuvio_2.png)

### Step 3
執行指令，假設zuvio下載檔案為`zuvio.xlsx`;目標輸出檔案為`webex.csv`
```bash
python3 main.py zuvio.xlsx webex.csv
```

## Requirements
- pandas
