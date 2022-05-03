import pandas as pd
import sys

# return a group name : email mapping
def getGroupDict( df ):
    group = {}
    for i in range(df.shape[0]):
        if df.iloc[i,0] == '組別名稱':
            name = df.iloc[i,1]
            group[name] = []
        elif df.iloc[i,0] == '未分組名單': 
            name = '未分組' 
            group[name] = []
        else:
            for j in range(df.shape[1]):
                if isinstance(df.iloc[i,j], str) and '@' in df.iloc[i,j]:
                    group[name].append(df.iloc[i,j])
    return group


def main():
    # input args
    try:
        zuvio_path = sys.argv[1]
        webex_path = sys.argv[2]
    except:
        print("Usage: python3 main.py $ZUVIO_FILE $WEBEX_FILE")
        raise

    df=pd.read_excel(zuvio_path)

    output_data = []
    for k, v in getGroupDict(df).items():
        for email in v:
            output_data.append((k,email))

    # output csv
    pd.DataFrame( output_data , columns = ['預先指定的分組討論名稱', '電子郵件地址']).to_csv('webex.csv', index = False, encoding = 'utf-8')

if __name__ == '__main__':
    main()