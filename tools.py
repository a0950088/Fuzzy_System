def convertContentToFloat(contents): # 轉換.txt檔案資料
    for content in range(len(contents)):
        contents[content] = float(contents[content])
    return contents